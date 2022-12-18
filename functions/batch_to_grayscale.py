from PIL import Image, ImageOps
import os

def img_to_gray(open_path, save_path):
    i = 0
    j = 0
    print("Starting")
    converted_images = [images.name for images in os.scandir(save_path)]
    for to_convert_img in os.scandir(open_path):
        if to_convert_img.name not in converted_images:
            img_gray = ImageOps.grayscale(Image.open(to_convert_img.path))
            img_gray.save(save_path+"g_"+to_convert_img.name)
            j += 1
        i += 1
    print(f"{i} Images Scanned - {j} Images Converted")

open_path = r"D:\Media\Prntsc\Scrape\\"
save_path = r"D:\Media\Prntsc\Gray\\"

img_to_gray(open_path, save_path)
