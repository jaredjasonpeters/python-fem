def sayHello(name):
    print(f'Hello {name}')


def fn1(fn):
    return fn


fn1(lambda name: print(f'hello {name}'))('Jim')
