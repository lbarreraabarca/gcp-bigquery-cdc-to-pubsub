resource "google_pubsub_topic" "topic_cdc" {
  name    = format("topic_cdc_%s_%s", var.bigquery_dataset_name, var.bigquery_table_name)
  project = var.gcp_project_id
}

resource "google_pubsub_subscription" "log_sink_subs_pull" {
  name    = format("subs_pull_cdc_%s_%s", var.bigquery_dataset_name, var.bigquery_table_name)
  topic   = google_pubsub_topic.topic_cdc.name
  project = var.gcp_project_id
  retry_policy {
    minimum_backoff = "600s"
  }
  ack_deadline_seconds = 600
  retain_acked_messages      = true
}

resource "google_pubsub_subscription" "log_sink_subs_push" {
  name    = format("subs_push_cdc_%s_%s", var.bigquery_dataset_name, var.bigquery_table_name)
  topic   = google_pubsub_topic.topic_cdc.name
  project = var.gcp_project_id
  retry_policy {
    minimum_backoff = "600s"
  }
  ack_deadline_seconds = 600
  retain_acked_messages      = true
  push_config {
    push_endpoint = "${google_cloud_run_service.default.status[0].url}/api/v1/insert"
    attributes = {
      x-goog-version = "v1"
    }
    oidc_token {
      service_account_email = var.cloud_run_sa
    }
  }
}

