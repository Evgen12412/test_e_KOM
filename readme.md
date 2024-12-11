# Приложение для определения шаблонов форм

Это приложение на Flask, которое позволяет определять шаблоны форм на основе входных данных. Оно использует базу данных TinyDB для хранения шаблонов форм и предоставляет REST API для взаимодействия с приложением.

## Установка и запуск

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/Evgen12412/test_e_KOM.git
   cd test_e_KOM
   ```

2. **Установите зависимости:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Запустите приложение:**

   ```bash
   python app.py
   ```

   Приложение будет доступно по адресу `http://0.0.0.0:5000`.

## Структура проекта

- `app.py`: Основной файл приложения Flask.
- `db.py`: Модуль для работы с базой данных TinyDB.
- `validators.py`: Модуль для валидации полей.
- `forms.py`: Модуль для работы с шаблонами форм.
- `db.json`: Файл базы данных TinyDB.

## API

### POST `/get_form`

Этот эндпоинт принимает данные формы в формате `application/x-www-form-urlencoded` и возвращает имя шаблона формы, если он найден, или типы полей, если шаблон не найден.

#### Пример запроса

```bash
curl -X POST -d "field1=value1&field2=value2" http://0.0.0.0:5000/get_form
```

#### Пример ответа

Если шаблон найден:

```json
{
  "form_name": "example_form"
}
```

Если шаблон не найден:

```json
{
  "field1": "text",
  "field2": "date"
}
```

## Валидация полей

Приложение поддерживает следующие типы полей:

- **phone**: Номер телефона в формате `+7 xxx xxx xx xx`.
- **date**: Дата в формате `DD.MM.YYYY` или `YYYY-MM-DD`.
- **email**: Адрес электронной почты.
- **text**: Любое другое значение.

## База данных

База данных TinyDB хранит шаблоны форм в формате JSON. Каждый шаблон содержит имя формы и набор полей с их типами.

Пример структуры базы данных:

```json
[
  {
    "name": "example_form",
    "field1": "text",
    "field2": "date"
  }
]
```

## Тестирование

Для тестирования приложения можно использовать инструменты, такие как `curl` или Postman.

## Лицензия

Этот проект лицензирован под MIT License. Подробности смотрите в файле `LICENSE`.

## Контакты

Если у вас есть вопросы или предложения, пожалуйста, свяжитесь со мной по адресу `hh_search_job@mail.ru`.