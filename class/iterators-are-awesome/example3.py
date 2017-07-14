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
        # consume images until XX
        print('STATE: starting from {}'.format(last_started))
        for cat_image in cat_images:
            if cat_image == last_started:
                break
        sys.exit('{}: state file corrupt'.format(last_started))
    except FileNotFoundError:
        print('STATE: starting anew')

    for cat_image in cat_images:
        make_thumbnail(cat_image)

if __name__ == '__main__':
    main()

