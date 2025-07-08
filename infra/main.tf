terraform {
  required_version = ">= 1.3.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 3.0.0"
    }
  }
}

provider "azurerm" {
  features {}
  subscription_id = "b83326f1-b625-4cbc-b5c3-c2f240c6665d"
}

# Modules will be instantiated here 

module "resource_group" {
  source       = "./modules/resource_group"
  name         = "insurance-rag-rg3"
  location     = var.location
  common_tags  = var.common_tags
}

module "network" {
  source                  = "./modules/network"
  vnet_name               = "insurance-rag-vnet"
  address_space           = ["10.0.0.0/16"]
  location                = var.location
  resource_group_name     = module.resource_group.name
  subnet_name             = "default"
  subnet_address_prefixes = ["10.0.1.0/24"]
  common_tags             = var.common_tags
}

module "storage" {
  source                = "./modules/storage"
  storage_account_name  = "insuranceragstoruniq3"
  resource_group_name   = module.resource_group.name
  location              = var.location
  container_name        = "docs"
  common_tags           = var.common_tags
}

module "function_app" {
  source                = "./modules/function_app"
  app_service_plan_name = "insurance-rag-plan3"
  function_app_name     = "insurance-rag-func3"
  storage_account_name  = module.storage.storage_account_name
  resource_group_name   = module.resource_group.name
  location              = var.location
  common_tags           = var.common_tags
  depends_on            = [module.storage]
}

module "aml_workspace" {
  source                = "./modules/aml_workspace"
  workspace_name        = "insurance-rag-aml3"
  app_insights_name     = "insurance-rag-ai3"
  key_vault_name        = "insurance-rag-kv-unique"
  storage_account_name  = "insuranceragamlstoruniq3"
  location              = var.location
  resource_group_name   = module.resource_group.name
  tenant_id             = "221e7052-4196-456d-a2fa-a567271e2d0b"
  common_tags           = var.common_tags
}

module "cognitive_search" {
  source                = "./modules/cognitive_search"
  search_service_name   = "insuranceragsearch3"
  resource_group_name   = module.resource_group.name
  location              = var.location
  sku                   = "basic"
  index_name            = "insurance-rag-index"
  common_tags           = var.common_tags
}

module "openai" {
  source                = "./modules/openai"
  openai_account_name   = "insuranceragopenai3"
  location              = var.location
  resource_group_name   = module.resource_group.name
  sku_name              = "S0"
  common_tags           = var.common_tags
  embedding_deployment_name = var.embedding_deployment_name
  chat_deployment_name      = var.chat_deployment_name
}

module "aad" {
  source                = "./modules/aad"
  app_name              = "insurance-rag-app3"
}

# Commented out - using the Key Vault created by AML workspace instead
# module "key_vault" {
#   source                = "./modules/key_vault"
#   key_vault_name        = "insurance-rag-kv-unique3"
#   location              = var.location
#   resource_group_name   = module.resource_group.name
#   tenant_id             = "221e7052-4196-456d-a2fa-a567271e2d0b"
#   common_tags           = var.common_tags
# }

module "monitor" {
  source                = "./modules/monitor"
  log_analytics_name    = "insurance-rag-logs"
  location              = var.location
  resource_group_name   = module.resource_group.name
  common_tags           = var.common_tags
}

module "managed_identity" {
  source                = "./modules/managed_identity"
  identity_name         = "insurance-rag-mi3"
  location              = var.location
  resource_group_name   = module.resource_group.name
  common_tags           = var.common_tags
} 