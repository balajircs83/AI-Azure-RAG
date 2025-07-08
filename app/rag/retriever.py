import os
import requests
from typing import List, Dict
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from app.utils.config import AZURE_SEARCH_ENDPOINT, AZURE_SEARCH_KEY, AZURE_SEARCH_INDEX

# Optionally set API version for REST calls (default to latest preview)
AZURE_SEARCH_API_VERSION = os.getenv("AZURE_SEARCH_API_VERSION", "2025-05-01-preview")

# Initialize the SearchClient for upload (SDK is fine for this)
search_client = SearchClient(
    endpoint=AZURE_SEARCH_ENDPOINT,
    index_name=AZURE_SEARCH_INDEX,
    credential=AzureKeyCredential(AZURE_SEARCH_KEY)
)

def upload_chunks(chunks: List[Dict]):
    """
    Uploads a list of chunk dicts (with 'content', 'embedding', etc.) to Azure Cognitive Search.
    Each chunk must have a unique 'id' field (can be source+chunk_id).
    """
    import re
    docs = []
    for chunk in chunks:
        safe_source = re.sub(r'[^A-Za-z0-9_\-=]', '_', chunk['source'])
        doc = {
            "id": f"{safe_source}-{chunk['chunk_id']}",
            "content": chunk["content"],
            "embedding": chunk["embedding"],
            "source": chunk["source"],
            "chunk_id": chunk["chunk_id"]
        }
        docs.append(doc)
    result = search_client.upload_documents(documents=docs)
    print(f"Uploaded {len(result)} documents to Azure Cognitive Search.")


def search_similar(query_embedding: List[float], top_k: int = 3) -> List[Dict]:
    """
    Uses the REST API to search Azure Cognitive Search for the top_k most similar chunks to the given embedding.
    Supports the 2025-05-01-preview API using the 'vectorQueries' parameter.
    Returns a list of matching documents.
    """
    url = f"{AZURE_SEARCH_ENDPOINT}/indexes/{AZURE_SEARCH_INDEX}/docs/search?api-version={AZURE_SEARCH_API_VERSION}"
    headers = {
        "Content-Type": "application/json",
        "api-key": AZURE_SEARCH_KEY
    }
    vector_query = {
        "kind": "vector",
        "vector": query_embedding,
        "k": top_k,
        "fields": "embedding"
    }
    data = {
        "vectorQueries": [vector_query]
    }
    response = requests.post(url, headers=headers, json=data)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Error response from Azure Search:", response.text)
        raise
    results = response.json()
    return results.get("value", [])

# Example usage (for testing):
if __name__ == "__main__":
    from app.rag.doc_loader import load_documents
    from app.rag.embedder import embed_chunks
    from app.rag.llm import generate_rag_answer
    import sys
    import re

    chunks = load_documents()
    chunks = embed_chunks(chunks)
    upload_chunks(chunks)

    # Accept a search query string from the user
    if len(sys.argv) > 1:
        user_query = " ".join(sys.argv[1:])
    else:
        user_query = input("Enter your search query: ")

    # Try to extract policy/claim number and policy holder from the query
    match_num = re.search(r'(policy|claim) number\s*:?\s*([A-Z0-9\-]+)', user_query, re.IGNORECASE)
    filter_number = match_num.group(2) if match_num else None
    match_holder = re.search(r'policy holder\s*:?\s*([A-Za-z ]+)', user_query, re.IGNORECASE)
    filter_holder = match_holder.group(1).strip().lower() if match_holder else None

    # Embed the user query
    import openai
    from app.utils.config import AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_KEY, AZURE_OPENAI_EMBEDDING_DEPLOYMENT
    openai.api_type = "azure"
    openai.api_base = AZURE_OPENAI_ENDPOINT
    openai.api_key = AZURE_OPENAI_KEY
    openai.api_version = "2023-05-15"
    embedding_response = openai.Embedding.create(
        input=[user_query],
        engine=AZURE_OPENAI_EMBEDDING_DEPLOYMENT
    )
    query_embedding = embedding_response["data"][0]["embedding"]

    # Search for similar chunks to the query embedding (increase top_k)
    hits = search_similar(query_embedding, top_k=5)
    print("\nTop matching chunks:")
    for hit in hits:
        print(hit)

    # Filtering logic
    filtered_hits = chunks
    if filter_number:
        filtered_hits = [c for c in filtered_hits if c.get('policy_or_claim_number') == filter_number]
    if filter_holder:
        filtered_hits = [c for c in filtered_hits if c.get('policy_holder') == filter_holder]
    if (filter_number or filter_holder) and filtered_hits:
        print(f"\nFiltered to {len(filtered_hits)} chunks with", end=' ')
        if filter_number:
            print(f"policy/claim number {filter_number}", end=' ')
        if filter_holder:
            print(f"policy holder {filter_holder}", end=' ')
        print()
        hits = filtered_hits

    # Generate and print the RAG answer
    answer = generate_rag_answer(user_query, hits)
    print("\nRAG Answer:\n", answer)

    # Test multiple scenarios
    if len(sys.argv) == 1:
        print("\n--- Test: status of policy number : HLTH-987654 ---")
        test_query = "status of policy number : HLTH-987654"
        embedding_response = openai.Embedding.create(
            input=[test_query],
            engine=AZURE_OPENAI_EMBEDDING_DEPLOYMENT
        )
        test_embedding = embedding_response["data"][0]["embedding"]
        test_hits = search_similar(test_embedding, top_k=5)
        test_filtered = [c for c in chunks if c.get('policy_or_claim_number') == 'HLTH-987654']
        if test_filtered:
            test_hits = test_filtered
        print("Test hits:", test_hits)
        print("RAG Answer:", generate_rag_answer(test_query, test_hits))

        print("\n--- Test: claim number of policy holder john doe ---")
        test_query2 = "claim number of policy holder john doe"
        embedding_response = openai.Embedding.create(
            input=[test_query2],
            engine=AZURE_OPENAI_EMBEDDING_DEPLOYMENT
        )
        test_embedding2 = embedding_response["data"][0]["embedding"]
        test_hits2 = search_similar(test_embedding2, top_k=5)
        test_filtered2 = [c for c in chunks if c.get('policy_holder') == 'john doe']
        if test_filtered2:
            test_hits2 = test_filtered2
        print("Test hits:", test_hits2)
        print("RAG Answer:", generate_rag_answer(test_query2, test_hits2)) 