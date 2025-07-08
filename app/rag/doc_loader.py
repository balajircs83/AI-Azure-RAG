import os
import re
from typing import List, Dict

SAMPLE_DOCS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'sample-docs')

# Simple text splitter: splits on paragraphs, then further splits long paragraphs
CHUNK_SIZE = 500  # characters
CHUNK_OVERLAP = 50  # characters

def extract_policy_or_claim_number(text: str) -> str:
    # Try to extract Policy Number or Claim Number
    match = re.search(r'(Policy Number|Claim Number):\s*([A-Z0-9\-]+)', text)
    if match:
        return match.group(2)
    return ""

def extract_policy_holder(text: str) -> str:
    match = re.search(r'Policy Holder:\s*([A-Za-z ]+)', text)
    if match:
        return match.group(1).strip().lower()
    return ""

def load_documents() -> List[Dict]:
    """
    Loads all .txt files from the sample-docs directory, splits them into chunks, and returns a list of dicts:
    { 'content': str, 'source': str, 'chunk_id': int, 'policy_or_claim_number': str, 'policy_holder': str }
    """
    docs = []
    for fname in os.listdir(SAMPLE_DOCS_DIR):
        if fname.endswith('.txt'):
            path = os.path.join(SAMPLE_DOCS_DIR, fname)
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
            policy_or_claim_number = extract_policy_or_claim_number(text)
            policy_holder = extract_policy_holder(text)
            # Split into paragraphs
            paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
            chunk_id = 0
            for para in paragraphs:
                # Further split long paragraphs into overlapping chunks
                start = 0
                while start < len(para):
                    chunk = para[start:start+CHUNK_SIZE]
                    docs.append({
                        'content': chunk,
                        'source': fname,
                        'chunk_id': chunk_id,
                        'policy_or_claim_number': policy_or_claim_number,
                        'policy_holder': policy_holder
                    })
                    chunk_id += 1
                    start += CHUNK_SIZE - CHUNK_OVERLAP
    return docs

# Example usage (for testing):
if __name__ == "__main__":
    chunks = load_documents()
    print(f"Loaded {len(chunks)} chunks.")
    for c in chunks[:3]:
        print(c) 