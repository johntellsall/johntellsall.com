class MyOdd:
    def __init__(self, data):
        self.data = iter(data)

    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            value = next(self.data)
            if value % 2 == 1:
                return value


def test_odd_class():
    assert list(MyOdd([1, 2, 3, 4, 5])) == [1, 3, 5]


def odd_func(values):
    return (value for value in values if value % 2 == 1)


def test_odd_func():
    assert list(odd_func([1, 2, 3, 4, 5])) == [1, 3, 5]

