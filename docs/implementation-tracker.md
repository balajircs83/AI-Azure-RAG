# Azure Insurance RAG PoC Implementation Tracker

This tracker breaks down the implementation phases and steps for the Azure-based RAG solution. Use the checkboxes to track progress during development.

---

## Phase 1: Data Collection & Storage
- [x] Set up Azure Blob Storage account and containers
- [ ] Define document organization structure in Blob Storage
- [ ] Upload sample insurance documents (policies, claims, FAQs)
- [x] Set up access policies and permissions

---

## Phase 2: Data Ingestion & Preprocessing
- [x] Develop Azure Function to trigger on Blob upload
- [ ] Implement document extraction and cleaning logic
- [ ] Store cleaned/preprocessed documents in Blob Storage
- [ ] Log ingestion and preprocessing events

---

## Phase 3: Embedding Generation
- [x] Set up Azure Machine Learning workspace
- [ ] Develop batch job for embedding generation
- [ ] Integrate with Azure OpenAI or custom embedding model
- [ ] Store generated embeddings in Azure Cognitive Search

---

## Phase 4: Vector Storage & Retrieval
- [x] Set up Azure Cognitive Search with vector search enabled
- [x] Define and create index schema for insurance documents
- [ ] Implement Azure Function to query Cognitive Search for top-k relevant documents
- [ ] Test retrieval with sample queries

---

## Phase 5: LLM Orchestration & Generation
- [x] Set up Azure OpenAI Service (provision model deployment)
- [ ] Develop Azure Function to orchestrate retrieval and LLM call
- [ ] Format prompt with retrieved context and user query
- [ ] Process and return LLM output

---

## Phase 6: API Exposure
- [ ] Develop REST API endpoint (FastAPI/Flask)
- [ ] Integrate API with Azure API Management *(skipped for PoC)*
- [x] Secure API with Azure Active Directory (AAD)
- [ ] Document API usage and authentication

---

## Phase 7: Monitoring & Security
- [x] Configure Managed Identities for all Azure resources
- [x] Store secrets and keys in Azure Key Vault
- [x] Set up Azure Monitor for logging and alerting
- [ ] Implement access control and audit logging

---

## General Project Steps
- [x] Scaffold recommended folder structure
- [x] Write and maintain project documentation
- [x] Implement Infrastructure as Code (Bicep/Terraform)
- [ ] Conduct integration and end-to-end testing
- [ ] Review and iterate based on feedback

---

*Update this tracker as the project progresses. Add or adjust steps as needed for your team's workflow.* 