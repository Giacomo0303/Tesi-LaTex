import os
import sys
from PIL import Image

def split_plot(img_path):
    if not os.path.exists(img_path):
        print(f"Error: {img_path} does not exist.")
        return

    # Load image
    img = Image.open(img_path)
    width, height = img.size
    
    if width != 1400 or height != 900:
        print(f"Warning: Expected image dimensions 1400x900, but got {width}x{height}. Crops might not align correctly.")

    # Calculate crop coordinates for 300px height subplots
    crop_top = img.crop((0, 39, width, 339))
    crop_middle = img.crop((0, 320, width, 620))
    crop_bottom = img.crop((0, 600, width, height))

    base, ext = os.path.splitext(img_path)
    
    # Save cropped subplots
    save_kwargs = {"format": "PNG", "compress_level": 9}
    
    top_path = f"{base}_top{ext}"
    mid_path = f"{base}_middle{ext}"
    bot_path = f"{base}_bottom{ext}"
    
    crop_top.save(top_path, **save_kwargs)
    crop_middle.save(mid_path, **save_kwargs)
    crop_bottom.save(bot_path, **save_kwargs)
    
    print(f"Successfully split '{os.path.basename(img_path)}' into:")
    print(f"  - {os.path.basename(top_path)}")
    print(f"  - {os.path.basename(mid_path)}")
    print(f"  - {os.path.basename(bot_path)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python split_stacked_plot.py <image_path>")
        sys.exit(1)
    
    split_plot(sys.argv[1])
