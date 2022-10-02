#!python

import os
import sys
import json
import time
import random
from PIL import Image
from dotenv import load_dotenv
from progress_bar import progressbar

load_dotenv()

ipfs_client = None

# Environment & Input checks

if os.getenv('VIRTUAL_ENV') == None:
    print("This script needs to be run inside a virtual environment. Please read the README.md")
    exit()

if len(sys.argv) == 1 or len(sys.argv) > 2 and sys.argv[1] not in ["genesis", "second_season", "third_season"]:
    print("Please use the argument 'genesis', 'second_season' or 'third_season' to generate NFTs")
    exit()

season = sys.argv[1]

current_wd = os.path.dirname(os.path.realpath(__file__))
images_path = os.path.join(current_wd, os.path.join("..", "..", "Drawings"))
ipfs_folder_path = os.path.join(current_wd, os.path.join("..", "..", "IPFS"))
json_folder_path = os.path.join(ipfs_folder_path, os.path.join("JSON"))
bkground = Image.open(os.path.join(images_path, "test_card.png"))
categories = ['head', 'eyes', 'mouth', 'clothes', 'background']
nfts_attributes = []
nfts_path = None
json_files_path = None
number_of_nfts = 0
item_range = []
items = []

if season == "genesis":
    number_of_nfts = 3
    item_range = [x for x in range(0,4)]
    nfts_path = os.path.join(ipfs_folder_path, os.path.join("NFTs", "Genesis"))
    json_files_path = os.path.join(json_folder_path, os.path.join("Genesis"))
elif season == "second_season":
    number_of_nfts = 2000
    item_range = [x for x in range(0,7)]
    nfts_path = os.path.join(ipfs_folder_path, os.path.join("NFTs", "2nd_Season"))
    json_files_path = os.path.join(json_folder_path, os.path.join("2nd_Season"))
elif season == "third_season":
    number_of_nfts = 3000
    item_range = [x for x in range(4,10)]
    nfts_path = os.path.join(ipfs_folder_path, os.path.join("NFTs", "3rd_Season"))
    json_files_path = os.path.join(json_folder_path, os.path.join("3rd_season"))
else:
    exit(str(season) + " is not a season!")

if nfts_path == None or json_files_path == None or number_of_nfts == 0 or len(item_range) == 0:
    exit("Setup Failed!")

# Delete all the old files

for file in os.scandir(nfts_path):
    if file.name.endswith(".png"):
        os.unlink(file.path)

for file in os.scandir(json_files_path):
    if file.name.endswith(".json"):
        os.unlink(file.path)

# Setup a file array so we can reference traits

for category in categories:
    items.append([])
    for category_num in range(0,10):
        items[len(items)-1].append(Image.open(images_path + "/" + category + "/" + category + "_" +str(category_num) + ".png"))
'''
items.append([])
for bg_num in range(0,10):
    items[len(items)-1].append(Image.open(images_path + "/background/bg_" + str(bg_num) + ".png"))
'''

# Create an arrary of all unique NFT traits

for x in item_range:
    for y in item_range:
        for z in item_range:
            for s in item_range:
                for t in item_range:
                    for bg in item_range:
                        nfts_attributes.append([x,y,z,s,t,bg])

random.shuffle(nfts_attributes)

# Only use the first bunch of NFTs

total_nfts = nfts_attributes[:number_of_nfts]

nft_number = 0
manifest = []

for current_nft in progressbar(total_nfts, "Generating NFTs: ", 40):
    # Create the NFTs
    nft_image = Image.new('RGBA',(bkground.size[0], bkground.size[1]), (255,255,255))
    nft_image = Image.alpha_composite(nft_image, bkground)
    traits = {}
    for i in range(0,len(categories)):
        nft_image = Image.alpha_composite(nft_image, items[i][current_nft[i]])
        #traits[categories[i]] = os.getenv(categories[i].upper() + "_" + str(i))
        traits[categories[i]] = current_nft[i]
    image_path_and_filename = nfts_path + "/" + str(nft_number) + ".png"
    nft_image.save(image_path_and_filename)
    # Create NFTs traits list for manifest
    manifest.append(traits)
    nft_number += 1

# Write the manifest
with open(os.path.join(json_folder_path, season + "_manifest") + ".json", "w") as file:
    json.dump(manifest, file)

print("Finished!")
