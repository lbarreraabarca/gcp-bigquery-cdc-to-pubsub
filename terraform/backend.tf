terraform {
  required_version = ">= 0.12"
  backend "gcs" {
    bucket = "bucket"
    prefix = "prefix/state"
  }
}
