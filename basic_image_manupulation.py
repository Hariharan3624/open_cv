import cv2
import matplotlib.pyplot as plt

image = cv2.imread('example.jpg')

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.title("RGB Image")
plt.show

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image, cmap='gray')
plt.title("Gayscale Image")
plt.show()

cropped_image = image[100:300, 200:400]
cropped_rgb = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("Cropped Region")
plt.show()
key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite('grayscale_resized_image.jpg', cropped_image)
    print("Image saved as grayscale_resized_image.jpg")
else:
    print("Image not save")
cv2.destroyAllWindows()
print(f"Processed Image Dimensions: {cropped_image.shape}")
