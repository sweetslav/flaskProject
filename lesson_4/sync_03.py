import time
import random


def long_running_task():
    for i in range(5):
        print(f'Task {i} is running')
        time.sleep(random.randint(1, 5))


def main():
    print('Start program')
    long_running_task()
    print('End program')


if __name__ == '__main__':
    main()
