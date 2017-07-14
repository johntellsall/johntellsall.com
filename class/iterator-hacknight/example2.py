import os


def is_image(path):
    return os.path.splitext(path)[-1] in ('.jpg', '.png')


def get_paths(topdir):
    for dirpath, _, files in os.walk(topdir):
        for name in files:
            yield os.path.join(dirpath, name)

cat_paths = get_paths('cats-master')
cat_images = filter(is_image, cat_paths)
cat_images = list(cat_images)
print(len(cat_images), cat_images[0], cat_images[-1])
