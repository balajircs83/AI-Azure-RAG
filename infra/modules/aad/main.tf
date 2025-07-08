resource "azuread_application" "this" {
  display_name = var.app_name
}

resource "azuread_service_principal" "this" {
  client_id = azuread_application.this.client_id
} 