from inspect import getgeneratorstate


def simple_coro2(a):
    print('-> Started: a =', a)
    b = yield a
    print('-> Recieve: b =', b)
    c = yield b
    print('-> Receive: c =', c)


my_coro2 = simple_coro2(14)
print(getgeneratorstate(my_coro2))
next(my_coro2)
print(getgeneratorstate(my_coro2))
print(my_coro2.send(28))