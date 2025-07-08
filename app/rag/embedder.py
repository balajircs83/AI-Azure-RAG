import openai
from typing import List, Dict
from app.utils.config import AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_KEY, AZURE_OPENAI_EMBEDDING_DEPLOYMENT

openai.api_type = "azure"
openai.api_base = AZURE_OPENAI_ENDPOINT
openai.api_key = AZURE_OPENAI_KEY
openai.api_version = "2023-05-15"  # Use the version your Azure OpenAI resource supports

def embed_chunks(chunks: List[Dict]) -> List[Dict]:
    """
    Given a list of chunk dicts (with 'content'), returns a list of dicts with 'embedding' and original metadata.
    """
    texts = [chunk['content'] for chunk in chunks]
    # Azure OpenAI supports batch embedding (up to 16 per request for text-embedding-ada-002)
    batch_size = 16
    results = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i+batch_size]
        response = openai.Embedding.create(
            input=batch,
            engine=AZURE_OPENAI_EMBEDDING_DEPLOYMENT
        )
        for j, record in enumerate(response['data']):
            # Attach embedding to the corresponding chunk
            chunk_with_embedding = dict(chunks[i+j])
            chunk_with_embedding['embedding'] = record['embedding']
            results.append(chunk_with_embedding)
    return results

# Example usage (for testing):
if __name__ == "__main__":
    from app.rag.doc_loader import load_documents
    chunks = load_documents()
    embeddings = embed_chunks(chunks)
    print(f"Embedded {len(embeddings)} chunks. Example:")
    print(embeddings[0].keys()) 