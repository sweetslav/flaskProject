# Задание №4.2.
# Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории.
# Использую потоки

import logging
import threading
import time
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='seminar_4.log',
    filemode='w',
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
    """Обрабатывает все файлы в указанной директории и рекурсивно в поддиректориях."""
    threads = []
    for item in directory_path.glob('[!.]*'):
        if item.is_file():
            thread = threading.Thread(target=process_file, args=(item,))
            threads.append(thread)
            thread.start()
        elif item.is_dir():
            process_directory(item)
    for thread in threads:
        thread.join()


def main():
    start_time = time.time()

    directory_path = Path('..')
    process_directory(directory_path)

    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f'Time taken: {elapsed_time:.2f} seconds')


if __name__ == '__main__':
    main()
