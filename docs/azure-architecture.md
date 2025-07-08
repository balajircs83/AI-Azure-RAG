# Azure Insurance RAG PoC Solution Documentation

## 1. Project Overview
This Proof of Concept (PoC) demonstrates an enterprise Retrieval-Augmented Generation (RAG) system for the insurance domain, leveraging Azure services for secure, scalable, and efficient question answering over insurance documents.

### Goal
Enable insurance agents, customers, or support staff to ask natural language questions about insurance policies, claims, and procedures, and receive accurate, context-rich answers by leveraging enterprise documents and LLMs.

---

## 2. High-Level Architecture
- **Data Storage:** Azure Blob Storage (raw and processed documents)
- **Data Ingestion & Processing:** Azure Functions (triggered on Blob upload)
- **Embedding Generation:** Azure Machine Learning (batch embedding generation)
- **Vector Store:** Azure Cognitive Search (vector search)
- **Retrieval & Orchestration:** Azure Functions (retrieval and LLM orchestration)
- **LLM Inference:** Azure OpenAI Service (managed LLM)
- **API Layer:** Azure API Management (REST endpoint)
- **Security & Monitoring:** Azure Active Directory (AAD), Key Vault, Monitor, Managed Identities

---

## 3. Implementation Steps
1. **Data Collection & Storage**
   - Upload insurance documents to Azure Blob Storage.
2. **Data Ingestion & Preprocessing**
   - Azure Function triggered by Blob upload to extract, clean, and preprocess documents.
   - Store cleaned data in Blob Storage.
3. **Embedding Generation**
   - Azure Machine Learning batch job generates embeddings for processed documents.
   - Store embeddings in Azure Cognitive Search.
4. **Vector Storage & Retrieval**
   - Store all embeddings in Azure Cognitive Search.
   - Azure Function queries Cognitive Search for top-k relevant documents based on user query embedding.
5. **LLM Orchestration & Generation**
   - Azure Function sends retrieved context and user query to Azure OpenAI Service for answer generation.
   - Process and return LLM output.
6. **API Exposure**
   - Expose orchestration as a REST API via Azure API Management.
   - Secure with Azure Active Directory (AAD).
7. **Monitoring & Security**
   - Use Managed Identities for access control, Key Vault for secrets/encryption, and Azure Monitor for logging/monitoring.

---

## 4. Recommended Folder Structure

```
/ (project root)
│
├── infra/                  # Terraform IaC for Azure resources
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── ...
│
├── app/                    # Python application code
│   ├── main.py             # Python app entrypoint
│   ├── rag/
│   │   ├── embedding.py    # Embedding generation logic
│   │   ├── retrieval.py    # Cognitive Search retrieval logic
│   │   ├── llm.py          # Azure OpenAI integration
│   │   └── ...
│   ├── utils/
│   └── requirements.txt
│
├── docs/                   # Documentation
│   └── azure-architecture.md
│
├── .github/
│   └── copilot-instructions.md
│
└── README.md
```

---

## 5. Functional Requirements
- Upload insurance documents (policies, claims, FAQs) to Azure Blob Storage
- Preprocess and index documents for semantic search
- Accept user queries via API
- Retrieve relevant document snippets using vector search
- Generate context-aware answers using LLM
- Provide API endpoint for querying and retrieving answers
- User authentication (Azure AD)
- Logging and monitoring

---

## 6. Tech Stack
- **IaC:** Terraform (for all Azure resource deployment)
- **Backend:** Python (for all application code)
- **ML/AI:** Azure Machine Learning, Azure OpenAI Service
- **Vector Store:** Azure Cognitive Search
- **Storage:** Azure Blob Storage
- **Auth:** Azure Active Directory
- **Monitoring:** Azure Monitor

---

## 7. Next Steps
- Scaffold the folder structure above
- Implement Terraform modules for each Azure resource
- Develop Python app for RAG workflow
- Integrate, test, and iterate

---

*For further details, see the implementation steps and folder structure above. Update this document as the project evolves.* 