# Azure RAG Insurance PoC - Local Python App

This app demonstrates a Retrieval-Augmented Generation (RAG) workflow for insurance use cases, using Azure OpenAI and Azure Cognitive Search. It is designed to run locally, using the sample insurance documents provided in the `sample-docs/` folder.

## App Structure

- `rag/` - Core RAG modules (document loader, embedder, retriever, LLM interface)
- `utils/` - Utility functions (config, logging, etc.)
- `main.py` - FastAPI app entry point (to be created)

## Azure Resource Configuration

This app requires Azure resource information, which should be set as environment variables (or in a `.env` file in the `app/` folder). Use the outputs from your Terraform deployment to populate these values.

### Example `.env` file (populate with your Terraform outputs):

```
# Azure OpenAI
AZURE_OPENAI_ENDPOINT=<output.openai_endpoint>
AZURE_OPENAI_KEY=<output.openai_key>
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=<output.openai_embedding_deployment>
AZURE_OPENAI_CHAT_DEPLOYMENT=<output.openai_chat_deployment>

# Azure Cognitive Search
AZURE_SEARCH_ENDPOINT=<output.cognitive_search_endpoint>
AZURE_SEARCH_KEY=<output.cognitive_search_key>
AZURE_SEARCH_INDEX=<output.cognitive_search_index_name>  # <-- Automatically created by Terraform

# Azure Key Vault
AZURE_KEY_VAULT_URI=<output.key_vault_uri>

# Azure Storage
AZURE_STORAGE_ACCOUNT=<output.storage_account_name>
AZURE_STORAGE_KEY=<output.storage_account_key>
AZURE_STORAGE_CONTAINER=<output.storage_container_name>

# Azure ML Workspace
AZURE_ML_WORKSPACE=<output.aml_workspace_name>
AZURE_ML_RESOURCE_GROUP=<output.resource_group_name>
AZURE_ML_SUBSCRIPTION_ID=<output.subscription_id>

# Managed Identity (optional)
AZURE_CLIENT_ID=<output.managed_identity_client_id>
```

- Replace `<output.*>` with the actual values from your Terraform outputs.
- All secrets and endpoints should be managed securely (use Key Vault in production).

---

**This ensures the app is fully cloud-ready and can be deployed or run locally using the same configuration.**

## Step 1: Document Loading and Preprocessing

The first step is to load and preprocess the sample insurance documents. This involves:

1. Reading all `.txt` files from the `sample-docs/` directory.
2. Splitting each document into manageable text chunks (for embedding and retrieval).
3. Storing the chunks in memory (for now; later, we will index them in Azure Cognitive Search).

We will implement this in `rag/doc_loader.py`.

---

## Step 2: Embedding the Chunks with Azure OpenAI

Now that your documents are chunked, the next step is to convert each chunk into a vector embedding using Azure OpenAI.

1. Set your Azure OpenAI credentials in a `.env` file in the `app/` folder:

```
AZURE_OPENAI_ENDPOINT=https://<your-resource-name>.openai.azure.com/
AZURE_OPENAI_KEY=<your-key>
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=<your-embedding-deployment-name>
```

2. The embedder module (`rag/embedder.py`) will use these credentials to call the Azure OpenAI embedding API and return a list of embeddings for your chunks.

---

## Step 3: Cognitive Search Integration (Vector Store)

Now that you have embeddings, you can store and retrieve them using Azure Cognitive Search.

- The retriever module (`rag/retriever.py`) provides functions to upload your chunks+embeddings to Azure Cognitive Search and to query for similar chunks using vector search.
- Make sure your index exists in Azure (see previous instructions for schema).
- Your `.env` must have the correct endpoint, key, and index name.

---

**Next steps will be explained as we proceed.** 