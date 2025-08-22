# Когда НЕ использовать Session()

- Одиночные запросы - если делаете всего 1-2 запроса

- К разным доменам - если запросы к совершенно разным API

- Очень редкие запросы - если между запросами большие паузы

# Best Practices

- Всегда используйте контекстный менеджер

- Настраивайте таймауты

- Добавляйте User-Agent

- Обрабатывайте ошибки

- Закрывайте сессию явно при долгоживущих объектах

```py

# Идеальный шаблон
def make_requests():
    with requests.Session() as session:
        session.timeout = 10
        session.headers.update({'User-Agent': 'MyApp/1.0'})

        try:
            response = session.get('https://api.example.com/data')
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None
```

```py
# Проверяем производительность

import time

# Без сессии
start = time.time()
for i in range(10):
    requests.get('https://httpbin.org/get')
print(f"Без сессии: {time.time() - start:.2f} сек.")

# С сессией
start = time.time()
with requests.Session() as session:
    for i in range(10):
        session.get('https://httpbin.org/get')
print(f"С сессией: {time.time() - start:.2f} сек.")
```
