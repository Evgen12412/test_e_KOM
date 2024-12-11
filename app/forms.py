from validators import validate_field


def get_form_template(db, data):
    templates = db.all()
    for template in templates:
        if all(field in data and validate_field(data[field]) == template[field] for field in template if
               field != "name"):
            return template["name"]
    return None
