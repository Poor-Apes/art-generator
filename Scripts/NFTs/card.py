from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps
from dotenv import load_dotenv
from random import randint
import datetime
import os

load_dotenv()

card_size = (566, 943)
background_colour = "#7e6254"
nft_scale = 0.235
assets_scale = 0.225

project_base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ipfs_path = os.path.join(project_base_path, "IPFS")
assets_path = os.path.join(project_base_path, "Assets")


def getAssetsFontPath(font_name):
    return os.path.join(assets_path, "Fonts", font_name + ".ttf")


def getAssetsCardPath(image_full_name):
    return os.path.join(assets_path, "Cards", "Front", image_full_name + ".png")


def getNFTWithPath(nft_number):
    return os.path.join(ipfs_path, "NFTs", "Genesis", str(nft_number) + ".png")


def getIPFSCardsGenesisPath():
    return os.path.join(ipfs_path, "Cards", "Genesis")


def getCardsPath(card_number):
    return os.path.join(ipfs_path, "Cards", "Genesis", str(card_number) + ".png")


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


def delete_old_genesis_cards():
    for file in os.scandir(getIPFSCardsGenesisPath()):
        if file.name.endswith(".png"):
            os.unlink(file.path)

def create_genesis_card(
    ape_number, location_number, clothes_number, head_number, eyes_number, mouth_number
):

    card = Image.new("RGB", card_size, color=background_colour)

    # NFT

    nft_image = Image.open(getNFTWithPath(ape_number))

    nft_image_scaled = ImageOps.scale(nft_image, nft_scale)

    card.paste(nft_image_scaled, (-80, 0))

    add_borders(card)

    # Registration Card

    registration_card = Image.open(getAssetsCardPath("registration_card"))

    drawable_image = ImageDraw.Draw(registration_card)

    # Create the details on the card
    card_details(
        drawable_image,
        ape_number,
        location_number,
        clothes_number,
        head_number,
        eyes_number,
        mouth_number,
    )

    create_drop_shadow(card, registration_card)

    reg_card_colour, reg_card_alpha = create_reg_card_colour_and_alpha(
        registration_card
    )

    card.paste(reg_card_colour, (0, 0), reg_card_alpha)

    cut_the_corners_off(card)

    card.save(getCardsPath(ape_number))


def add_borders(card):
    borders = Image.open(getAssetsCardPath("borders"))
    borders_scaled = ImageOps.scale(borders, assets_scale)

    borders_alpha = Image.open(getAssetsCardPath("borders_alpha"))
    borders_alpha_scaled = ImageOps.scale(borders_alpha, assets_scale)
    r, g, b, a = borders_alpha_scaled.split()
    borders_alpha_recombined = Image.merge("RGBA", (r, g, b, r))

    card.paste(borders_scaled, (0, 0), borders_alpha_recombined)


def card_details(
    drawable_image,
    ape_number,
    location_number,
    clothes_number,
    head_number,
    eyes_number,
    mouth_number,
):
    # NFT Number
    drawable_image.text(
        (240, 240),
        str(ape_number + 1).rjust(3, " "),
        fill=gravitas_one_colour,
        font=gravitas_one_100,
    )

    # Name
    drawable_image.text((670, 220), "Unknown", fill=rock_salt_colour, font=rock_salt_70)

    # Season
    drawable_image.text((170, 460), "GENESIS", fill=rock_salt_colour, font=rock_salt_60)

    # Age in Years
    age = randint(18, 50)
    drawable_image.text((970, 450), str(age), fill=rock_salt_colour, font=rock_salt_70)

    # Date of Birth
    start_date = datetime.date(1930, 4, 28)
    rand_days = randint(1, 355)
    full_age = datetime.timedelta((age * 365) + rand_days)
    dob = start_date - full_age
    drawable_image.text(
        (1500, 435),
        str(dob.day) + "/" + str(dob.month) + "/" + str(dob.year),
        fill=rock_salt_colour,
        font=rock_salt_70,
    )

    # FEATURERS

    # Local
    drawable_image.text(
        (120, 717),
        "LOCATION: " + os.getenv("BACKGROUND_" + str(location_number)),
        fill=typewriter_colour,
        font=typewriter_80,
    )

    # Clothes
    drawable_image.text(
        (135, 817),
        "CLOTHES: " + os.getenv("CLOTHES_" + str(clothes_number)),
        fill=typewriter_colour,
        font=typewriter_80,
    )

    # Head
    drawable_image.text(
        (120, 910),
        "HEAD: " + os.getenv("HEAD_" + str(head_number)),
        fill=typewriter_colour,
        font=typewriter_80,
    )

    # Eyes
    drawable_image.text(
        (1200, 710),
        "EYES: " + os.getenv("EYES_" + str(eyes_number)),
        fill=typewriter_colour,
        font=typewriter_80,
    )

    # Mouth
    drawable_image.text(
        (1180, 822),
        "MOUTH: " + os.getenv("MOUTH_" + str(mouth_number)),
        fill=typewriter_colour,
        font=typewriter_80,
    )


