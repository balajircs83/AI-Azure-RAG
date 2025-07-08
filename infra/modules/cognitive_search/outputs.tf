output "search_service_id" {
  value = azurerm_search_service.this.id
}

output "search_service_name" {
  value = azurerm_search_service.this.name
}

output "cognitive_search_endpoint" {
  value = "https://${azurerm_search_service.this.name}.search.windows.net"
}

output "cognitive_search_key" {
  value = azurerm_search_service.this.primary_key
}

output "cognitive_search_index_name" {
  value = var.index_name
  description = "Name of the Cognitive Search index"
} 