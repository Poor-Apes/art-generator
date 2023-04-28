import os
from math import floor
from PIL import Image, ImageFont

card_size = (566, 943)
# card_size = (900, 1500)

background_colours = [
    "966a64",
    "7e6254",
    "616b63",
    "89815a",
    "434752",
    "955e5e",
    "706c7d",
    "7c6e4b",
    "987d8b",
    "7b7d8a",
]
background_colours_border = [
    "cabab9",
    "c1b8b5",
    "b8bbb8",
    "c5c2b6",
    "b1b2b4",
    "c9b7b7",
    "bcbbc0",
    "c0bcb3",
    "cac0c5",
    "c0c0c5",
]

# nft_scale = 0.235
# assets_scale = 0.225
nft_scale = 1.30879515898461
asset_scale = 1.36696383271726
border_scale = 0.999311185291157


def get_nft_scale(nft_image: Image):
    nft_height = nft_image.size[1]
    card_height = card_size[1]
    return (card_height / nft_height) / nft_scale


def get_asset_scale(asset_image: Image):
    asset_height = asset_image.size[1]
    card_height = card_size[1]
    return (card_height / asset_height) / asset_scale


def get_border_scale(border_image: Image):
    border_height = border_image.size[1]
    card_height = card_size[1]
    return (card_height / border_height) / border_scale


project_base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ipfs_path = os.path.join(project_base_path, "IPFS")
assets_path = os.path.join(project_base_path, "Assets")


def getAssetsFontPath(font_name):
    return os.path.join(assets_path, "Fonts", font_name + ".ttf")


# Assets


def getAssetsCardPath():
    return os.path.join(assets_path, "Cards")


def getAssetsCardRootPath(direction, image_name):
    return os.path.join(getAssetsCardPath(), direction, image_name + ".png")


def getAssetsCardFrontPath(image_name):
    return getAssetsCardRootPath("Front", image_name)


def getAssetsCardBackPath(image_name):
    return getAssetsCardRootPath("Back", image_name)


# IPFS


def getIPFSCardsPath(season, direction):
    return os.path.join(ipfs_path, "Cards", season.title(), direction)


def getIPFSCardsFrontPath(season):
    return getIPFSCardsPath(season, "Front")


def getIPFSCardsBackPath(season):
    return getIPFSCardsPath(season, "Back")


# Card Path (Save)


def getCardsPath(season, direction, card_number):
    return os.path.join(
        ipfs_path, "Cards", season.title(), direction, str(card_number) + ".png"
    )


def getCardsFrontPath(season, card_number):
    return getCardsPath(season, "Front", card_number)


def getCardsBackPath(season, card_number):
    return getCardsPath(season, "Back", card_number)


def percentageOfCardWidth(percent_var):
    return floor(card_size[0] * (percent_var / 100))


def percentageOfCardHeight(percent_var):
    return floor(card_size[1] * (percent_var / 100))


gravitas_one = getAssetsFontPath("GravitasOne-Regular")
rock_salt = getAssetsFontPath("RockSalt-Regular")
typewriter = getAssetsFontPath("zai_OlivettiLettera22Typewriter")
goldman = getAssetsFontPath("Goldman-Bold")

gravitas_one_colour = (147, 0, 0)
rock_salt_colour = (0, 0, 100)
typewriter_colour = (0, 0, 0)

gravitas_one_100 = ImageFont.truetype(font=gravitas_one, size=100)
rock_salt_60 = ImageFont.truetype(font=rock_salt, size=60)
# rock_salt_60.set_variation_by_name("Bold")
rock_salt_70 = ImageFont.truetype(font=rock_salt, size=70)
typewriter_80 = ImageFont.truetype(font=typewriter, size=80)
typewriter_200 = ImageFont.truetype(font=typewriter, size=200)
goldman_font = ImageFont.truetype(font=goldman, size=120)
