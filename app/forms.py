from validators import validate_field


def get_form_template(db, data):
    """
        Ищет подходящий шаблон формы в базе данных.
        :param db: Объект базы данных TinyDB.
        :param data: Словарь с данными формы.
        :return: Имя шаблона формы, если найден, иначе None.
    """
    # Получаем все шаблоны форм из базы данных
    templates = db.all()
    for template in templates:
        # Проверяем, совпадают ли все поля шаблона с данными формы
        if all(field in data and validate_field(data[field]) == template[field] for field in template if
               field != "name"):
            return template["name"]
    return None
