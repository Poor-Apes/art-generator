#!python3

import json
from math import floor
from random import shuffle, randrange, choice
from accessories_accommodation_attributes import *

max_nfts = 300
current_nft = 0

nft_json = []
nft_types = []

i = 0
for i in range(3):
    nft_types.append(4)
i = 0
for i in range(27):
    nft_types.append(3)
i = 0
for i in range(50):
    nft_types.append(2)
i = 0
for i in range(80):
    nft_types.append(1)
i = 0
for i in range(140):
    nft_types.append(0)

shuffle(nft_types)


def rand_attribute_number_for_type(random_type):
    return randrange(floor(random_type * (70 / 4)), floor((random_type + 1) * (70 / 4)))


while current_nft < max_nfts:
    nft_type_num = nft_types[current_nft]
    name = accessory_type[nft_type_num]
    description = accessories_decription[nft_type_num]
    current_nft_json = {}
    lower_bound = nft_type_num * 20
    upper_bound = (nft_type_num + 1) * 20
    current_nft_json["name"] = (
        "Poor Apes - Accessories (No. " + str(current_nft + 1) + ")"
    )
    current_nft_json["description"] = description
    current_nft_json["image"] = (
        "https://ipfs.io/ipfs/"
        + accessories_ipfs_folder
        + "/"
        + str(nft_type_num)
        + ".jpg"
    )

    current_nft_json["attributes"] = []
    current_nft_json["attributes"].append({"trait_type": "accessory", "value": name})
    current_nft_json["attributes"].append(
        {"trait_type": "level", "value": nft_type_num + 1}
    )
    current_nft_json["attributes"].append(
        {
            "trait_type": "Street Smarts",
            "value": rand_attribute_number_for_type(nft_type_num),
        }
    )
    current_nft_json["attributes"].append(
        {"trait_type": "OG", "value": rand_attribute_number_for_type(nft_type_num)}
    )
    current_nft_json["attributes"].append(
        {
            "trait_type": "Survival",
            "value": rand_attribute_number_for_type(nft_type_num),
        }
    )
    current_nft_json["attributes"].append(
        {"trait_type": "Backup", "value": rand_attribute_number_for_type(nft_type_num)}
    )
    current_nft_json["attributes"].append(
        {"trait_type": "Cunning", "value": rand_attribute_number_for_type(nft_type_num)}
    )
    current_nft_json["attributes"].append(
        {"trait_type": "Makes Apes ...", "value": choice(emotions)}
    )
    nft_json.append(current_nft_json)
    current_nft += 1

with open("../../IPFS/JSON/FREE_Mints/accessories.json", "w", encoding="utf-8") as f:
    json.dump(nft_json, f, ensure_ascii=False, indent=4)
