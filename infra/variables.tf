variable "common_tags" {
  type = map(string)
  default = {
    "Owner Name"        = "Sandeep"
    "Owner Phone-Email" = "sandeepg@newtglobalcorp.com"
    "POC Name"          = "Sample PoC"
    "Approver"          = "Sandeep"
    "Valid till Date"   = "31-Mar-2025"
  }
  description = "Common tags applied to all resources."
}

variable "location" {
  type        = string 
  default     = "East US 2"
  description = "Azure region for all resources."
}

variable "project_name" {
  type        = string
  default     = "insurance-rag-poc"
  description = "Project name prefix for resource naming."
} 

variable "embedding_deployment_name" {
  description = "Name of the Azure OpenAI embedding deployment"
  type        = string
  default     = "text-embedding-ada-002"
}

variable "chat_deployment_name" {
  description = "Name of the Azure OpenAI chat deployment"
  type        = string
  default     = "gpt-35-turbo"
} 