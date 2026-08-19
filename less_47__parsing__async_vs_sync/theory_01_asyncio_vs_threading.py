"""
https://it4each.com/blog/threading-multiprocessing-i-asyncio-v-python-chast-2/
"""


import requests
import threading
import time

URLS = [
    "https://example.com",
    "https://wikipedia.org",
    "https://google.com",
    # ...
] * 10

# ======================================================
# Синхронно
# ======================================================

print("=== Синхронные запросы ==================================")
start = time.perf_counter()

results = []

for url in URLS:
    try:
        response = requests.get(url, timeout=10)
        results.append(response.status_code)
    except requests.RequestException:
        results.append(None)

elapsed = time.perf_counter() - start

print(f"Сайтов: {len(URLS)}")
print(f"Время: {elapsed:.2f} сек")
print(f"Успешно: {sum(x is not None for x in results)}")


print("=== Асинхронные запросы =================================")
# ======================================================
# asyncio
# ======================================================
import asyncio
import aiohttp

async def check_async(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            return response.status

    except (aiohttp.ClientError, asyncio.TimeoutError):
        return None


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [
            check_async(session, url)
            for url in URLS
        ]

        return await asyncio.gather(*tasks)


print("\n--- Запускаем asyncio --------------------------------")
results = []

start = time.perf_counter()

results_async = asyncio.run(main())

elapsed = time.perf_counter() - start

print(f"Сайтов: {len(URLS)}")
print(f"Время: {elapsed:.2f} сек")
print(f"Успешно: {sum(x is not None for x in results_async)}")

# ======================================================
# Потоки
# ======================================================
def check(url):
    try:
        response = requests.get(url, timeout=10)
        results.append(response.status_code)
    except requests.RequestException:
        results.append(None)

print("--- Запускаем потоки ---------------------------------")
start = time.perf_counter()

threads = []

for url in URLS:
    thread = threading.Thread(target=check, args=(url,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

elapsed = time.perf_counter() - start


print(f"Сайтов: {len(URLS)}")
print(f"Время: {elapsed:.2f} сек")
print(f"Успешно: {sum(x is not None for x in results)}")


"""
=================================================
 сайтов     синхронно   asyncio    threading
-------------------------------------------------
   30         6.57        0.69        0.57
  300        73.26        3.84        5.53
=================================================
"""