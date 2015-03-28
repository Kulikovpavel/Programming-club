from multiprocessing import Process, Queue
from time import sleep


def f1(q):
    for i in range(5):
        sleep(1)
        q.put(i)

def f2(q):
    while True:
        sleep(1)
        if not q.empty():
            print(q.get())

if __name__ == '__main__':
    q = Queue()

    p1 = Process(target=f1, args=(q,))
    p2 = Process(target=f2, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while p1.is_alive():
        pass

    p2.terminate()
