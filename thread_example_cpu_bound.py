import random

from threading import Thread

result = 0


def worker():
    global result
    for _ in range(100_000):
        result += random.random()


if __name__ == '__main__':
    threads = []
    for _ in range(8):
        threads.append(Thread(target=worker))
        threads[-1].start()

    for thread in threads:
        thread.join()

    print(result)