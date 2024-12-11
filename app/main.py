from flask import Flask, request, jsonify

from validators import validate_field
from db import get_db, close_db
from forms import get_form_template

app = Flask(__name__)


@app.route('/get_form', methods=['POST'])
def get_form():
    """
       Эндпоинт для определения шаблона формы.
       Принимает данные формы в формате application/x-www-form-urlencoded.
       Возвращает имя шаблона формы, если он найден, или типы полей, если шаблон не найден.
    """

    # Преобразуем данные формы в словарь
    data = request.form.to_dict()
    # Получаем объект базы данных
    db = get_db()
    # Ищем подходящий шаблон формы
    form_name = get_form_template(db, data)
    # Закрываем соединение с базой данных
    close_db()
    # Если шаблон найден, возвращаем его имя
    if form_name:
        return jsonify({"form_name": form_name})
    else:
        # Если шаблон не найден, возвращаем типы полей
        field_types = {field: validate_field(value) for field, value in data.items()}
        return jsonify(field_types)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
