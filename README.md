# Асинхронный веб сервер

Python + Aiohttp \
Веб сервер который последовательно выполняет задачи за указанное количество секунд и сохраняет 
результат выполнения задачи. Запускается в один процесс.
## Запуск для разработки

```sh
# Создаем виртуальное окружения
$ python3 -m venv venv
$ . ./venv/bin/activate

# Загружаем зависимости
$ pip install -r requirements.txt

# Запускаем приложение
$ python main.py
```

### Используемые технологии

- [Aiohttp](https://docs.aiohttp.org/en/latest/index.html) - асинхронный HTTP сервер/клиент на 
  основе [Asyncio](https://docs.aiohttp.org/en/latest/glossary.html#term-asyncio) и Python.

## Документация REST API

***
#### Оглавление
- Поддерживаемый функционал
- Примеры запросов
***
### Поддерживаемый функционал
При создании задания передаются следующие параметры: num - число задания, timeout - время выполнения задания.
Задачи выполняются последовательно, задача выполняется в течении указанного timeout (сек).

Далее перечислены варианты использования методов
бэкенда.

- Создание задания
- Просмотр результатов задания
- Получение списка заданий в работе
***
### Примеры использования
Обмен данными происходит через `x-www-form-urlencoded`.

Далее перечислены конкретные примеры запросов,
указанных выше.
***
### Создание задания
- Запрос POST /task
```json
{
    "num": 1,
    "timeout": 13
}
```
- Ответ
```json
{
  "detail": "created"
}
```
***
### Получение списка заданий в работе
- Запрос GET /task
- Ответ
```json
[
    {
        "date_created": "2021-04-03 16:49:08.572279",
        "index_num": 0,
        "num": 1,
        "timeout": 13
    },
    {
        "date_created": "2021-04-03 16:49:08.946933",
        "index_num": 0,
        "num": 1,
        "timeout": 13
    }
]
```
***
### Получение списка выполненных заданий
- Запрос GET /result
- Ответ
```json
[
    {
        "num": 1
    },
    {
        "num": 1
    }
]
```