# Задание №4.3.
# Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории.
# Использую процессы

import logging
import time
from multiprocessing import Process
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='seminar_5.log',
    filemode='a', # обязательно ставим режим дописывания файла
)

logger = logging.getLogger(__name__)


def count_words_in_file(file_path: Path) -> int:
    """Подсчитывает количество слов в файле."""
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        words = content.split()
        return len(words)


def process_file(file_path: Path):
    """Обрабатывает один файл."""
    word_count = count_words_in_file(file_path)
    logger.info(f"File: {file_path}, Word Count: {word_count}")


def process_directory(directory_path: Path):
    """Обрабатывает все нескрытые файлы в указанной директории и рекурсивно в поддиректориях."""
    processes = []
    for file_path in directory_path.glob('[!.]*'):  # [!.]* - шаблон, игнорирует скрытые файлы, начинающиеся с точки
        if file_path.is_file():
            logger.info(f"Processing file: {file_path}")
            process = Process(target=process_file, args=(file_path,))
            processes.append(process)
            process.start()
        elif file_path.is_dir():
            logger.info(f"Processing directory: {file_path}")
            process_directory(file_path)

        for process in processes:
            process.join()
            if process.exitcode != 0:
                logger.error(f"Process failed with exit code {process.exitcode} for file: {file_path}")


def main():
    start_time = time.time()

    directory_path = Path('..')
    process_directory(directory_path)

    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f'Time taken: {elapsed_time:.2f} seconds')


if __name__ == '__main__':
    main()
