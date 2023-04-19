#!python

import os
import sys
import time
import json
import random
from PIL import Image
from dotenv import load_dotenv
from progress_bar import progressbar
from card_chicago import create_card as create_chicago_card
from card_chicago import delete_old_cards as delete_old_chicago_cards

load_dotenv()

ipfs_client = None

# Environment & Input checks

if os.getenv("VIRTUAL_ENV") == None:
    print(
        "This script needs to be run inside a virtual environment. Please read the README.md"
    )
    exit()

if len(sys.argv) != 2 and sys.argv[1] not in [
    "chicago",
    "new_york",
    "detroit",
]:
    print("Please use the argument 'chicago', 'new_york' or 'detroit' to generate NFTs")
    exit()

season = sys.argv[1]

current_wd = os.path.dirname(os.path.realpath(__file__))
images_path = os.path.join(current_wd, os.path.join("..", "..", "Assets", "Drawings"))
ipfs_folder_path = os.path.join(current_wd, os.path.join("..", "..", "IPFS"))
json_folder_path = os.path.join(ipfs_folder_path, os.path.join("JSON"))
base_ape = Image.open(os.path.join(images_path, "ape.png"))
categories = ["background", "clothes", "mouth", "eyes", "head"]
nfts_attributes = []
nfts_path = None
json_files_path = None
number_of_nfts = 0
chicago_nfts = 3
new_york_nfts = 1700
detroit_nfts = 2000
item_range = []
items = []
names = []
# for the Latin American name for the Detroit season
names_2 = []

if season == "chicago":
    number_of_nfts = chicago_nfts
    item_range = [x for x in range(0, 4)]
    for first_name in range(50):
        for last_name in range(50):
            names.append([first_name, last_name])
    random.shuffle(names)
elif season == "new_york":
    number_of_nfts = new_york_nfts
    item_range = [x for x in range(0, 7)]
    for first_name in range(50):
        for last_name in range(50):
            names.append([first_name, last_name])
    random.shuffle(names)
elif season == "detroit":
    number_of_nfts = detroit_nfts
    item_range = [x for x in range(4, 10)]
    # Western names
    for first_name in range(40):
        for last_name in range(40):
            names.append([first_name, last_name])
    random.shuffle(names)
    # Latin American names
    for first_name in range(20):
        for last_name in range(20):
            names_2.append([first_name, last_name])
    random.shuffle(names_2)
else:
    exit(str(season) + " is not a season!")

nfts_path = os.path.join(ipfs_folder_path, os.path.join("NFTs", season.title()))
json_files_path = os.path.join(json_folder_path, os.path.join(season.title()))

if (
    nfts_path == None
    or json_files_path == None
    or number_of_nfts == 0
    or len(item_range) == 0
):
    exit("Setup Failed!")

# Delete all the old files

for file in os.scandir(nfts_path):
    if file.name.endswith(".png"):
        os.unlink(file.path)

for file in os.scandir(json_files_path):
    if file.name.endswith(".json"):
        os.unlink(file.path)

if season == "chicago":
    delete_old_chicago_cards()

# Setup a file array so we can reference traits

for category in categories:
    items.append([])
    for category_num in range(0, 10):
        items[len(items) - 1].append(
            Image.open(
                images_path
                + "/"
                + category
                + "/"
                + category
                + "_"
                + str(category_num)
                + ".png"
            )
        )

# Create an arrary of all unique NFT traits

for bg in item_range:
    for cl in item_range:
        for m in item_range:
            for e in item_range:
                for h in item_range:
                    nfts_attributes.append([bg, cl, m, e, h])

random.shuffle(nfts_attributes)

# Only use the first bunch of NFTs

total_nfts = nfts_attributes[:number_of_nfts]

nft_number = 0
manifest = []

for current_nft in progressbar(total_nfts, "Generating NFTs: ", 40):
    # Create the NFTs
    nft_image = Image.new("RGBA", base_ape.size, (255, 255, 255, 255))
    traits = {}
    traits_score = 0
    for i in range(0, len(categories)):
        # background
        if i == 0:
            # start with the background
            nft_image.paste(items[0][current_nft[0]])
            # add the ape
            nft_image = Image.alpha_composite(nft_image, base_ape)
        else:
            # layer the traits
            nft_image = Image.alpha_composite(nft_image, items[i][current_nft[i]])
        traits[categories[i]] = current_nft[i]
        traits_score += current_nft[i]
    traits["score"] = 50 - traits_score
    image_path_and_filename = nfts_path + "/" + str(nft_number) + ".png"
    nft_image_resized = nft_image.resize((1024, 1024))
    nft_image_resized.save(image_path_and_filename)
    create_chicago_card(
        nft_image=nft_image,
        ape_number=nft_number,
        score_number=traits["score"],
        background_number=traits["background"],
        clothes_number=traits["clothes"],
        head_number=traits["head"],
        eyes_number=traits["eyes"],
        mouth_number=traits["mouth"],
    )
    manifest.append(traits)
    nft_number += 1

# Write the manifest
with open(os.path.join(json_folder_path, season + "_manifest") + ".json", "w") as file:
    json.dump(manifest, file, indent=4)

print("Finished!")
