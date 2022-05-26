# Как запустить


## Установка:

``` bash
git clone https://github.com/fnceba/street-beat-parser
cd street-beat-parser
```

Создать виртуальную среду:
``` bash
virtualenv -p $(which python2.7) venv
source venv/bin/activate
```

Установить зависимости:
```bash
pip install -r requirements.txt
```

## Парсинг:
```bash
scrapy crawl goods -t json --nolog -o - > results.json
```
