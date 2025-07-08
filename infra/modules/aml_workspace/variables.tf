variable "workspace_name" {
  type = string
}

variable "app_insights_name" {
  type = string
}

variable "key_vault_name" {
  type = string
}

variable "storage_account_name" {
  type = string
}

variable "location" {
  type = string
}

variable "resource_group_name" {
  type = string
}

variable "tenant_id" {
  type = string
}

variable "common_tags" {
  type = map(string)
} 