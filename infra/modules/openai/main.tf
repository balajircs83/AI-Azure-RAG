resource "azurerm_cognitive_account" "this" {
  name                = var.openai_account_name
  location            = var.location
  resource_group_name = var.resource_group_name
  kind                = "OpenAI"
  sku_name            = var.sku_name
  tags                = var.common_tags
} 