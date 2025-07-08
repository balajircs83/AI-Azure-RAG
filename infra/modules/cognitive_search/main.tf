resource "azurerm_search_service" "this" {
  name                = var.search_service_name
  resource_group_name = var.resource_group_name
  location            = var.location
  sku                 = var.sku
  partition_count     = 1
  replica_count       = 1
  tags                = var.common_tags
}

# Note: Azure Cognitive Search indexes are not supported as Terraform resources
# Use the create-search-index.ps1 script to create the index after deploying the search service 
