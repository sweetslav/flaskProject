# Задание №9.
# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск.
# Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения.
# Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# Программа должна использовать синхронный подход.
# Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# Программа должна выводить информацию о времени скачивания каждого изображения и общем времени выполнения программы.

import logging
import time

import requests

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='images_sync.log',
    filemode='w')

logger = logging.getLogger(__name__)


def download_file(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем наличие ошибок
        return response.content
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to download file from {url}: {e}")
        return None


def time_for_download(urls):
    start_time = time.time()
    elapsed_time = 0
    for url in urls:
        file_content = download_file(url)
        if file_content:
            file_name = url.split('/')[-1][:50]  # Получаем имя файла (не более 50 символов)
            with open(file_name, 'wb') as file:
                file.write(file_content)
                elapsed_time = time.time() - start_time
                logger.info(f'The file {file_name} from {url} was uploaded in {elapsed_time:.2f} seconds.')
    return elapsed_time


if __name__ == '__main__':
    links = [
        'https://images.freeimages.com/images/large-previews/c15/texture-1186115.jpg',
        'https://images.freeimages.com/images/large-previews/774/animal-1372311.jpg',
        'https://images.freeimages.com/images/large-previews/ba3/animal-1405602.jpg',
        'https://images.freeimages.com/images/large-previews/2ef/wild-animal-1376626.jpg',
        'https://images.freeimages.com/images/large-previews/972/animal-textures-1180974.jpg']

    result_time = time_for_download(links)
    logger.info(f'Finish. Time taken: {result_time:.2f} seconds')
