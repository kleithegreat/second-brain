# dependencies: imagemagick, img2pdf
import requests
import os
from data import title, urls

folder = title.replace(' ', '-')
abs_folder_path = os.path.abspath(folder)

# Ensure the folder exists
if not os.path.exists(abs_folder_path):
    os.mkdir(abs_folder_path)

# Download images from URLs
image_files = []
for i, u in enumerate(urls.splitlines()):
    if u:
        print(f'Downloading chunk {i} of {title}')
        image_path = os.path.join(abs_folder_path, f"{i:02}.png")
        with open(image_path, 'wb') as out_file:
            out_file.write(requests.get(u.strip()).content)
        image_files.append(image_path)

print("Files downloaded:", image_files)

# Merge every 6 images vertically
merged_images = []
for i in range(0, len(image_files), 6):
    segment = [f'"{img}"' for img in image_files[i:i+6]]
    merged_image_path = os.path.join(abs_folder_path, f"merged_{i//6}.png")
    os.system(f'magick convert -append {" ".join(segment)} "{merged_image_path}"')
    merged_images.append(merged_image_path)

print("Merged images:", merged_images)

# Convert merged images to a single PDF using img2pdf
output_pdf_path = os.path.join(os.getcwd(), f"{title}.pdf")
print(f'Converting: {" ".join(merged_images)} to {output_pdf_path}')

# Ensure each image path in merged_images is wrapped in double quotes
merged_images = [f'"{img}"' for img in merged_images]

# Use img2pdf for conversion as it typically preserves original image size without extra margins
os.system(f'img2pdf {" ".join(merged_images)} -o "{output_pdf_path}"')

print('Done')
