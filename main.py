import cv2

shwedagon = cv2.imread("assets/shwedagon.jpg")

shwedagonGrayScale = cv2.cvtColor(shwedagon, cv2.COLOR_BGR2GRAY)
shwedagonBlurred = cv2.GaussianBlur(shwedagonGrayScale, (5, 5), 0)

edgeDetected = cv2.Canny(shwedagonBlurred, threshold1 = 180, threshold2 = 200)

cv2.imshow("Shwedagon Edges", edgeDetected)

cv2.waitKey(0)
cv2.destroyAllWindows()