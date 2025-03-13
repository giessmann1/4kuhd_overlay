from PIL import Image
import sys
import os

def add_4k_logo(poster_path, logo_path, position="top"):

    with Image.open(poster_path) as img:
        img = img.convert("RGB") 
        img.save(sys.argv[1], "JPEG", quality=95) # Re-save without Exif

    poster = Image.open(poster_path).convert("RGBA")
    poster_width, poster_height = poster.size
    
    logo = Image.open(logo_path).convert("RGBA")
    
    max_logo_height = int(poster_height * 0.08)
    
    logo_aspect_ratio = logo.width / logo.height
    new_logo_width = int(max_logo_height * logo_aspect_ratio)
    logo = logo.resize((new_logo_width, max_logo_height), Image.LANCZOS)
    
    black_bar = Image.new("RGBA", (poster_width, max_logo_height), (0, 0, 0, 255))

    if position == "bottom":
        bar_y = poster_height - max_logo_height
        logo_y = bar_y
    else:  # Default: top
        bar_y = 0
        logo_y = 0
    
    poster.paste(black_bar, (0, bar_y), black_bar)
    logo_x = (poster_width - new_logo_width) // 2
    poster.paste(logo, (logo_x, logo_y), logo)
    
    poster.convert("RGB").save(poster_path, "JPEG", quality=95)
    print(f"Updated poster saved: {poster_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 labeler.py <path_to_poster> [--top|--bottom]")
        sys.exit(1)
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    logo_file = os.path.join(script_dir, "4k_logo.jpg")
    
    if not os.path.exists(logo_file):
        print("Error: 4K UHD logo file not found in script directory.")
        sys.exit(1)
    
    poster_file = sys.argv[1]
    if not os.path.exists(poster_file):
        print("Error: Poster file not found.")
        sys.exit(1)
    
    # Check for optional position argument
    position = "top"
    if len(sys.argv) > 2 and sys.argv[2] in ["--top", "--bottom"]:
        position = sys.argv[2][2:]  # Strip '--' from argument
    
    add_4k_logo(poster_file, logo_file, position)