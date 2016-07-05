class Zoot(list):

    def __init__(self, path):
        super(Zoot, self).__init__(open(path))

x = Zoot('recipe.ini')
print x
