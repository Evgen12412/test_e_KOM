from flask import Flask, request, jsonify

from validators import validate_field
from db import get_db, close_db
from forms import get_form_template

app = Flask(__name__)


@app.route('/get_form', methods=['POST'])
def get_form():
    data = request.form.to_dict()
    db = get_db()
    form_name = get_form_template(db, data)
    close_db()

    if form_name:
        return jsonify({"form_name": form_name})
    else:
        field_types = {field: validate_field(value) for field, value in data.items()}
        return jsonify(field_types)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
