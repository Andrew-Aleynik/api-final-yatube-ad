# API Yatube

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Andrew-Aleynik/api-final-yatube-ad
```

```
cd api-final-yatube-ad
```

Cоздать и активировать виртуальное окружение (рекомендуемая версия pyhon 3.10):

```
python3.X -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Сменить директорию на yatube_api

```
cd yatube_api
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
