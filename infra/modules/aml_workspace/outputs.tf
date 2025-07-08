output "workspace_id" {
  value = azurerm_machine_learning_workspace.this.id
}

output "workspace_name" {
  value = azurerm_machine_learning_workspace.this.name
}

output "aml_workspace_name" {
  value = azurerm_machine_learning_workspace.this.name
}

output "key_vault_id" {
  value = azurerm_key_vault.this.id
  description = "Azure Key Vault resource ID"
}

output "key_vault_name" {
  value = azurerm_key_vault.this.name
  description = "Azure Key Vault name"
}

output "key_vault_uri" {
  value = azurerm_key_vault.this.vault_uri
  description = "Azure Key Vault URI"
} 