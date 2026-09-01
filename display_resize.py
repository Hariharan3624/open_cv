import cv2
original_image = cv2.imread('example.jpg')
if original_image is None:
    print("error")
else:
    predefined_sizes = {
        "small": (320, 240),
        "medium": (640, 480),
        "large": (1280, 720)
    }
    for size_name, dimensions in predefined_sizes.items():
        resized_image = cv2.resize(original_image, dimensions, interpolation=cv2.INTER_AREA)
        output_filename = f"resized_{size_name}.jpg"
        cv2.imwrite(output_filename, resized_image)
        print(f"Saved: {output_filename} with dimensions {dimensions}")
        window_name = f"Resized Image - {size_name.capitalize()}"
        cv2.imshow(window_name, resized_image)
        print(f"Displaying '{window_name}'. Press any key to continue...")
        cv2.waitKey(0)
        cv2.destroyWindow(window_name)
    cv2.destroyAllWindows()
    print("Processing complete!")
