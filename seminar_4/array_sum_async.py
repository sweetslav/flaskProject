# � Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами от 1 до 100.
# � При решении задачи нужно использовать синхронность, многопоточность, многопроцессорность и асинхронность.
# � В каждом решении нужно вывести время выполнения вычислений.

import asyncio
import logging
import random
import time

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='array_sum_async.log',
    filemode='w')

arr = [random.randint(1, 10_000_000) for _ in range(1_000_000)]


async def calculate_sum(arr):
    return sum(arr)


async def main():
    start_time = time.time()
    sum_async = await calculate_sum(arr)
    end_time = time.time()
    execution_time_async = end_time - start_time

    logging.info(f'Сумма элементов (асинхронно): {sum_async:_}')
    logging.info(f'Время выполнения (асинхронно): {execution_time_async:.4f} секунд')


if __name__ == '__main__':
    asyncio.run(main())
