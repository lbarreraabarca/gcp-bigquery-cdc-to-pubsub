## Container registry steps

export GCP_PROJECT_ID=<gcp_project_id>
export APPNAME=<app.name>
export LOG_BUCKET=<bucket_name>
export CLOUD_RUN_NAME=<cloud_run_name>

bash scripts/deploy-cloud-build.sh


## Terraform steps
export BUCKET_TERRAFORM_STATES=<terraform_states_bucket>
export BACKEND_PREFIX=<prefix_or_folder>


export TF_VAR_gcp_sa=${GOOGLE_APPLICATION_CREDENTIALS}
export TF_VAR_gcp_project_id=<gcp_project_id>
export TF_VAR_gcp_region=us-central1
export TF_VAR_bigquery_dataset_name=<dataset>
export TF_VAR_bigquery_table_name=<table_name>
export TF_VAR_cloud_run_name=${CLOUD_RUN_NAME}
export TF_VAR_cloud_run_docker_image=gcr.io/${TF_VAR_gcp_project_id}/${APPNAME}:latest
export TF_VAR_cloud_run_sa=<sa>
export TF_VAR_cloud_run_kafka_config=<encoded_kafka_config_as_json>


cd terraform

terraform init -backend-config="bucket=${BUCKET_TERRAFORM_STATES}" -backend-config="prefix=${BACKEND_PREFIX}"
terraform plan
terraform apply -auto-approve
##terraform destroy -auto-approve