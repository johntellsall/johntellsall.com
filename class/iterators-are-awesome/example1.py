import glob


def make_thumbnail(path):
    print(path)

cat_dirs = ['cats-master/cat_photos', 'cats-master/catmapper']

for cat_dir in cat_dirs:
    cat_images = glob.glob('{}/*.jpg'.format(cat_dir))
    for image in cat_images:
        make_thumbnail(image)

