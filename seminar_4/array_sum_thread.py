# � Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами от 1 до 100.
# � При решении задачи нужно использовать синхронность, многопоточность, многопроцессорность и асинхронность.
# � В каждом решении нужно вывести время выполнения вычислений.

import concurrent.futures
import logging
import random
import time

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='array_sum_thread.log',
    filemode='w')

arr = [random.randint(1, 10_000_000) for _ in range(1_000_000)]


def calculate_sum(arr):
    return sum(arr)


if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor:
        start_time = time.time()
        future = executor.submit(calculate_sum, arr)
        sum_thread = future.result()
        end_time = time.time()
        execution_time_thread = end_time - start_time

    logging.info(f'Сумма элементов (многопоточно): {sum_thread:_}')
    logging.info(f'Время выполнения (многопоточно): {execution_time_thread:.4f} секунд')
