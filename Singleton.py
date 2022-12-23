import functools


class Counter:
    def __init__(self, initial_count=0, step=1):
        self.count = initial_count
        self.step = step

    def increment(self):
        self.count += self.step


def singleton(cls):
    singletons = {}
    default_init = cls.__init__
    default_new = cls.__new__

    @functools.wraps(default_init)
    def init(self, *args, **kwargs):
        if not (cls in singletons):
            default_init(self, *args, **kwargs)
            singletons[cls] = self

    @functools.wraps(default_new)
    def new(clas, *args, **kwargs):
        if not (clas in singletons):
            singletons[clas] = default_new(clas)
        init(singletons[clas], *args, **kwargs)
        return singletons[clas]

    cls.__new__ = new
    cls.__init__ = init
    return cls


@singleton
class GlobalCounter(Counter):
    pass


if __name__ == '__main__':
    gc1 = GlobalCounter(step=5)
    gc2 = GlobalCounter()
    print(id(gc1) == id(gc2))
