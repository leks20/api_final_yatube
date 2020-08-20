
# API_Yatube

REST API для социальной сети блогеров [Yatube](https://blog-yatube.tk), созданной в рамках учебного курса Яндекс.Практикум

Аутентификация по JWT-токену

Работает со всеми модулями социальной сети Yatube: постами, комментариями, группами, подписчиками

Поддерживает методы GET, POST, PUT, PATCH, DELETE

Предоставляет данные в формате JSON

## Стек технологий
- проект написан на Python с использованием Django REST Framework
- библиотека Simple JWT - работа с JWT-токеном
- система управления версиями - git

## Как запустить проект:

1) Клонируйте репозитроий с проектом:
```
git clone https://github.com/leks20/api_yatube
```
2) В созданной директории установите виртуальное окружение, активируйте его и установите необходимые зависимости:
```
python3 -m venv venv

. venv/bin/activate

pip install -r requirements.txt
```
3) Создайте в директории файл .env и поместите туда SECRET_KEY, необходимый для запуска проекта:
   - сгенерировать ключ можно на сайте [Djecrety](https://djecrety.ir/)

4) Выполните миграции:
```
python manage.py migrate
```
5) Создайте суперпользователя:
```
python manage.py createsuperuser
```
6) Запустите сервер:
```
python manage.py runserver
```
____________________________________

Ваш проект запустился на http://127.0.0.1:8000/

Полная документация ([redoc.yaml](https://github.com/leks20/api_yatube/blob/master/static/redoc.yaml)) доступна по адресу http://localhost:8000/redoc/

С помощью команды *pytest* вы можете запустить тесты и проверить работу модулей

## Аутентификация

Выполните POST-запрос *localhost:8000/api/v1/token/* передав поля username и password.

API вернет JWT-токен в формате:

    {
        "refresh": "ХХХХХХХХХХХ",
        "access": "ХХХХХХХХХХХХ"
    }
    
Токен вернётся в поле access, а данные из поля refresh нужны для обновления токена

При отправке запроcов передавайте токен в заголовке Authorization: Bearer <токен>

## Как работает API_Yatube

##### Пример http-запроса (POST) для создания поста:
```
url = 'http://127.0.0.1/api/v1/posts/'
data = {'text': 'Your post'}
headers = {'Authorization': 'Bearer your_token'}
request = requests.post(url, data=data, headers=headers)
```
##### Ответ API_Yatube:
```
Статус- код 200

{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2020-08-20T14:15:22Z"
}
```
_____________________________________________
##### Пример http-запроса (GET) для получения списка подписчиков:
```
url = 'http://127.0.0.1:8000/api/v1/follow/'
headers = {'Authorization': 'Bearer your_token'}
request = requests.get(api, headers=headers)
```
##### Ответ API_Yatube:
```
Статус- код 200

[
  {
    "user": "string",
    "following": "string"
  }
]
```
