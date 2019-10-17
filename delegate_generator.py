
def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


@coroutine
def subgen():
    while True:
        try:
            message = yield
        except:
            pass
        else:
            print('..........', message)


class MyException(Exception):
    pass


@coroutine
def delegator(g):
    while True:
        try:
            data = yield
            g.send(data)
        except MyException as e:
            g.throw(e)
