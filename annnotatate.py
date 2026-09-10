import cv2
import matplotlib.pyplot as plt
import numpy as np
image_path = "example.jpg"
canvas = cv2.imread(image_path)
if canvas is None:
    canvas = np.ones((500, 700, 3), dtype=np.uint8) * 220
pt1 = (150, 100)
pt2 = (550, 400)
width = abs(pt2[0] - pt1[0])
height = abs(pt2[1] - pt1[1])
rect_color = (0, 0, 255)
cv2.rectangle(canvas, pt1, pt2, rect_color, thickness=4)
canvas_rgb = cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(8, 6))
plt.imshow(canvas_rgb)
label_text = f"Width: {width}px\nHeight: {height}px"
plt.text(pt1[0], pt1[1] - 15, 
label_text, fontsize=11, color='white', weight='bold',bbox=dict(facecolor='red', alpha=0.8, edgecolor='none', boxstyle='round,pad=0.5'))
plt.title("Annotated Rectangle Dimensions", fontsize=14, weight='bold', pad=15)
plt.axis("on")
plt.tight_layout()
plt.show()
