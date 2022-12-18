import requests, random, cloudscraper, os, cv2
from bs4 import BeautifulSoup
from PIL import Image, ImageOps, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
from tqdm import tqdm

scraper = cloudscraper.create_scraper(
    browser={
        'browser': 'firefox',
        'platform': 'windows',
        'mobile': False
    }
)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

def generate_link():
    prnt_url = ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for i in range(6))
    while prnt_url[0] == "0":
        prnt_url = ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for i in range(6))

    return prnt_url

def get_img_url(prnt_url):
    html = scraper.get(f"https://prnt.sc/{prnt_url}", headers=headers).text
    soup = BeautifulSoup(html, 'lxml')
    img_url = soup.find_all('img', {'class': 'no-click screenshot-image'})

    return img_url[0]['src']

def get_img(no_of_imgs, path_dl_imgs):
    print(f"Starting Downmload Of {no_of_imgs} Image(s)..")
    for _ in tqdm(range(no_of_imgs)):
        filename = generate_link()
        img_url = get_img_url(filename)
        img_path_2_file = f"{path_dl_imgs}{filename}.png"

        try:
            response = scraper.get(img_url, headers= headers)
        except requests.exceptions.MissingSchema:
            img_url = "http:" + img_url 
            response = scraper.get(img_url, headers= headers)

        if response.status_code == 200:
            with open(img_path_2_file, 'wb') as f:
                f.write(response.content)

            image = Image.open(img_path_2_file)
            if image.mode != "RGB":
                try:
                    background = Image.new("RGB", image.size, (255, 255, 255))
                    background.paste(image, mask = image.split()[3])

                    background.save(img_path_2_file, "png", quality=100)
                    image = Image.open(img_path_2_file)
                except Exception as e:
                    # print(f"\n{e}")
                    pass
                image.close()

def get_imgs_removed(to_scan, PATH_IMGUR, PATH_PRNTSC):
    imgur_deleted = cv2.imread(PATH_IMGUR)
    prntsc_deleted = cv2.imread(PATH_PRNTSC)

    if imgur_deleted.shape == to_scan.shape or prntsc_deleted.shape == to_scan.shape:
        try:
            difference = cv2.subtract(imgur_deleted, to_scan)
        except cv2.error:
            difference = cv2.subtract(prntsc_deleted, to_scan)

        b, g, r = cv2.split(difference)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            return True

def delete_removed(path_dl_imgs, PATH_IMGUR, PATH_PRNTSC):
    print("Starting To Delete 'Image Was Removed' Images")
    scanned = 0
    deleted = 0
    for img_2_scan in tqdm(os.scandir(path_dl_imgs), total = len([images.name for images in os.scandir(path_dl_imgs)])):
        img = cv2.imread(img_2_scan.path)
        try:
            if get_imgs_removed(img, PATH_IMGUR, PATH_PRNTSC) == True:
                os.remove(img_2_scan.path)
                deleted += 1
        except AttributeError as AttErr:
            print(img_2_scan.name + str(AttErr))
            os.remove(img_2_scan.path)
            pass
        scanned += 1
    print(f"Scanned: {scanned} - Deleted: {deleted}")

def img_to_gray(open_path, save_path):
    i = 0
    j = 0
    print("Starting Conversion To Grayscale..")
    to_convert_imgs = [images.name for images in os.scandir(open_path)]
    converted_imgs = [images.name for images in os.scandir(save_path)]
    for to_convert_img in tqdm(os.scandir(open_path), total = len(to_convert_imgs)):
        if "g_"+to_convert_img.name not in converted_imgs:
            img_gray = ImageOps.grayscale(Image.open(to_convert_img.path))
            img_gray.save(save_path+"g_"+to_convert_img.name)
            j += 1
        i += 1
    print(f"{i} Images Scanned - {j} Image(s) Converted")

PATH_IMGUR = r"D:\Dokumente\Seafile\Seafile\Programming\_work\python_\prntsc\images\imgur_deleted.png"
PATH_PRNTSC = r"D:\Dokumente\Seafile\Seafile\Programming\_work\python_\prntsc\images\prntsc_deleted.png"

DL_PATH = r"D:\Media\prntsc\scrape\\"
# GRAY_PATH = r"D:\Media\prntsc\gray\\"

to_fetch = 1

# get_img(to_fetch, DL_PATH)
# delete_removed(DL_PATH, PATH_IMGUR, PATH_PRNTSC)
# img_to_gray(DL_PATH, GRAY_PATH)
