import requests, random, cloudscraper, os, cv2
from bs4 import BeautifulSoup
from PIL import Image, ImageOps, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from tqdm import tqdm

path_dl_imgs = r"D:\Media\Prntsc\Scrape\\d9ln0d.png"
image = Image.open(path_dl_imgs)
print(image.mode)
