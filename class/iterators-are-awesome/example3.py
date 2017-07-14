import os

import state
from ex1c_paths import *


def main():
    cat_state = state.State('cat-state.txt')
    cat_paths = get_paths('cats-master')
    cat_images = filter(is_image, cat_paths)

    # if we're continuing, then skip up to the most recent processed image
    try:
        last_started = cat_state.fetch()
    except FileNotFoundError:
        pass
    for cat_image in cat_images:
        make_thumbnail(cat_images)

if __name__ == '__main__':
    main()

