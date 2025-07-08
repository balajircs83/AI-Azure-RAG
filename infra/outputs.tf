# Outputs for app development

output "openai_endpoint" {
  value = module.openai.openai_endpoint
}

output "openai_key" {
  value     = module.openai.openai_key
  sensitive = true
}

output "openai_embedding_deployment" {
  value = module.openai.openai_embedding_deployment
}

output "openai_chat_deployment" {
  value = module.openai.openai_chat_deployment
}

output "cognitive_search_endpoint" {
  value = module.cognitive_search.cognitive_search_endpoint
}

output "cognitive_search_key" {
  value     = module.cognitive_search.cognitive_search_key
  sensitive = true
}

output "cognitive_search_index_name" {
  value = module.cognitive_search.cognitive_search_index_name
  description = "Cognitive Search index name for RAG documents"
}

output "storage_account_key" {
  value     = module.storage.storage_account_key
  sensitive = true
}

output "aml_workspace_name" {
  value = module.aml_workspace.aml_workspace_name
}

output "managed_identity_client_id" {
  value = module.managed_identity.managed_identity_client_id
}

output "aml_workspace_id" {
  value = module.aml_workspace.workspace_id
  description = "Azure Machine Learning workspace ID"
}

output "key_vault_id" {
  value = module.aml_workspace.key_vault_id
  description = "Azure Key Vault resource ID (from AML workspace)"
}

output "key_vault_name" {
  value = module.aml_workspace.key_vault_name
  description = "Azure Key Vault name (from AML workspace)"
}

output "key_vault_uri" {
  value = module.aml_workspace.key_vault_uri
  description = "Azure Key Vault URI (from AML workspace)"
}

output "storage_account_name" {
  value = module.storage.storage_account_name
  description = "Azure Storage Account name"
}

output "storage_account_id" {
  value = module.storage.storage_account_id
  description = "Azure Storage Account resource ID"
}

output "storage_container_name" {
  value = module.storage.container_name
  description = "Azure Storage Container name"
}

output "function_app_name" {
  value = module.function_app.function_app_name
  description = "Azure Function App name"
}

output "function_app_id" {
  value = module.function_app.function_app_id
  description = "Azure Function App resource ID"
}

output "function_app_hostname" {
  value = module.function_app.default_hostname
  description = "Azure Function App default hostname"
}

output "managed_identity_name" {
  value = module.managed_identity.identity_name
  description = "Managed Identity name"
}

output "managed_identity_id" {
  value = module.managed_identity.identity_id
  description = "Managed Identity resource ID"
}

output "log_analytics_name" {
  value = module.monitor.log_analytics_name
  description = "Log Analytics Workspace name"
}

output "log_analytics_id" {
  value = module.monitor.log_analytics_id
  description = "Log Analytics Workspace resource ID"
}

output "vnet_name" {
  value = module.network.vnet_name
  description = "Virtual Network name"
}

output "vnet_id" {
  value = module.network.vnet_id
  description = "Virtual Network resource ID"
}

output "subnet_id" {
  value = module.network.subnet_id
  description = "Subnet resource ID"
} 