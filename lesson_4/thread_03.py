import threading

counter = 0


def increment():
    global counter
    for _ in range(30_000_000):
        counter += 1
    print(f'Значение счётчика: {counter:_}')


threads = []
for i in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    # time.sleep(0.25)
    t.start()

for t in threads:
    t.join()

print(f'Значение счётчика в финале: {counter:_}')
