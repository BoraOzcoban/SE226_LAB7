import cv2

image = cv2.imread('bird.jpeg')
b, g, r = cv2.split(image)

cv2.imshow('Blue', b)
cv2.waitKey(0)

cv2.imshow('Green', g)
cv2.waitKey(0)

cv2.imshow('Red', r)
cv2.waitKey(0)

cv2.destroyAllWindows()

g.fill(0)

newImage = cv2.merge([b, g, r])

cv2.imshow('Image Without Green', newImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()