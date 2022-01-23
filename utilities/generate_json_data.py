from math import floor
from time import time
from json import dumps

background_values = ["orange_is_the_new_black", "green", "marroncino"]
body_values = ["basic"]
mouth_values = ["angry", "surprised"]
hat_values = ["detective", "red_hat"]
eyes_values = ["triple", "geek"]


def generate_json_data(new_image_id: int, combination: dict) -> None:
    dictionary = {
        "name": "CryptoCactus#" + str(new_image_id),
        "description": "Crypto Cactus number #" + str(new_image_id),
        "image": "ipfs://Qmb7skA43kEUQwVTaAepNmU9sk4rpHQn4feB4M5ibpdYZx/2650.png",  # not sure if needed
        "dna": "5b882fd9b472c8696ca514e34a91b32e36ff48f4",  # not sure if needed
        "edition": 1,
        "date": floor(time()),
        "attributes": [
            {"trait_type": "BACKGROUND", "value": background_values[combination['background_id']]},
            {"trait_type": "BODY", "value": body_values[combination['body_id']]},
            {"trait_type": "MOUTH", "value": mouth_values[combination['mouth_id']]},
            {"trait_type": "HAT", "value": hat_values[combination['hat_id']]},
            {"trait_type": "EYES", "value": eyes_values[combination['eyes_id']]},
        ],
        "compiler": "HashLips Art Engine"  # not sure if needed
    }

    json_data = dumps(obj=dictionary, indent=4)
    file = open(file="generated_nft_set/json/" + str(new_image_id) + ".json", mode="w")
    file.write(json_data)
