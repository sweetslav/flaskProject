# Задание №4.1.
# Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории.

import logging
import time
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='sync.log',
    filemode='w',
)

logger = logging.getLogger(__name__)


def count_words_in_file(file_path: Path) -> int:
    """Подсчитывает количество слов в файле."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except Exception as e:
        logger.error(f"Error processing file '{file_path}': {e}")
        return 0


def process_directory(directory_path: Path):
    """Обрабатывает все файлы в указанной директории и рекурсивно в поддиректориях."""
    for item in directory_path.glob('[!.]*'):
        if item.is_file():
            word_count = count_words_in_file(item)
            logger.info(f"File: {item}, Word Count: {word_count}")
        elif item.is_dir():
            process_directory(item)


def main():
    start_time = time.time()

    directory_path = Path('..')
    process_directory(directory_path)

    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f'Time taken: {elapsed_time:.2f} seconds')


if __name__ == '__main__':
    main()
