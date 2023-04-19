import os
from PIL import ImageFont

card_size = (566, 943)
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
nft_scale = 0.235
assets_scale = 0.225

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


gravitas_one = getAssetsFontPath("GravitasOne-Regular")
rock_salt = getAssetsFontPath("RockSalt-Regular")
typewriter = getAssetsFontPath("zai_OlivettiLettera22Typewriter")

gravitas_one_colour = (147, 0, 0)
rock_salt_colour = (0, 0, 100)
typewriter_colour = (0, 0, 0)

gravitas_one_100 = ImageFont.truetype(font=gravitas_one, size=100)
rock_salt_60 = ImageFont.truetype(font=rock_salt, size=60)
# rock_salt_60.set_variation_by_name("Bold")
rock_salt_70 = ImageFont.truetype(font=rock_salt, size=70)
typewriter_80 = ImageFont.truetype(font=typewriter, size=80)
typewriter_200 = ImageFont.truetype(font=typewriter, size=200)
