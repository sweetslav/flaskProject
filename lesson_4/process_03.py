import multiprocessing

counter = 0


def increment():
    global counter
    for _ in range(100_000):
        counter += 1
    print(f'Значение счётчика: {counter:_}')


if __name__ == '__main__':
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=increment)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f'Значение счётчика в финале: {counter:_}')
