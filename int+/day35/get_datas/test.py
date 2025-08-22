import time

import requests

# Без сессии
start = time.time()
for i in range(10):
    requests.get('https://httpbin.org/get')
print(f"Без сессии: {time.time() - start:.2f} сек.") # Без сессии: 13.35 сек.

# С сессией
start = time.time()
with requests.Session() as session:
    for i in range(10):
        session.get('https://httpbin.org/get')
print(f"С сессией: {time.time() - start:.2f} сек.") # С сессией: 5.94 сек.