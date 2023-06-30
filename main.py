import functools
import timeit
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def count(n):
    j = 0
    for i in range(n):
        # do some work
        if i % 2 == 0:
            j += 1
        else:
            j -= 1


def multi_threaded(n):
    workers = 4
    target = int(n / workers)
    e = ThreadPoolExecutor(max_workers=workers)
    for i in range(workers):
        e.submit(count, target)
    # wait for all tasks to complete
    e.shutdown(wait=True, cancel_futures=False)


def multi_process(n):
    workers = 4
    target = int(n / workers)
    e = ProcessPoolExecutor(max_workers=workers)
    for i in range(workers):
        e.submit(count, target)
    # wait for all tasks to complete
    e.shutdown(wait=True, cancel_futures=False)


if __name__ == '__main__':
    work = 50_000_000
    t = timeit.Timer(functools.partial(count, work))
    print(f"Single Threaded: {t.timeit(5)}")

    t = timeit.Timer(functools.partial(multi_threaded, work))
    print(f"Multi Threaded: {t.timeit(5)}")

    t = timeit.Timer(functools.partial(multi_process, work))
    print(f"Multi Process: {t.timeit(5)}")