def create_drop_shadow(card, registration_card):
    # 1. Create a slate for the drop shadow
    blank_slate_drop_shadow = Image.new("RGB", card_size, color="black")
    # 2. Use the reg card commands
    drop_shadow = Image.new("RGBA", registration_card.size, (255,) * 4)
    drop_shadow_scale = ImageOps.scale(drop_shadow, assets_scale)
    drop_shadow_rotate = drop_shadow_scale.rotate(5, resample=3, expand=1)
    # 3. Paste the drop shadow into location
    blank_slate_drop_shadow.paste(drop_shadow_rotate, (15, 630))
    # 4. Do the shadow
    blank_slate_drop_shadow_blur = blank_slate_drop_shadow.filter(
        ImageFilter.GaussianBlur(15)
    )
    # 5. Set the alph to the colors
    r, g, b = blank_slate_drop_shadow_blur.split()
    blank_slate_drop_shadow_recombined = Image.merge("RGBA", (r, g, b, r))
    # 6. Paset it onto the card
    card.paste(blank_slate_drop_shadow, (0, 0), blank_slate_drop_shadow_recombined)


def create_reg_card_colour_and_alpha(registration_card):
    reg_card_scaled = ImageOps.scale(registration_card, assets_scale)
    reg_card_rotated = reg_card_scaled.rotate(
        5, resample=3, expand=1, fillcolor="#fdfbc0"
    )
    alpha = Image.new("RGBA", registration_card.size, (255,) * 4)
    alpha_scale = ImageOps.scale(alpha, assets_scale)
    alpha_rotate = alpha_scale.rotate(5, resample=3, expand=1)
    # 1. Create a blank slate the same size as the card
    blank_slate_colour = Image.new("RGB", card_size, color="black")
    blank_slate_alpha = Image.new("RGB", card_size, color="black")
    # 2. Paste and move the card on the blank slate
    blank_slate_colour.paste(reg_card_rotated, (15, 630))
    # 3. Paste and move the alpha box on the blank slate
    blank_slate_alpha.paste(alpha_rotate, (15, 630))
    # 4. smooth the alpha edges
    blank_slate_alpha_blur = blank_slate_alpha.filter(ImageFilter.BoxBlur(3)).filter(
        ImageFilter.UnsharpMask(radius=20, percent=500, threshold=12)
    )
    # 5. Move the alpha colour to the alpha channel
    r, g, b = blank_slate_alpha_blur.split()
    blank_slate_alpha_recombined = Image.merge("RGBA", (r, g, b, r))
    # 6. Alpha the reg card onto the card
    return blank_slate_colour, blank_slate_alpha_recombined


def cut_the_corners_off(card):
    corners_colour = Image.new("RGB", card_size, color="black")
    corners_alpha = Image.open(getAssetsCardPath("corners_alpha"))
    corners_alpha_scaled = ImageOps.scale(corners_alpha, assets_scale).resize(card_size)
    r, g, b, a = corners_alpha_scaled.split()
    corners_alpha_recombined = Image.merge("RGBA", (r, g, b, r))

    card.paste(corners_colour, (0, 0), corners_alpha_recombined)
