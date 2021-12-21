import pytesseract
import cv2
import telebot

# img = Image.open('foto.png')
pytesseract.pytesseract.tesseract_cmd = r'D:\\Program Files (x86)\\teseract\\tesseract.exe'

img = cv2.imread('red.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

configf = r'--oem 3 psm 6'
text = pytesseract.image_to_string(img, config = configf )
print(text)

cv2.imshow("Result", img)
cv2.waitKey(0)