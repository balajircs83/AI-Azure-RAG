output "openai_account_id" {
  value = azurerm_cognitive_account.this.id
}

output "openai_account_name" {
  value = azurerm_cognitive_account.this.name
}

output "openai_endpoint" {
  value = azurerm_cognitive_account.this.endpoint
}

output "openai_key" {
  value = azurerm_cognitive_account.this.primary_access_key
}

output "openai_embedding_deployment" {
  value = var.embedding_deployment_name
}

output "openai_chat_deployment" {
  value = var.chat_deployment_name
} 