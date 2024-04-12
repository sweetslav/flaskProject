# Программа скачивает изображения с заданных URL-адресов и сохраняет их на диск.
# Она использует многопроцессорный подход для повышения эффективности работы.
# Каждое изображение сохраняется в отдельном файле с названием, соответствующим его исходному названию.
# Например, если URL-адрес имеет вид https://example/images/image1.jpg, то изображение сохранится в файле image1.jpg.
# Программа выводит информацию о времени скачивания каждого изображения и общем времени выполнения программы,
# что позволяет пользователю отслеживать процесс загрузки и оценить скорость выполнения.

import logging
import time
from concurrent.futures import ProcessPoolExecutor

import requests

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='images_multiprocess.log',
    filemode='a')  # Обязательно ставим режим дополнения файла

logger = logging.getLogger(__name__)


def download_file(url):
    """ Загружает содержимое файла по-указанному URL-адресу. """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем наличие ошибок
        return response.content, url.split('/')[-1][:50]
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to download file from {url}: {e}")
        return None, None


def download_and_save_image(url):
    """ Загружает изображение по-указанному URL-адресу и сохраняет его на диск. """
    file_content, file_name = download_file(url)
    if file_content and file_name:
        start_time = time.time()
        with open(file_name, 'wb') as file:
            file.write(file_content)
            elapsed_time = time.time() - start_time
            logger.info(f'The file {file_name} from {url} was uploaded in {elapsed_time:.2f} seconds.')
            print(f'The file {file_name} from {url} was uploaded in {elapsed_time:.2f} seconds.')


def time_for_download(urls):
    """ Загружает изображения с нескольких URL-адресов параллельно и измеряет общее время выполнения. """
    start_time = time.time()
    with ProcessPoolExecutor() as executor:  # По умолчанию используется количество доступных процессоров
        executor.map(download_and_save_image, urls)
    elapsed_time = time.time() - start_time
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
    print(f'Total time taken: {result_time:.2f} seconds')
