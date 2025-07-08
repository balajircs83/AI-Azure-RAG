variable "openai_account_name" {
  type = string
}

variable "location" {
  type = string
}

variable "resource_group_name" {
  type = string
}

variable "sku_name" {
  type    = string
  default = "S0"
}

variable "common_tags" {
  type = map(string)
}

variable "embedding_deployment_name" {
  description = "Name of the Azure OpenAI embedding deployment"
  type        = string
}

variable "chat_deployment_name" {
  description = "Name of the Azure OpenAI chat deployment"
  type        = string
} 