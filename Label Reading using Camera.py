try:
    from PIL import Image
except ImportError:
    import Image

import cv2
import time
import imutils

#C:\Users\MANI\AppData\Local\Tesseract-OCR\tesseract.exe

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\MANI\AppData\Local\Tesseract-OCR\tesseract.exe'

def recText(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text

#camera initializing
cam = cv2.VideoCapture(0)
time.sleep(1)
firstFrame = None
area = 500
cntdet = 0

while True:
    _, img = cam.read()
    cv2.imshow("cameraFeed", img)
    img = imutils.resize(img, width=450)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        cv2.imwrite('RDMobileText.jpg',img)
        break

info = recText('RDMobileText.jpg')
print(info)
file = open("result1.txt","w")
file.write(info)
file.close()
print("Written Successful")

cam.release()
cv2.destroyAllWindows()
