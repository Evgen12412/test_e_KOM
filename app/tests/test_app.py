import sys
import os
import unittest

# Добавляем корневую директорию проекта в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app  # Абсолютный импорт


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_form(self):
        response = self.app.post('/get_form', data={'f_name1': 'test@example.com', 'f_name2': '+7 123 456 78 90'})
        self.assertEqual(response.status_code, 200)

        # Проверяем, что шаблон формы найден
        if response.json.get("form_name"):
            self.assertEqual(response.json, {"form_name": "TestForm"})
        else:
            self.assertEqual(response.json, {"f_name1": "email", "f_name2": "phone"})


if __name__ == '__main__':
    unittest.main()
