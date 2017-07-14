import os


def make_thumbnail(path):
    print(path)


def is_image(path):
    extension = os.path.splitext(path)[-1]
    return extension in ('.jpg', '.png')


def get_paths(topdir):
    paths = []
    for dirpath, _, files in os.walk(topdir):
        for name in files:
            paths.append(os.path.join(dirpath, name))
    return paths


def main():
    cat_paths = get_paths('cats-master')
    cat_images = filter(is_image, cat_paths)
    for cat_image in cat_images:
        make_thumbnail(cat_images)

if __name__ == '__main__':
    main()


def test_get_paths():
    paths = ['cats-master/README.md', 'cats-master/index.html',
             'cats-master/cat_photos/kublai32.jpg']
    assert list(get_paths('cats-master'))[:3] == paths


def test_is_image():
    assert is_image('cat.jpg')
    assert not is_image('oldfashioned.ini')
