
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