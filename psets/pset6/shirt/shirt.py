from PIL import Image
from PIL import ImageOps
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not (sys.argv[1].casefold().endswith(".png") or sys.argv[1].casefold().endswith(".jpg") or sys.argv[1].casefold().endswith(".jpeg")):
    sys.exit("First argument must be an image file")
elif not (sys.argv[2].casefold().endswith(".png") or sys.argv[2].casefold().endswith(".jpg") or sys.argv[2].casefold().endswith(".jpeg")):
    sys.exit("Second argument must be an image file")
elif not (sys.argv[1].casefold().split(".")[1] == sys.argv[2].casefold().split(".")[1]):
    sys.exit("Extensions don't match")
try:
    shirt = Image.open("shirt.png")
    with Image.open(sys.argv[1]) as image:
        resized_image = ImageOps.fit(image, shirt.size)
        resized_image.paste(shirt, mask = shirt)
        resized_image.save(sys.argv[2])
except FileNotFoundError:
    sys.exit(f"Input does not exist")
