import cv2, os

imgur_deleted = cv2.imread(r"D:/Dokumente/Seafile/Seafile/Programming/_work/python_/SmallProjects/prntsc/images/imgur_deleted.png")
prntsc_deleted = cv2.imread(r"D:/Dokumente/Seafile/Seafile/Programming/_work/python_/SmallProjects/prntsc/images/prntsc_deleted.png")

def delete_removed(to_scan):
    if imgur_deleted.shape == to_scan.shape or prntsc_deleted.shape == to_scan.shape:
        try:
            difference = cv2.subtract(imgur_deleted, to_scan)
        except cv2.error:
            difference = cv2.subtract(prntsc_deleted, to_scan)

        b, g, r = cv2.split(difference)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            return True

i = 0
j = 0
for to_scan_path in os.scandir(r"D:\Media\Prntsc_Scrape"):
    print(to_scan_path.path)

    to_scan = cv2.imread(to_scan_path.path)
    try:
        if delete_removed(to_scan) == True:
            os.remove(to_scan_path)
            print("Image Deleted.")
            j += 1

    except AttributeError:
        continue
    i += 1

print(f"Scanned: {i} - Deleted: {j} - {round((j/i*100),3)}%")
