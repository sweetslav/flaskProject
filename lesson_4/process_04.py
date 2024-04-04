import multiprocessing
import time

counter = multiprocessing.Value('i', 0)


def increment(cnt):
    start_time = time.time()
    for _ in range(10_000):
        with cnt.get_lock():
            cnt.value += 1
    end_time = time.time()
    print(f'Значение счётчика: {cnt.value:,}')
    print(f'Время выполнения: {end_time - start_time:.2f} секунд')


if __name__ == '__main__':
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=increment, args=(counter,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f'Значение счётчика в финале: {counter.value:,}')
