import re
from datetime import datetime


def validate_field(value):
    """
        Определяет тип поля на основе его значения.
        Поддерживаемые типы: phone, date, email, text.
        :param value: Значение поля.
        :return: Тип поля.
    """
    # Проверка на телефонный номер
    if re.match(r'^\+7 \d{3} \d{3} \d{2} \d{2}$', value):
        return "phone"
    # Проверка на дату в формате DD.MM.YYYY или YYYY-MM-DD
    elif re.match(r'^\d{2}\.\d{2}\.\d{4}$', value) or re.match(r'^\d{4}-\d{2}-\d{2}$', value):
        try:
            datetime.strptime(value, '%d.%m.%Y')
            return "date"
        except ValueError:
            try:
                datetime.strptime(value, '%Y-%m-%d')
                return "date"
            except ValueError:
                pass
    # Проверка на email
    elif re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value):
        return "email"
    else:
        # Если ничего не подошло, возвращаем тип "text"
        return "text"
