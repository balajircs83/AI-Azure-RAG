from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.rag.doc_loader import load_documents
from app.rag.embedder import embed_chunks
from app.rag.retriever import search_similar
from app.rag.llm import generate_rag_answer
import openai
from app.utils.config import AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_KEY, AZURE_OPENAI_EMBEDDING_DEPLOYMENT
import re

app = FastAPI()

# Preload and embed docs at startup
chunks = embed_chunks(load_documents())

class RAGRequest(BaseModel):
    query: str

@app.post("/rag")
async def rag_endpoint(request: RAGRequest):
    user_query = request.query
    # Extract policy/claim number and policy holder
    match_num = re.search(r'(policy|claim) number\s*:?\s*([A-Z0-9\-]+)', user_query, re.IGNORECASE)
    filter_number = match_num.group(2) if match_num else None
    match_holder = re.search(r'policy holder\s*:?\s*([A-Za-z ]+)', user_query, re.IGNORECASE)
    filter_holder = match_holder.group(1).strip().lower() if match_holder else None
    # Embed the user query
    openai.api_type = "azure"
    openai.api_base = AZURE_OPENAI_ENDPOINT
    openai.api_key = AZURE_OPENAI_KEY
    openai.api_version = "2023-05-15"
    embedding_response = openai.Embedding.create(
        input=[user_query],
        engine=AZURE_OPENAI_EMBEDDING_DEPLOYMENT
    )
    query_embedding = embedding_response["data"][0]["embedding"]
    # Vector search
    hits = search_similar(query_embedding, top_k=5)
    # Filtering logic
    filtered_hits = chunks
    if filter_number:
        filtered_hits = [c for c in filtered_hits if c.get('policy_or_claim_number') == filter_number]
    if filter_holder:
        filtered_hits = [c for c in filtered_hits if c.get('policy_holder') == filter_holder]
    if (filter_number or filter_holder) and filtered_hits:
        hits = filtered_hits
    # Generate answer
    answer = generate_rag_answer(user_query, hits)
    # Return answer, chunks, and sources
    return {
        "answer": answer,
        "chunks": hits,
        "sources": list({c['source'] for c in hits})
    } 