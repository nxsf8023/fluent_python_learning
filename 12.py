
def fun(*args, **kwargs):
    for l in args:print(l)
    it = kwargs.items()
    d = 1

fun(0, 1, a=3, b=4)