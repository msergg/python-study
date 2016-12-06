import threading

# mutext  and binary semaphore
#
#
# a = 0
#
# l = threading.Lock()
#
#
#
#
# def hello():
#     global a
#     for i in range(10000):
#         l.acquire()
#         a += 1
#         l.release()
#
#
# ts = []
# for i in range(100):
#     t = threading.Thread(target=hello)
#     # t = threading.Thread(target=hello, args=(i,))
#     t.start()
#     ts.append(t)
#
#
# for t in ts:
#     t.join()
#
#
# print a


import urllib2
import Queue

q = Queue.Queue()
is_finished = False

def get(i):
    while not is_finished:
        try:
            url = q.get(False)
            r = urllib2.urlopen(url)
            print len(r.read()), i
            q.task_done()
        except Queue.Empty:
            pass





ts = []
for i in range(5):
    t = threading.Thread(target=get, args=(i,))
    t.start()



for url in range(20):
    q.put('http://lifecell.ua/uk/')

q.join()

is_finished = True
