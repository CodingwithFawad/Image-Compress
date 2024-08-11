from PIL import Image
import os

def compress_jpeg(input_file, output_file, quality=100):
    with Image.open(input_file) as img:
        img = img.convert("RGB")  # Ensure image is in RGB mode for JPEG
        img.save(output_file, 'JPEG', quality=quality)

def get_file_size(file_path):
    return os.path.getsize(file_path)

# Get input from the user
input_file = input("Enter the path of the image file: ").strip()
quality = input("Enter the Quality (1-100): ").strip()

# Validate and convert quality to integer
try:
    quality = int(quality)
    if not (1 <= quality <= 100):
        raise ValueError("Quality must be between 1 and 100.")
except ValueError as e:
    print(f"Invalid quality value: {e}")
    exit(1)

compressed_file = 'compressed_image.jpg'

# Compress the image
try:
    compress_jpeg(input_file, compressed_file, quality=quality)
except Exception as e:
    print(f"Error compressing image: {e}")
    exit(1)

# Check file sizes
try:
    original_size = get_file_size(input_file)
    compressed_size = get_file_size(compressed_file)

    print(f'Original file size: {original_size} bytes')
    print(f'Compressed file size: {compressed_size} bytes')
except Exception as e:
    print(f"Error checking file sizes: {e}")
