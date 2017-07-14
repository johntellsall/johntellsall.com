import os


def make_thumbnail(path):
    print(path)


def is_image(path):
    return os.path.splitext(path)[-1] in ('.jpg', '.png')


def get_paths(topdir):
    for dirpath, _, files in os.walk(topdir):
        for name in files:
            yield os.path.join(dirpath, name)


def get_cat_images():
    cat_paths = get_paths('cats-master')
    cat_images = filter(is_image, cat_paths)
    return list(cat_images)


cat_images = get_cat_images()
print(len(cat_images), cat_images[0], cat_images[-1])

for cat_image in cat_images:
    make_thumbnail(cat_image)