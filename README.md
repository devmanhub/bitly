# Обрезка ссылок с помощью Битли

Данный проект помогает работать с сокращением ссылок при помощи сервиса bitly. Вы можете делать свои собственные сокращенные ссылки, для этого в аргумент команды вставьте ссылку, на которую хотите получить битлинк или же узнать количество переходов по вашим битлинкам, для этого просто вставьте ваш битлинк на место ссылки.

### Как установить

Python3 должен быть уже установлен. Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Чтобы запустить программу, вам нужно зарегестрироваться на [сайте](https://bitly.com/) и получить там токен, затем создать в папке проекта создать файл .env в котором записать BITLY_TOKEN=Bearer сюда вставить ваш токен. Создать файл .env можно при помощи [notepad++](https://notepad-plus-plus.org/).

Пример запуска программы:

```
python main.py https://bit.ly/411AnCN
```

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html)

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://vmn.org/).
