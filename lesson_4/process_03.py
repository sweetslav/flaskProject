import multiprocessing
import time

counter = 0


def increment():
    global counter
    start_time = time.time()
    for _ in range(10_000):
        counter += 1
    end_time = time.time()
    print(f'Значение счётчика: {counter:_}')
    print(f'Время выполнения: {end_time - start_time:.2f}')


if __name__ == '__main__':
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=increment)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f'Значение счётчика в финале: {counter:_}')
