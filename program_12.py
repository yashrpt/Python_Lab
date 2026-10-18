import os

print("Files in current folder:")
for file in os.listdir():
    print(file)
from PIL import Image, ImageFilter

# Open an image
file_name = input("Enter image file name: ")

try:
    img = Image.open(file_name).convert("RGB")

    print("\nDigital Image Filter Utility")
    print("1. Grayscale")
    print("2. Black and White (Threshold)")
    print("3. Blur")
    print("4. Save Original Image")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        result = img.convert("L")
        output_file = "grayscale.png"

    elif choice == "2":
        gray = img.convert("L")
        result = gray.point(lambda pixel: 255 if pixel > 128 else 0)
        output_file = "black_white.png"

    elif choice == "3":
        result = img.filter(ImageFilter.BLUR)
        output_file = "blurred.png"

    elif choice == "4":
        result = img
        output_file = "original_copy.png"

    else:
        print("Invalid choice!")
        exit()

    result.save(output_file)
    result.show()

    print("Processed image saved as:", output_file)

except FileNotFoundError:
    print("Error: Image file not found.")

except Exception as e:
    print("Error:", e)
