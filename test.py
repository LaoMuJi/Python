import threading as t

lock = t.Lock()
a,b = 0,1000000000

def jia():
    global a,b
    for i in range(1,b):
        lock.acquire()
        a+=1


def jian():
    global a,b
    for i in range(1,b):
        a-=1

def jia1():
    global a,b
    for i in range(1,b):
        a+=1


def jian1():
    global a,b
    for i in range(1,b):
        a-=1

if __name__ == '__main__':
    t1 = t.Thread(target=jia,args=())
    t2 = t.Thread(target=jian,args=())
    t3 = t.Thread(target=jia1,args=())
    t4 = t.Thread(target=jian1,args=())
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print(a)
