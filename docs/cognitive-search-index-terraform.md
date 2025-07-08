# Cognitive Search Index Implementation

## Overview

This document describes the implementation of Azure Cognitive Search index creation for the insurance RAG PoC project.

## What Was Implemented

### 1. Index Schema Definition

The Cognitive Search index is created with the following schema:

| Field | Type | Purpose | Searchable | Filterable | Sortable | Facetable |
|-------|------|---------|------------|------------|----------|-----------|
| `id` | Edm.String | Primary key | No | No | No | No |
| `content` | Edm.String | Document text content | Yes | No | No | No |
| `embedding` | Collection(Edm.Single) | Vector embeddings (1536 dim) | No | No | No | No |
| `source` | Edm.String | Source document filename | Yes | Yes | Yes | Yes |
| `chunk_id` | Edm.Int32 | Chunk sequence number | No | Yes | Yes | No |
| `policy_or_claim_number` | Edm.String | Policy/claim identifier | Yes | Yes | Yes | Yes |
| `policy_holder` | Edm.String | Policy holder name | Yes | Yes | Yes | Yes |

### 2. Vector Search Configuration

- **Vector dimensions**: 1536 (compatible with OpenAI text-embedding-ada-002)
- **Vector search algorithm**: HNSW (Hierarchical Navigable Small World)
- **Semantic search**: Enabled with default configuration

### 3. Implementation Approach

Since Azure Cognitive Search indexes are not supported as native Terraform resources, we use a two-step approach:

1. **Terraform**: Creates the Azure Cognitive Search service
2. **PowerShell Script**: Creates the index with the required schema

#### Terraform Resources

```hcl
# infra/modules/cognitive_search/main.tf
resource "azurerm_search_service" "this" {
  name                = var.search_service_name
  resource_group_name = var.resource_group_name
  location            = var.location
  sku                 = var.sku
  partition_count     = 1
  replica_count       = 1
  tags                = var.common_tags
}
```

#### PowerShell Script

```powershell
# create-search-index.ps1
# Creates the index using Azure REST API
az rest --method PUT `
  --url "https://$SearchServiceName.search.windows.net/indexes/$IndexName?api-version=2025-05-01-preview" `
  --headers "Content-Type=application/json" `
  --body "@$tempFile"
```

## Implementation Notes

### Why PowerShell Script Instead of Native Terraform Resource?

Azure Cognitive Search indexes are not currently supported as native Terraform resources in the Azure provider. This is a common limitation with some Azure services. We use a PowerShell script with Azure CLI REST API calls to create the index.

### Prerequisites

- Azure CLI must be installed and authenticated
- User must have appropriate permissions to create search indexes
- PowerShell execution policy must allow script execution

### Benefits

1. **Infrastructure as Code**: Index creation is version-controlled and reproducible
2. **Consistency**: Ensures the same index schema across all environments
3. **Automation**: No manual index creation required in Azure Portal
4. **Integration**: Seamlessly integrates with the existing RAG application

## Usage

### Step 1: Deploy Infrastructure
```bash
cd infra
terraform plan
terraform apply
```

### Step 2: Create the Index
```bash
# Option 1: Run the batch file
create-index.bat

# Option 2: Run PowerShell script directly
powershell -ExecutionPolicy Bypass -File "create-search-index.ps1"
```

### Step 3: Application Configuration
The index name is available as a Terraform output and can be used in the application:

```bash
# Get the index name
terraform output cognitive_search_index_name

# Use in .env file
AZURE_SEARCH_INDEX=$(terraform output -raw cognitive_search_index_name)
```

## Files Created

- `create-search-index.ps1` - PowerShell script to create the index
- `create-index.bat` - Batch file for easy execution
- Updated Terraform configuration (removed problematic null_resource)

## Compatibility

The index schema is designed to work with:
- **OpenAI text-embedding-ada-002**: 1536-dimensional embeddings
- **Azure Cognitive Search 2025-05-01-preview API**: Vector search support
- **Existing RAG application**: All required fields are included

## Next Steps

1. Deploy the updated Terraform configuration
2. Run the index creation script
3. Update application environment variables to use the new output
4. Test the RAG workflow with the automatically created index
5. Consider adding index management features (reindexing, schema updates)

## Notes

- The index uses the "basic" SKU of Cognitive Search, which supports vector search
- Vector search requires the 2025-05-01-preview API version
- The index is optimized for insurance document retrieval with policy/claim filtering capabilities
- Azure CLI must be installed and authenticated for index creation to work
- PowerShell execution policy may need to be adjusted to run the script 