
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


f = fibonacci()
print(next(f))
print(next(f))