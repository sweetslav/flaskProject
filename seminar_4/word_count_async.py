# Задание №4.3.
# Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории.
# Использую процессы

import asyncio
import logging
import time
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='async.log',
    filemode='w', )

logger = logging.getLogger(__name__)


async def count_words_in_file(file_path: Path) -> int:
    """Подсчитывает количество слов в файле."""
    try:
        async with open(file_path, 'r', encoding='utf-8') as file:
            content = await file.read()
            words = content.split()
            return len(words)
    except Exception as e:
        logger.error(f"Error processing file '{file_path}': {e}")
        return 0


async def process_file(file_path: Path) -> None:
    """Обрабатывает один файл."""
    word_count = await count_words_in_file(file_path)
    logger.info(f"File: {file_path}, Word Count: {word_count}")


async def process_directory(directory_path: Path) -> None:
    """Обрабатывает все нескрытые файлы в указанной директории и рекурсивно в поддиректориях."""
    tasks = []
    for file_path in directory_path.glob('[!.]*'):  # [!.]* - шаблон, игнорирует скрытые файлы, начинающиеся с точки
        if file_path.is_file():
            logger.info(f"Processing file: {file_path}")
            task = asyncio.create_task(process_file(file_path))
            tasks.append(task)
        elif file_path.is_dir():
            logger.info(f"Processing directory: {file_path}")
            task = asyncio.create_task(process_directory(file_path))
            tasks.append(task)

        await asyncio.gather(*tasks)


async def main() -> None:
    start_time = time.time()

    directory_path = Path('..')
    await process_directory(directory_path)

    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f'Time taken: {elapsed_time:.2f} seconds')


if __name__ == '__main__':
    asyncio.run(main())
