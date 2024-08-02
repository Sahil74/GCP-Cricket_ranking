from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "local-tempo-430304-t9"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"
                     
    template_body = {
        "jobName": "bq-load",  # Provide a unique name for the job
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://dataflow-metadata1/udf.js",
        "JSONPath": "gs://dataflow-metadata1/bq.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "local-tempo-430304-t9.cricket_dataset.icc_odi_batsman_ranking",
        "inputFilePattern": "gs://bkt-iccranking-data/batsmen_ranking.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://dataflow-metadata1",
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)

