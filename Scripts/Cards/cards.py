from PIL import Image, ImageDraw, ImageFont
import os

def getFontWithPath(font_name):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "../Fonts/" + font_name + ".ttf"))

def getImageWithPath(image_full_name):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "../Cards/" + image_full_name))

gravitas_one = getFontWithPath("GravitasOne-Regular")
rock_salt = getFontWithPath("RockSalt-Regular")
typewriter = getFontWithPath("zai_OlivettiLettera22Typewriter")

gravitas_one_colour = (147, 0, 0)
rock_salt_colour = (0,0,100)
typewriter_colour = (0,0,0)

gravitas_one_100 = ImageFont.truetype(font=gravitas_one, size=100)
rock_salt_60 = ImageFont.truetype(font=rock_salt, size=60)
#rock_salt_60.set_variation_by_name("Bold")
rock_salt_70 = ImageFont.truetype(font=rock_salt, size=70)
typewriter_80 = ImageFont.truetype(font=typewriter, size=80)

registration_card = Image.open(getImageWithPath("registration_card.png"))

drawable_image = ImageDraw.Draw(registration_card)

# NFT Number
drawable_image.text((160, 240), "105", fill=gravitas_one_colour,font=gravitas_one_100)

# Name
drawable_image.text((670, 220), "Unknown", fill=rock_salt_colour,font=rock_salt_70)

# Season
drawable_image.text((170, 460), "GENESIS", fill=rock_salt_colour,font=rock_salt_60)

# Age in Years
drawable_image.text((970, 450), "46", fill=rock_salt_colour,font=rock_salt_70)

# Date of Birth
drawable_image.text((1500, 435), "12/10/1932", fill=rock_salt_colour,font=rock_salt_70)

# FEATURERS

# Location
drawable_image.text((120, 717), "LOCATION: Shops", fill=typewriter_colour,font=typewriter_80)

# Clothes
drawable_image.text((135, 817), "CLOTHES: Dungarees", fill=typewriter_colour,font=typewriter_80)

# Head
drawable_image.text((120, 910), "HEAD: Flat Cap", fill=typewriter_colour,font=typewriter_80)

# Eyes
drawable_image.text((1200, 710), "EYES: Yellow Glasses", fill=typewriter_colour,font=typewriter_80)

# Mouth
drawable_image.text((1180, 822), "MOUTH: Cigarette", fill=typewriter_colour,font=typewriter_80)

# Neck
drawable_image.text((1200, 923), "NECK: Burn Mark", fill=typewriter_colour,font=typewriter_80)

registration_card.show()
registration_card.save(getImageWithPath("result.png"))
