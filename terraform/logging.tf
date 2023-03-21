
resource "google_logging_project_sink" "log_sink_cdc" {
  name = format("log_sink_cdc_%s_%s", var.bigquery_dataset_name, var.bigquery_table_name)
  project = var.gcp_project_id
  destination = format("pubsub.googleapis.com/projects/%s/topics/%s", var.gcp_project_id, google_pubsub_topic.topic_cdc.name)
  filter = format("protoPayload.methodName=google.cloud.bigquery.v2.JobService.InsertJob AND protoPayload.resourceName = projects/%s/datasets/%s/tables/%s", var.gcp_project_id, var.bigquery_dataset_name, var.bigquery_table_name)
  unique_writer_identity = true
}

resource "google_project_iam_binding" "log-writer" {
  project = var.gcp_project_id
  role = "roles/pubsub.editor"

  members = [
    google_logging_project_sink.log_sink_cdc.writer_identity,
  ]
}