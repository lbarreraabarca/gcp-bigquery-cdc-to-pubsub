#!/usr/bin/env bash

echo  "Build image gcr.io/${GCP_PROJECT_ID}/${APPNAME}:latest"

gcloud builds submit --project ${GCP_PROJECT_ID} \
  --config cloudbuild.yaml \
  --substitutions=_GCP_PROJECT_ID="$GCP_PROJECT_ID",_APPNAME="$APPNAME",_LOG_BUCKET="$LOG_BUCKET",_CLOUD_RUN_NAME="$CLOUD_RUN_NAME"
