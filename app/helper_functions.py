import boto3

# get all available garments
def get_available_garments(garments):
    available_garments = []

    for garment in garments:
        if garment["is_available"]:
            available_garments.append(garment)

    return available_garments

# add garment image to aws s3 bucket
def upload_file(file_name, bucket):
    object_name = file_name
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)
    return response