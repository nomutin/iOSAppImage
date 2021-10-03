"""
iOS appアイコンのリサイズする
Usage: python3 main.py PATH_TO_IMAGE (PATH_TO_SAVE_DIRECTORY)
"""
# TODO アスペクト比を変えずにリサイズできるようにしたい

import datetime
import sys
import os
from PIL import Image

IOS_ICON_SIZES = [1024, 180, 167, 152, 120, 87, 80, 76, 60, 58, 40, 29, 20]

if __name__ == '__main__':
    path_to_image = sys.argv[1]
    _, ext = os.path.splitext(path_to_image)

    try:
        path_to_save_dir = sys.argv[2]
    except IndexError:
        formatted_current_date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        path_to_save_dir = os.path.join(os.getcwd(), f'icon-{formatted_current_date}')

    if not os.path.exists(path_to_save_dir):
        os.mkdir(path_to_save_dir)

    with Image.open(path_to_image) as img:
        for size in IOS_ICON_SIZES:
            img_resized = img.resize((size, size))
            img_resized.save(os.path.join(path_to_save_dir, f"Icon-{size}{ext}"))
        print(f'SAVE DIR: {path_to_save_dir} is correctly created and IMAGE: {path_to_image} is correctly converted.')
