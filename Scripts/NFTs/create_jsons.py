import os
import sys
import json
import argparse
from dotenv import load_dotenv
from progress_bar import progressbar

load_dotenv()

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--season", required=True, help = "The season (genesis, second, third)")
parser.add_argument("-n", "--nft-folder-hash", required=True, dest="nft_folder_hash", help = "The hash of the NFT folder on IPFS")
parser.add_argument("-c", "--card-folder-hash", required=True, dest="card_folder_hash", help = "The hash of the card folder on IPFS")
parser.add_argument("-cf", "--card-file-hash", required=True, dest="card_file_hash", help = "The hash of the card viewer HTML file on IPFS")

args = parser.parse_args()

if len(args.nft_folder_hash) != 46:
    raise SyntaxError("NFT folder hash should be 46 characters long")

if len(args.card_file_hash) != 46:
    raise SyntaxError("Card file hash should be 46 characters long")

if len(args.card_folder_hash) != 46:
    raise SyntaxError("Card folder hash should be 46 characters long")


name = "Poor Apes"
description = "The first PBM (Proof of Bear Market) apes"
external_url = "https://card.poor-apes.com/"

ipfs_url = "https://ipfs.io/ipfs/"

genesis_background_colours = ["966a64", "7e6254", "616b63", "89815a"]


current_wd = os.path.dirname(os.path.realpath(__file__))
ipfs_folder_path = os.path.join(current_wd, os.path.join("..", "..", "IPFS"))
json_folder_path = os.path.join(ipfs_folder_path, os.path.join("JSON"))

current_file_number = 0

with open(os.path.join(json_folder_path, args.season + "_manifest") + ".json", "r") as file:
    manifest = json.load(file)
    for current_json in progressbar(manifest, "Generating JSON files: ", 40):
        data = {}
        data['name'] = name
        data["description"] = description
        data["image"] = ipfs_url + args.nft_folder_hash + "/" + str(current_file_number) + ".png"
        data["external_url"] = ipfs_url + args.card_file_hash + "/?number=" + str(current_file_number)
        data["background_color"] = genesis_background_colours[current_json["background"]]
        data["attributes"] = {
            "card": ipfs_url + args.card_folder_hash + "/" + str(current_file_number) + ".png",
            "background": os.getenv("BACKGROUND_"+str(current_json["background"])),
            "clothes": os.getenv("CLOTHES_"+str(current_json["clothes"])),
            "head": os.getenv("HEAD_"+str(current_json["head"])),
            "eyes": os.getenv("EYES_"+str(current_json["eyes"])),
            "mouth": os.getenv("MOUTH_"+str(current_json["mouth"])),
        }
        with open(os.path.join(json_folder_path, args.season.title(), str(current_file_number)), "w") as current_json_file:
            json.dump(data, current_json_file, indent=4)
        current_file_number += 1
