import qrcode
import cv2
from cv2 import  imread
img=qrcode.make("Vaibhav Parkale")
img.save("vaibhav.jpg")

d=cv2.QRCodeDetector()
val,s,p=d.detectAndDecode(cv2.imread("vaibhav.jpg"))
print(val)
