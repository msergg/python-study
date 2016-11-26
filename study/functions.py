
# def log(f):
#     def wrapper(context):
#         print 'before'
#         f(context)
#         print str("{}" + context).format('OK')
#
#         print 'after'
#     return wrapper
#
#
# @log
# def hello(context):
#     print context
#
#
#
# hello('Its test')
#
#
#


# soc seperation of consorns
# KISS principle
# DRY

# LEGB

"""test 1"""
# python -m doctest add.py
def odd(x):
    """
    Take odd numbers only
    >>> odd(4)
    1
    >>> odd(5)
    0
    """
    return x % 2

# def double(x):
#     return x * 2
#
#
# filter(odd, [1,2,3,4,5])
#
# map(double, [1,2,3,4,5,6,7])
#
# [2 * x for x in [1,2,3,4,5,6,7] if x % 2]
#
#
# [2 * x for x in [1,2,3,4,5,6,7]]
#
#
# [2 * x for x in [1,2,3,4,5,6,7] if x % 2]
#
#
#
# map(lambda x: 2 * x, [1,2,3,4,5])
#
#
# help(abs)

# pydoc -w *.py

# python -m doctest add.py
# BuildBot


#
#
# def f(*args, **kwargs):
#     print args, kwargs
#
#
# def sum_(*args):
#     s = 0
#     for i in args:
#         s+= i
#     return s
#
#
#
# def sum_(a, *args):
#     for i in args:
#         a+= i
#     return a
#
#
# def f(a, b, c):
#     return a + b + c
#
# t = (1,2,3)
# d = {'a': 2, 'b': 4, 'c':5}
# f(**d)
# f(*t)



def f():
    def g(x):
        return 2 * x
    return g

double = f()
f(3)



a = 5
def f():
    b = a
    def g(x):
        return b + x
    return  g

dir(mul)

# Closures

def mul(x):
    def g(y):
        return  y * x
    return g


double = mul(2)
triple = mul(3)







l = []
for i in range(10):
    def f(x, a=i):
        return a * x
    l.append(f)


l[3](3)






# Carring, function composition

def mul(a, x):
    return a * x



import functools
double = functools.partial(mul, 2)

import operator

double = functools.partial(operator.mul, 2)



def composition(f, g):
    return lambda x: f(g(x))

quadruple = composition(double, double)
quadruple(4)

type(1) == int
isinstance(1,(int,float))

def odd(x):
    return x % 2

even = composition(operator.not_, odd)


l = [(1,2), (2,3), (3,4), (4,5)]

l.sort(key=lambda x:x[1])


import random

random.shuffle(l)


l.sort(key=operator.itemgetter(1))

l.sort(key=operator.attrgetter())

#iterator
type(a)
a = reversed(l)
a.next()
# type 'listreverseiterator'








# decorators





def scale(f):
    def wrapper(x):
        print "In"
        res = f(x / 100.0)
        print "Out"
        return res
    print "Scale"
    return wrapper



def scale(k):
    def decorator(f):
        def wrapper(x):
            return f(k * x)
        return wrapper
    return decorator



def get_area(x):
    return x * x

get_area = scale(get_area)


# @scale(5) :    get-area = scale(5)(get_area)

@scale(5)
def get_area(x):
    return x * x




def logger(f):
    def wrapper(*args, **kwargs):
        print "Params: {}, {}".format(args, kwargs)
        res = f(*args, **kwargs)
        print "Result: {}".format(res)
        return res
    return wrapper


@logger
def f(a,b,c):
    return a + b + c







def f_a():
    print 'Func a'


def f_b():
    print 'Func b'


def f_c():
    print 'Func c'


action = raw_input('?')



d = {'a': f_a, 'b': f_b, 'c': f_c}

def default():
    print 'Default'

d.get(action, default)()
