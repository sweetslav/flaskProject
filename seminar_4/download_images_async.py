# Программа скачивает изображения с заданных URL-адресов и сохраняет их на диск.
# Она использует асинхронный подход для повышения эффективности работы.
# Каждое изображение сохраняется в отдельном файле с названием, соответствующим его исходному названию.
# Например, если URL-адрес имеет вид https://example/images/image1.jpg, то изображение сохранится в файле image1.jpg.
# Программа выводит информацию о времени скачивания каждого изображения и общем времени выполнения программы,
# что позволяет пользователю отслеживать процесс загрузки и оценить скорость выполнения.

import asyncio
import logging
import time

import aiohttp

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='images_async.log',
    filemode='w')

logger = logging.getLogger(__name__)


async def download_file(url):
    """ Загружает содержимое файла по-указанному URL-адресу. """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()  # Проверяем наличие ошибок
                content = await response.read()
                filename = url.split('/')[-1][:50]
                return content, filename
    except aiohttp.ClientError as e:
        logger.error(f"Failed to download file from {url}: {e}")
        return None, None


async def download_and_save_image(url):
    """ Загружает изображение по-указанному URL-адресу и сохраняет его на диск. """
    file_content, file_name = await download_file(url)
    if file_content and file_name:
        start_time = time.time()
        with open(file_name, 'wb') as file:
            file.write(file_content)
            elapsed_time = time.time() - start_time
            logger.info(f'The file {file_name} from {url} was uploaded in {elapsed_time:.2f} seconds.')
            print(f'The file {file_name} from {url} was uploaded in {elapsed_time:.2f} seconds.')


async def time_for_download(urls):
    """ Загружает изображения с нескольких URL-адресов параллельно и измеряет общее время выполнения. """
    start_time = time.time()
    tasks = []
    for url in urls:
        task = asyncio.create_task(download_and_save_image(url))
        tasks.append(task)
    await asyncio.gather(*tasks)
    elapsed_time = time.time() - start_time
    return elapsed_time


if __name__ == '__main__':
    links = [
        'https://images.freeimages.com/images/large-previews/c15/texture-1186115.jpg',
        'https://images.freeimages.com/images/large-previews/774/animal-1372311.jpg',
        'https://images.freeimages.com/images/large-previews/ba3/animal-1405602.jpg',
        'https://images.freeimages.com/images/large-previews/2ef/wild-animal-1376626.jpg',
        'https://images.freeimages.com/images/large-previews/972/animal-textures-1180974.jpg']

    loop = asyncio.get_event_loop()
    result_time = loop.run_until_complete(time_for_download(links))
    logger.info(f'Finish. Time taken: {result_time:.2f} seconds')
    print(f'Total time taken: {result_time:.2f} seconds')
