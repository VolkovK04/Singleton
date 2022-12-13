import functools


class Counter:
    def __init__(self, initial_count=0, step=1):
        self.count = initial_count
        self.step = step

    def increment(self):
        self.count += self.step


def singleton(cls):
    singletons = {}

    @functools.wraps(cls)
    def init(*args, **kwargs):
        if cls in singletons:
            return singletons[cls]
        else:
            singletons[cls] = cls(*args, **kwargs)
            return singletons[cls]
    return init


@singleton
class GlobalCounter(Counter):
    pass


if __name__ == '__main__':
    gc1 = GlobalCounter(step=5)
    gc1.increment()
    gc2 = GlobalCounter()
    print(id(gc1) == id(gc2))

