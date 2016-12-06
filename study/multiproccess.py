# import multiprocessing
#
# a = 0
#
# q = multiprocessing.Queue()
#
#
# def f():
#     global a
#     for i in range(10000):
#         a += 1
#     q.put(a)
#
#
# # ps = []
#
# for i in range(100):
#     p = multiprocessing.Process(target=f)
#     p.start()
#     # ps.append(p)
#
#
# #
# # for p in ps:
# #     p.join()
#
#
# for i in range(100):
#     a += q.get()
#
# print a
#

# pipe
# message queue
# shared memory
# sockets
















import multiprocessing
import urllib2



def get(url):
    r = urllib2.urlopen(url)
    return len(r.read())

p = multiprocessing.Pool(20)

print p.map(get, ['http://lifecell.ua/uk/'] * 1000)
