## Первый запуск:

Создать виртуальную среду:
``` bash
virtualenv -p /usr/bin/python2.7 venv
source venv/bin/activate
```

Установить зависимости:
```bash
pip install -r requirements.txt
```

## Парсинг
```bash
scrapy crawl goods
```
В результате появится файл results_{today_date}.json