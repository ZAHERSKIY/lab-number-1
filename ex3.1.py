import cv2
   
image = cv2.imread('pic.jpg')
hsvImage = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
 
cv2.imshow('Original image',image)
cv2.imshow('HSV image', hsvImage)

cv2.imwrite('HSV.jpg', hsvImage)

rgbImage = cv2.cvtColor(hsvImage, cv2.COLOR_HSV2RGB)

cv2.imshow('Converted_back', rgbImage)
   
cv2.waitKey(0)
cv2.destroyAllWindows()
