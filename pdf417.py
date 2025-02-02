import cv2
import numpy as np
import subprocess
import os

# Paths to required files
javase_jar = "C:/Users/user/Downloads/opencv/opencv/Decoding/javase-3.5.0.jar"
core_jar = "C:/Users/user/Downloads/opencv/opencv/Decoding/core-3.5.0.jar"
jcommander_jar = "C:/Users/user/Downloads/opencv/opencv/Decoding/jcommander-1.82.jar"
barcode_image = "C:/Users/user/Downloads/opencv/opencv/Decoding/id-gabriel.png"
image_path= "file:///"+barcode_image.replace("//","/")
# Validate required files
for file in [javase_jar, core_jar, jcommander_jar, barcode_image]:
    if not os.path.exists(file):
        print(f"Error: {file} not found!")
        exit(1)

# Java command to detect the barcode and get its position
java_command = [
    "java",
    "-cp",
    f"{javase_jar};{core_jar};{jcommander_jar}",  # Classpath for Windows
    "com.google.zxing.client.j2se.CommandLineRunner",
    image_path # Use normal path, no file:// needed
]

# Debugging: Check the actual command
print("Running command:", " ".join(java_command))
try:
    # Run the Java command to get the decoding and position
    result = subprocess.run(java_command, capture_output=True, text=True, check=True)
    output = result.stdout.strip()
    print("Decoded Output:")
    print(output)
except subprocess.CalledProcessError as e:
    print("Error during decoding:")
    print(e.stderr)
    exit(1)

# Parse the ZXing output for barcode position
points = []
for line in output.splitlines():
    if line.startswith("  Point"):
        parts = line.split(":")[1].strip().replace("(", "").replace(")", "").split(",")
        points.append((int(float(parts[0])), int(float(parts[1]))))

# If points are found, draw a bounding polygon
if len(points) >= 4:
    # Load the image with OpenCV
    image = cv2.imread(barcode_image)
    if image is None:
        print("Error: Unable to read the image!")
        exit(1)

    # Draw a polygon connecting the points
    points_array = np.array(points, dtype=np.int32).reshape((-1, 1, 2))
    print(f"Drawing polygon with points: {points}")

    cv2.polylines(image, [points_array], isClosed=True, color=(0, 255, 0), thickness=2)

    # Save and display the annotated image
    annotated_image_path = "annotated_barcode.png"
    cv2.imwrite(annotated_image_path, image)
    print(f"Annotated image saved as {annotated_image_path}")

    # Display the image
    cv2.imshow("Detected Barcode", image)
    print("Press any key to close the window.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No bounding box points detected.")
