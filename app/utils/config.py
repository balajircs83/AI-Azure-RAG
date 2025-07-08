import os
from dotenv import load_dotenv

# Load .env file if present
load_dotenv()

# Azure OpenAI
AZURE_OPENAI_ENDPOINT = os.getenv('AZURE_OPENAI_ENDPOINT')
AZURE_OPENAI_KEY = os.getenv('AZURE_OPENAI_KEY')
AZURE_OPENAI_EMBEDDING_DEPLOYMENT = os.getenv('AZURE_OPENAI_EMBEDDING_DEPLOYMENT')
AZURE_OPENAI_CHAT_DEPLOYMENT = os.getenv('AZURE_OPENAI_CHAT_DEPLOYMENT')

# Azure Cognitive Search
AZURE_SEARCH_ENDPOINT = os.getenv('AZURE_SEARCH_ENDPOINT')
AZURE_SEARCH_KEY = os.getenv('AZURE_SEARCH_KEY')
AZURE_SEARCH_INDEX = os.getenv('AZURE_SEARCH_INDEX', 'insurance-rag-index')

# Azure Key Vault
AZURE_KEY_VAULT_URI = os.getenv('AZURE_KEY_VAULT_URI')

# Azure Storage
AZURE_STORAGE_ACCOUNT = os.getenv('AZURE_STORAGE_ACCOUNT')
AZURE_STORAGE_KEY = os.getenv('AZURE_STORAGE_KEY')
AZURE_STORAGE_CONTAINER = os.getenv('AZURE_STORAGE_CONTAINER')

# Azure ML Workspace
AZURE_ML_WORKSPACE = os.getenv('AZURE_ML_WORKSPACE')
AZURE_ML_RESOURCE_GROUP = os.getenv('AZURE_ML_RESOURCE_GROUP')
AZURE_ML_SUBSCRIPTION_ID = os.getenv('AZURE_ML_SUBSCRIPTION_ID')

# Managed Identity (optional, for cloud deployment)
AZURE_CLIENT_ID = os.getenv('AZURE_CLIENT_ID')

# Validate required variables for local dev (OpenAI, Search)
required_vars = [
    AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_KEY, AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
    AZURE_SEARCH_ENDPOINT, AZURE_SEARCH_KEY, AZURE_SEARCH_INDEX
]
if not all(required_vars):
    raise ValueError("Please set all required Azure resource environment variables in your environment or .env file. See README for details.") 