# heif to jpeg

import os
import glob
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

def batch_convert(directory_path):
    search_path = os.path.join(directory_path, "*.heic")
    heic_files = glob.glob(search_path)
    
    if not heic_files:
        print("No HEIC files found in the directory.")
        return

    for file_path in heic_files:
        base_name = os.path.splitext(file_path)[0]
        output_path = f"{base_name}.jpg"
        
        try:
            img = Image.open(file_path)
            if img.mode != "RGB":
                img = img.convert("RGB")
            img.save(output_path, "JPEG", quality=95)
            print(f"Converted: {os.path.basename(file_path)} -> {os.path.basename(output_path)}")
        except Exception as e:
            print(f"Failed to convert {file_path}: {e}")

batch_convert(".")