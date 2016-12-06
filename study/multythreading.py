import threading

# mutext  and binary semaphore


a = 0

l = threading.Lock()




def hello():
    global a
    for i in range(1000):
        l.acquire()
        a += 1
        l.release()


ts = []
for i in range(100):
    t = threading.Thread(target=hello)
    # t = threading.Thread(target=hello, args=(i,))
    t.start()
    ts.append(t)


for t in ts:
    t.join()


print a