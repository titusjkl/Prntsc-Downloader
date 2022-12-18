import requests, random, cloudscraper, os, cv2
from bs4 import BeautifulSoup
from PIL import Image, ImageOps, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from tqdm import tqdm

images = r"D:\Media\Prntsc\Scrape\\"

for to_scan_path in tqdm(os.scandir(images), total = len([images.name for images in os.scandir(images)])):
    image = Image.open(to_scan_path.path)
    if image.mode != "RGB":
        if image.mode == "RGBA":
            print(image.mode)
        try:
            background = Image.new("RGB", image.size, (255, 255, 255))
            background.paste(image, mask = image.split()[3])

            background.save(to_scan_path.path, "png", quality=100)
            rgb_image = Image.open("sample_2.jpg")
        except Exception:
            pass

#     image.close()

#print(rgb_image.mode)