from coroutil import coroutine
from inspect import getgeneratorstate


@coroutine
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count
        print(average)


if __name__ == "__main__":
    coro_avg = averager()
    state = getgeneratorstate(coro_avg)
    print(state)
    coro_avg.send(10)
    coro_avg.send(20)