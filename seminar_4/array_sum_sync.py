# � Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами от 1 до 100.
# � При решении задачи нужно использовать синхронность, многопоточность, многопроцессорность и асинхронность.
# � В каждом решении нужно вывести время выполнения вычислений.

import random
import time
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='array_sum_sync.log',
    filemode='w')


arr = [random.randint(1, 1_000_000) for _ in range(1_000_000)]

if __name__ == '__main__':
    start_time = time.time()
    sum_sync = sum(arr)
    end_time = time.time()
    execution_time_sync = end_time - start_time
    logging.info(f'Сумма элементов (синхронно): {sum_sync:_}')
    logging.info(f'Время выполнения (синхронно): {execution_time_sync:.4f}')
