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
        return lambda x: x * x


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


l = [Person('Bob', 32), Person('John', 43), Person('Bill', 23)]
l.sort()


class ReprMixin(object):
    def __repr__(self):
        return '{}({})'.format(
            self.__class__.__name__,
            ', '.join(['{}={}'.format(k, v) for k, v in self.__dict__.items()])
        )


class EqMixin(object):
    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.__dict__ == other.__dict__


# mro

class Person(ReprMixin, EqMixin):
    def __init__(self, name, age):
        self.name, self.age = name, age

    def __getstate__(self):
        return {
            'name': self.name,
            'age': self.age

        }

    def __setstate__(self, state):
        self.__init__(**state)


# >>> Person('John', 10)
# Person(age=10, name=John)
# >>> Person('John', 10) == Person('John', 10)
# True
# >>> Person('John', 10) == Person('John', 11)
# False



# whois UA https://hostmaster.ua/whois.php?domain=lifecell.ua
# to parse all parameters in to dict "<td.*>(?<a>.*)<\/td><td>(?<b>.*)<\/td>"


import re
import urllib2


def get_whois(url):
    url = 'https://hostmaster.ua/whois.php?domain=' + url
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    html_page = response.read()

    r = re.findall(r'<td.*>(.*)<\/td><td>(.*)<\/td>', html_page)

    print r

    for i in r:
        print i[0] + ':' + i[1]


get_whois('lifecell.ua')


class MyList(object):
    def __init__(self, l=[]):
        self._l = l[:]

    def __repr__(self):
        return repr(self._l)

    def __len__(self):
        return len(self._l)

    def __contains__(self, item):
        return item in self._l

    def add(self, value):
        self._l.append(value)

    def __setitem__(self, key, value):
        self._l[key] = value

    def __getitem__(self, item):
        if isinstance(item, int):
            return self._l[item]
        elif isinstance(item, tuple):
            return [self._l[x] for x in item if 0 <= x < len(self._l) - 1]
        elif item == Ellipsis:
            return self._l[:]

    # def __iter__(self):
    #     return MyListIterator(self._l)

    def __iter__(self):
        # returns generator object
        for i in self._l:
            yield i


class MyListIterator(object):
    def __init__(self, l):
        self._l = l[:]
        self.i = 0

    def __iter__(self):
        return self

    def next(self):
        if self.i == len(self._l):
            raise StopIteration
        self.i += 1
        return self._l[self.i - 1]


def f():
    print 'a'


import dis

dis.dis(f)


#
# async - coroutine
# await - yield

# lazy calculations

def f(x, y):
    if x:
        return 2 * x * y


# f (x, g(a,b)) if g(a,b) = > generator


def inf_list():
    i = 0
    while True:
        yield i
        i += 1


for i in inf_list():
    if i * i > 1000:
        break
    print i

g = xrange(10)

i = iter(g)
i.next()

import itertools

print list(itertools.takewhile(lambda i: i * i <= 100, itertools.count()))

permutations = itertools.permutations('ABC', 2)

print list(permutations)

[x * x for x in range(10)]  # list comprehensions

(x * x for x in range(10))  # generator


# twsited acsync lib

# aiohttp




# coroutine
def coroutine(f):
    g = f()
    g.next()
    return g


@coroutine
def f():
    i = yield

    print 'f,', i
    i = yield i + 1
    print 'f,', i
    i = yield i + 1
    print 'f,', i
    i = yield i + 1


def main():
    i = f.send(0)
    print 'main, ', i
    i = f.send(i + 1)
    print 'main, ', i
    i = f.send(i + 1)
    print 'main, ', i


# Constructor / singleton

class A(object):
    def __new__(cls, *args, **kwargs):
        print "NEW"
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls, *args)
        return cls._instance

        # return super(A, cls).__new__(cls, *args, **kwargs)

    def __init__(self):
        print 'init'


class Line(object):
    def __init__(self):
        self._l = 0

    @property
    def l(self):
        return self._l * 10

    @l.setter
    def l(self, value):
        self._l = value / 10


# Metaclasses
A = type('A', (object,), {'a': 1})


class A(object):
    a = 1


class Meta(type):
    def __new__(cls, name, parents, attrs):
        new_attrs = {name: value
                     for name, value in attrs.items()
                     if not name.startswith('unused')}

        return type.__new__(cls, name, parents, new_attrs)


class A(object):
    __metaclass__ = Meta

    a = 1
    unused_a = 1


import abc


class Base(object):
    __metaclass__ = abc.ABCMeta

    def f(self):
        print 'Base.f'

    @abc.abstractmethod
    def g(self):
        pass


class Child(Base):
    def g(self):
        pass
