import cv2
from pyzxing import BarCodeReader

# Read the image
image = cv2.imread('maxicode.png')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding (if needed)
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Save the preprocessed image or pass it directly to ZXing
cv2.imwrite('processed_maxicode.png', thresh)

# Decode using ZXing
reader = BarCodeReader()
result = reader.decode('processed_maxicode.png')[0]['raw']

print(result)
