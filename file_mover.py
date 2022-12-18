import shutil, os
import keyboard as kb
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

DATADIR = r"D:\Media\prntsc\scrape"
DESTINATION_1 = r"D:\Media\prntsc\gems" #r
DESTINATION_2 = r"D:\Media\prntsc\categories\game" #q
DESTINATION_3 = r"D:\Media\prntsc\categories\text" #w
DESTINATION_4 = r"D:\Media\prntsc\categories\personal" #e

nl = "\\"
counter = 1
for file in os.scandir(DATADIR):
    if file.name.endswith(".png"):
        try:
            print(file.name)
            image = mpimg.imread(file.path)
            plt.title(f"{file.name} - {counter}")
            plt.imshow(image)
            plt.show(block=False)
            a = input()
            if a == "r":
                print(f"Moving To '/{DESTINATION_1.split(nl)[-1]}'")
                os.replace(file.path, DESTINATION_1 + "/" + file.name)
            elif a == "q":
                print(f"Moving To '/{DESTINATION_2.split(nl)[-1]}'")
                os.replace(file.path, DESTINATION_2 + "/" + file.name)
            elif a == "w":
                print(f"Moving To '/{DESTINATION_3.split(nl)[-1]}'")
                os.replace(file.path, DESTINATION_3 + "/" + file.name)
            elif a == "e":
                print(f"Moving To '/{DESTINATION_4.split(nl)[-1]}'")
                os.replace(file.path, DESTINATION_4 + "/" + file.name)
            elif a == "a":
                os.remove(file.path)
            plt.close()
        except SyntaxError as SynErr:
            print(f"{file.name} - {SynErr}")

    counter += 1