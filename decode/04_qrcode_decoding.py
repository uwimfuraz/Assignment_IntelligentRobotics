import cv2
import pyzxing
import tempfile
import os

# Initialize the ZXing barcode reader
reader = pyzxing.BarCodeReader()

# Load the image using OpenCV
image = cv2.imread('qrcode.jpg')

# Save the image to a temporary file
temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
cv2.imwrite(temp_file.name, image)

# Decode the QR code from the temporary file
result = reader.decode(temp_file.name)

# Ensure the file is closed before deleting
temp_file.close()

# Clean up the temporary file
try:
    os.remove(temp_file.name)
except PermissionError:
    print(f"Could not delete temporary file {temp_file.name}. It may still be in use.")
    # Handle the error or wait for the file to be released if necessary

# Print the full result to understand its structure
print("Decoded Data:", result)

# Access and print the data based on the correct key (adjust depending on result structure)
if result:
    for item in result:
        print("Decoded Data:", item)  # or item.get('raw') if that key exists
else:
    print("No QR code found.")
