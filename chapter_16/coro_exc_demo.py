from inspect import getgeneratorstate

class DemoException(Exception):
    """Test"""


def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except Exception:
            print('*** DemoException handled. Continuing...')
        else:
            print('-> coroutine received: {!r}'.format(x))

    raise RuntimeError('This line should never run.')


if __name__ == "__main__":
    exc_coro = demo_exc_handling()
    print(getgeneratorstate(exc_coro))
    next(exc_coro)
    print(getgeneratorstate(exc_coro))
    exc_coro.throw(DemoException)
