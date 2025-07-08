# AWS Insurance RAG PoC Solution Documentation

## 1. Project Overview
This Proof of Concept (PoC) demonstrates an enterprise Retrieval-Augmented Generation (RAG) system for the insurance domain, leveraging AWS services for secure, scalable, and efficient question answering over insurance documents.

### Goal
Enable insurance agents, customers, or support staff to ask natural language questions about insurance policies, claims, and procedures, and receive accurate, context-rich answers by leveraging enterprise documents and LLMs.

---

## 2. High-Level Architecture
- **Data Storage:** Amazon S3 (raw and processed documents)
- **Data Ingestion & Processing:** AWS Lambda (triggered on S3 upload)
- **Embedding Generation:** Amazon SageMaker (batch embedding generation)
- **Vector Store:** Amazon OpenSearch Service (k-NN vector search)
- **Retrieval & Orchestration:** AWS Lambda (retrieval and LLM orchestration)
- **LLM Inference:** Amazon Bedrock (managed LLM)
- **API Layer:** Amazon API Gateway (REST endpoint)
- **Security & Monitoring:** IAM, KMS, CloudWatch, Cognito

---

## 3. Implementation Steps
1. **Data Collection & Storage**
   - Upload insurance documents to S3.
2. **Data Ingestion & Preprocessing**
   - Lambda function triggered by S3 upload to extract, clean, and preprocess documents.
   - Store cleaned data in S3.
3. **Embedding Generation**
   - SageMaker batch job generates embeddings for processed documents.
   - Store embeddings in OpenSearch.
4. **Vector Storage & Retrieval**
   - Store all embeddings in OpenSearch Service.
   - Lambda queries OpenSearch for top-k relevant documents based on user query embedding.
5. **LLM Orchestration & Generation**
   - Lambda sends retrieved context and user query to Bedrock for answer generation.
   - Process and return LLM output.
6. **API Exposure**
   - Expose Lambda orchestration as a REST API via API Gateway.
   - Secure with Cognito.
7. **Monitoring & Security**
   - Use IAM for access control, KMS for encryption, and CloudWatch for logging/monitoring.

---

## 4. Recommended Folder Structure

```
/ (project root)
│
├── infra/                  # Terraform IaC for AWS resources
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── ...
│
├── app/                    # Python application code
│   ├── main.py             # FastAPI/Flask app entrypoint
│   ├── rag/
│   │   ├── embedding.py    # Embedding generation logic
│   │   ├── retrieval.py    # OpenSearch retrieval logic
│   │   ├── llm.py          # Bedrock LLM integration
│   │   └── ...
│   ├── utils/
│   └── requirements.txt
│
├── docs/                   # Documentation
│   └── architecture.md
│
├── .github/
│   └── copilot-instructions.md
│
└── README.md
```

---

## 5. Functional Requirements
- Upload insurance documents (policies, claims, FAQs) to S3
- Preprocess and index documents for semantic search
- Accept user queries via API
- Retrieve relevant document snippets using vector search
- Generate context-aware answers using LLM
- Provide API endpoint for querying and retrieving answers
- User authentication (Cognito)
- Logging and monitoring

---

## 6. Tech Stack
- **IaC:** Terraform
- **Backend:** Python (FastAPI/Flask)
- **ML/AI:** SageMaker, Bedrock
- **Vector Store:** OpenSearch
- **Storage:** S3
- **Auth:** Cognito
- **Monitoring:** CloudWatch

---

## 7. Next Steps
- Scaffold the folder structure above
- Implement Terraform modules for each AWS resource
- Develop Python app for RAG workflow
- Integrate, test, and iterate

---

*For further details, see the implementation steps and folder structure above. Update this document as the project evolves.*
