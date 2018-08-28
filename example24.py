import cv2


img=cv2.imread("lena.jpg")

smaller=cv2.pyrDown(img)
larger=cv2.pyrUp(img)

cv2.imshow('Original',img)
cv2.imshow('Smaller',smaller)
cv2.imshow('Larger',larger)

cv2.waitkey(0)
cv2.destroyAllWindows()
