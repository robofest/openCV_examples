import cv2

img = cv2.imread('images/cog.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Ensure it's a binary mask (0 or 255)
_, mask = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Calculate spatial moments of the binary image
M = cv2.moments(mask)

# Calculate the centroid (cX, cY)
# M["m00"] represents the total area. We check if it's > 0 to avoid division by zero.
if M["m00"] != 0:
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])

    print(f"Centroid Coordinates: cX = {cX}, cY = {cY}")

    # Draw the center on a color version of the image to visualize it
    output = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    cv2.circle(output, (cX, cY), 5, (0, 0, 255), -1)  # Red dot at the center
    cv2.imshow("Centroid", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("The mask is completely black; no centroid could be found.")
