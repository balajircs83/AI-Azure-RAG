import openai
from typing import List, Dict
from app.utils.config import AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_KEY, AZURE_OPENAI_CHAT_DEPLOYMENT

openai.api_type = "azure"
openai.api_base = AZURE_OPENAI_ENDPOINT
openai.api_key = AZURE_OPENAI_KEY
openai.api_version = "2023-05-15"

def generate_rag_answer(user_query: str, retrieved_chunks: List[Dict]) -> str:
    """
    Formats a prompt with retrieved context and calls Azure OpenAI chat completion to generate an answer.
    """
    context = "\n\n".join([chunk.get("content", "") for chunk in retrieved_chunks])
    prompt = f"""
You are an insurance assistant. Use ONLY the following context to answer the user's question. If the user's question is about the status of a claim or policy, look for a line starting with 'Status:' in the context and extract its value exactly. If the answer is not in the context, say you don't know.

Context:
{context}

User question: {user_query}
"""
    messages = [
        {"role": "system", "content": "You are a helpful insurance assistant."},
        {"role": "user", "content": prompt}
    ]
    response = openai.ChatCompletion.create(
        engine=AZURE_OPENAI_CHAT_DEPLOYMENT,
        messages=messages,
        temperature=0.2,
        max_tokens=512
    )
    return response["choices"][0]["message"]["content"].strip()

# Example usage (for testing):
if __name__ == "__main__":
    # Example: user_query and fake chunks
    user_query = "How do I file a claim for my auto policy?"
    chunks = [
        {"content": "Claims Process: Report incident within 48 hours. Submit claim form and supporting documents. Inspection and approval within 7 business days."}
    ]
    answer = generate_rag_answer(user_query, chunks)
    print("RAG Answer:\n", answer) 