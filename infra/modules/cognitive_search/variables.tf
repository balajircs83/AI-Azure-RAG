variable "search_service_name" {
  type = string
}

variable "resource_group_name" {
  type = string
}

variable "location" {
  type = string
}

variable "sku" {
  type    = string
  default = "basic"
}

variable "common_tags" {
  type = map(string)
}

variable "index_name" {
  type        = string
  default     = "insurance-rag-index"
  description = "Name of the Cognitive Search index for RAG documents"
} 