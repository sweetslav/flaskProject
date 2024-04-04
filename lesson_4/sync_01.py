import time


def count_down(seconds: int) -> None:
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)


if __name__ == '__main__':
    count_down(5)
