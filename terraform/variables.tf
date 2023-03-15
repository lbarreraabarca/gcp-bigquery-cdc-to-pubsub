
variable "gcp_sa" {
    type = string
}

variable "gcp_project_id" {
    type = string
}

variable "gcp_region" {
  type = string
}

variable "bigquery_dataset_name" {
  type = string
}

variable "bigquery_table_name" {
    type = string
}

#variable "cloud_run_name" {
#  type = string
#}
#
#variable "cloud_run_docker_image" {
#  type = string
#}
#
#variable "cloud_run_sa" {
#  type = string
#}
#
#variable "cloud_run_kafka_config" {
#  type = string
#}