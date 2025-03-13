# 4K UHD Overlay Labeler

## Overview
This Python script adds a 4K UHD overlay to the top or bottom of a given poster image (for Jellyfin, Plex, etc.). It resizes the logo to fit proportionally, places it on a black bar, and saves the updated poster in JPEG format.

### Installation
Create a virtual environment and install the dependencies from `requirements.txt`:

```sh
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

## Usage
Run the script using the following command:

```sh
python3 labeler.py <path_to_poster> [--top|--bottom]
```

### Parameters

- `<path_to_poster>`: Path to the poster image file.
- `[--top|--bottom]` (optional): Position of the 4K UHD logo. Defaults to top if not specified.

### Example

```sh
python3 labeler.py movie_poster.jpg --bottom
```

This will add the 4K UHD logo to the bottom of `movie_poster.jpg`. See example files.

## License
This project is licensed under the MIT License.