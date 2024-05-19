"""
Завдання 3: Асинхронне програмування
Напишіть асинхронну функцію, яка виконує кілька HTTP-запитів до різних URL-адрес і повертає їх результати.
Використовуйте бібліотеку `aiohttp`.
"""
import aiohttp
import asyncio


async def fetch_url(session, url):
    """
    Асинхронно виконує HTTP-запит і повертає результат.
    :param session: об'єкт сесії aiohttp
    :param url: URL-адреса
    :return: результат запиту
    """
    async with session.get(url) as response:
        return await response.text()


async def fetch_all(urls):
    """
    Асинхронно виконує HTTP-запити до всіх URL-адрес і повертає їх результати.
    :param urls: список URL-адрес
    :return: результати запитів
    """
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        return await asyncio.gather(*tasks)

# Приклад використання:
urls = ['http://example.com', 'http://example.org']
results = asyncio.run(fetch_all(urls))
print(results)
