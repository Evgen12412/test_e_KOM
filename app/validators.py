import re
from datetime import datetime

def validate_field(value):
    if re.match(r'^\+7 \d{3} \d{3} \d{2} \d{2}$', value):
        return "phone"
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
    elif re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value):
        return "email"
    else:
        return "text"