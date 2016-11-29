class Table(object):
    #  t = Table(1,2,3)
    # vars(t)

    def __init__(self, l, w, h):
        print "Init"
        self.l = l
        self.w = w
        self.h = h


# Static variable
# class A(object):
#     a = 1
#
#     def __init__(self):
#         A.a += 1
#         print A.a
#
#     def f(self):
#         print "Class A"
#
#
# a = A()
# b = A()







class B(object):
    __slots__ = ('x')
    def __init__(self, x):
        self.x = x
        print "Class B"

a = A()
a.f()
b = B()




# Polymorphism , magic methods


class Cat():
    def say(self):
        print 'Meow'

    def __repr__(self):
        return 'I`m a Cat'

    def __str__(self):
        return 'String representation'








