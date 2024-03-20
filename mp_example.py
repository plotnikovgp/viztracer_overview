from multiprocessing import Pool, cpu_count
from time import perf_counter


def sum_of_squares(start, end):
    result = 0
    for i in range(start, end):
        result += i ** 2
    return result


def count_sum_of_squares(n, chunks = cpu_count() // 2):
    step: int = n // chunks
    ranges = [(step * i, step * (i + 1)) for i in range(chunks)]

    with Pool(chunks) as pool:
        results = pool.starmap(sum_of_squares, ranges)
    return sum(results)


if __name__ == '__main__':
    start_t = perf_counter()
    print("result", count_sum_of_squares(10_000_000))
    print("time", perf_counter() - start_t)
    