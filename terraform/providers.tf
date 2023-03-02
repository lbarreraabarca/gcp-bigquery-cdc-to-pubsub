provider "google" {
  project     = var.gcp_project_id
  credentials = file(var.gcp_sa)
}
provider "google-beta" {
  project     = var.gcp_project_id
  credentials = file(var.gcp_sa)
}
