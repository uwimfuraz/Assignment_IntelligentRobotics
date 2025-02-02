import cv2
from pyzxing import BarCodeReader

# Read the image
image = cv2.imread('aztec.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to make the barcode stand out more (if necessary)
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Save the processed image or pass it directly to the barcode reader
cv2.imwrite('processed_image.png', thresh)

# Decode with pyzxing
reader = BarCodeReader()
result = reader.decode('processed_image.png')[0]['raw']

print(result)