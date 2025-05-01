# שלב 1: ייבוא ספריות
import os
import cv2
import matplotlib.pyplot as plt
from zipfile import ZipFile
from urllib.request import urlretrieve

def download_and_unzip(url, save_path):
    print("Downloading and extracting assets... ", end="")
    urlretrieve(url, save_path)

    try:
        with ZipFile(save_path) as z:
            z.extractall(os.path.split(save_path)[0])
        print("Done extracting")
        print("Files inside zip:")
        print(z.namelist())
    except Exception as e:
        print("\nInvalid file.", e)

# שלב 3: הורדת הקובץ אם הוא לא קיים
URL = r"C:\Users\1\Downloads\MVI_4477.zip"
asset_zip_path = os.path.join(os.getcwd(), "opencv_bootcamp_assets_NB6.zip")

if not os.path.exists(asset_zip_path):
    download_and_unzip(URL, asset_zip_path)

# שלב 4: פתיחת הווידאו (הקובץ נחלץ לתיקייה הנוכחית)
source = "MVI_4477.MP4"
cap = cv2.VideoCapture(source)

# שלב 5: בדיקה שהווידאו נפתח
if not cap.isOpened():
    print("Error opening video stream or file")
else:
    cv2.namedWindow("Video Frame", cv2.WINDOW_NORMAL)  # אפשרות לשינוי גודל
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # קבלת גודל החלון הנוכחי
        _, _, win_w, win_h = cv2.getWindowImageRect("Video Frame")
        if win_w > 0 and win_h > 0:
            frame_resized = cv2.resize(frame, (win_w, win_h))
        else:
            frame_resized = frame

        cv2.imshow("Video Frame", frame_resized)

        if cv2.waitKey(25) & 0xFF == 27:
            break



# שחרור המשאבים
cap.release()
cv2.destroyAllWindows()
