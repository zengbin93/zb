
import cv2

fn_img = "\\xl.jpg"

img = cv2.imread(fn_img, cv2.IMREAD_COLOR)
cv2.namedWindow("test")
cv2.imshow("test", img)
