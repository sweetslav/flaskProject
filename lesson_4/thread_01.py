import threading
import time


def worker(num):
    print(f'Начало работы потока {num}')
    time.sleep(4)
    print(f'Конец работы потока {num}')


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    # time.sleep(0.25)
    t.start()

for t in threads:
    t.join()

print('Все потоки завершили работу')
