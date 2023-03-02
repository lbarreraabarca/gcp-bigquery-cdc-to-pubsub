

resource "google_cloud_run_service" "default" {
  name     = var.cloud_run_name
  location = var.gcp_region
  project = var.gcp_project_id
  metadata {
    annotations = {
      "run.googleapis.com/ingress" = "internal"
    }
  }
  template {
    spec {
      service_account_name = var.cloud_run_sa
      containers {
        image = var.cloud_run_docker_image
        env {
          name = "KAFKA_CONFIG"
          value = var.cloud_run_kafka_config
        }
        env {
          name = "randomtext"
          value = uuid() 
        }
        ports {
          container_port = 8080
        }
        resources {
          limits = {
            cpu = "2"
            memory = "1Gi"
          }
        }
      }
      timeout_seconds = 300
      container_concurrency = 1
    }
  }
}

data "google_iam_policy" "noauth" {
  binding {
    role = "roles/run.invoker"
    members = ["serviceAccount:${var.cloud_run_sa}"]
  }
}

resource "google_cloud_run_service_iam_policy" "noauth" {
  location    = google_cloud_run_service.default.location
  project     = google_cloud_run_service.default.project
  service     = google_cloud_run_service.default.name

  policy_data = data.google_iam_policy.noauth.policy_data
}