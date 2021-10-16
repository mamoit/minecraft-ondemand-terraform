import json
import boto3

def lambda_handler(event, context):

  ecs = boto3.client('ecs', region_name='${aws_region}')
  response = ecs.describe_services(
    cluster='${cluster_name}',
    services=[
      'minecraft-server',
    ]
  )

  desired = response["services"][0]["desiredCount"]

  if desired == 0:
    ecs.update_service(
      cluster='${cluster_name}',
      service='minecraft-server',
      desiredCount=1
    )
    print("Updated desiredCount to 1")
  else:
    print("desiredCount already at 1")
