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








@staticmethod
@classmethod


class A(object):
    def __init__(self):
        self.a = 42

    # def __setattr__(self, name, value):
    #     if hasattr(self,'a') and name == 'a':
    #         raise AttributeError('a is read-only')
    #     print "Set {} = {}".format(name, value)
    #     super(A, self).__setattr__(name, value)


    def __delattr__(self, name):
        if name == 'a':
            raise AttributeError('a is read-only')
        super(A, self).__delattr__(name)


    def __getattribute__(self, name):
        print "Get attribute " + name
        return super(A, self).__getattribute__(name)

    def __getattr__(self, name):
        print "Get attr" + name
        return 44


class Mock(object):
    def __getattr__(self, item):
        return lambda x: x*x


#
# import whois
# domain = whois.query('google.com')
#
# print(domain.__dict__)
#
# print(domain.name)
#
#




class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "Person({}, {})".format(self.name, self.age)

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __lt__(self, other):
        return self.age < other.age


l = [Person('Bob',32), Person('John', 43), Person('Bill', 23)]
l.sort()