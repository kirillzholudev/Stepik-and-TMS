def f(arg):

    def wrapper(*b):
        print(b[::-1])

    return wrapper

@f
def num(*a):
    print(a)


num(5,5,8,9,1,0,0)
