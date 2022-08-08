import boto3

# get all available garments
def get_available_garments(garments):
    available_garments = []

    for garment in garments:
        if garment["is_available"]:
            available_garments.append(garment)

    return available_garments