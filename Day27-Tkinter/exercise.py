# What is the output of this code?

def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)


bar(1, 2)


# What is the output of this code?
def bar(spam, eggs, toast='yes please!', ham=0):
    print(spam, eggs, toast, ham)


bar(toast='nah', spam=4, eggs=2)


# What is the data type of args?
def test(*args):
    print(args)


test(1, 2, 3, 5)


# What is the output of the code above?
def test(*args):
    print(args)


test(1, 2, 3, 5)


# What is the output of the code above?
def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)
