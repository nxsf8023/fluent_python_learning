import weakref
stock = weakref.WeakValueDictionary()


class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return "Cheese({})".format(self.kind)

catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Parmesan'), Cheese('Brie')]

for cheese in catalog:
    stock[cheese.kind] = cheese

print(sorted(stock.keys()))

del catalog

print(sorted(stock.keys()))

print(cheese)

del cheese

print(sorted(stock.keys()))

class MyList(list):
    """111"""

a_list = MyList(range(10))
wref_to_a_list = weakref.ref(a_list)
print(wref_to_a_list())