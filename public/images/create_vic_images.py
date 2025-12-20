"""
deps: pillow
this script creates the top, bottom, left and right variants of the victim images from the victim image itself

Eg.:
python create_vic_images.py h H_nobg.png
will create h_bottom.png, h_top.png, h_left.png and h_right.png images.
"""

import sys
from PIL import Image

base_name = sys.argv[1] 

orig_fp = sys.argv[2] 
letter = Image.open(orig_fp)
letter = letter.resize((50, 50))

for name, pos in {
        "left":   (0,   50),
        "right":  (100, 50),
        "top":    (50,   0),
        "bottom": (50, 100),
    }.items():

    img = Image.new("RGBA", (150, 150), (255, 255, 255, 0))
    img.paste(letter, pos)
    img.save(f"{base_name}_{name}.png")



