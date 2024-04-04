import time
import random


def long_running_task():
    for i in range(5):
        print(f'Task {i} is running')
        time.sleep(random.randint(1, 5))


def program_status(func):
    def wrapper(*args, **kwargs):
        print("Старт программы")
        result = func(*args, **kwargs)
        print("Конец программы")
        return result

    return wrapper


@program_status
def main():
    long_running_task()


if __name__ == '__main__':
    main()
