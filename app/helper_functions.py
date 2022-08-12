# get all available garments
def get_available_garments(garments):
    available_garments = []

    for garment in garments:
        if garment["is_available"]:
            available_garments.append(garment)

    return available_garments

# get garments in shopping bag
def get_unavailable_garments(garments):
    shopping_bag = []

    for garment in garments:
        if not garment["is_available"]:
            shopping_bag.append(garment)

    return shopping_bag