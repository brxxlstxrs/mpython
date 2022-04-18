class SpaceArray():
    def __init__(self):
        self.array = dict()

    def __getitem__(self, key):
        return self.array.get(key, 0)

    def __setitem__(self, key, value):
        self.array[key] = value
