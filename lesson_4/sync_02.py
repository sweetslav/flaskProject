import time


def slow_function():
    print('Start slow_function')
    time.sleep(5)
    print('End slow_function')


def main():
    print('Start program')
    slow_function()
    print('End program')


if __name__ == '__main__':
    main()

