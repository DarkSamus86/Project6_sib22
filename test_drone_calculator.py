import unittest
from calculate_data import calculate_total_mass
from output_data import save_report
from data_storage import save_to_json, load_from_json

class TestDroneCalculator(unittest.TestCase):
    def setUp(self):
        """
        Устанавливаем тестовые данные перед запуском каждого теста.
        """
        self.test_weights = {
            "корпус": 1200,
            "двигатели": 800,
            "аккумуляторы": 1000
        }
        self.payload_mass = 500
        self.test_file = "test_report.txt"
        self.test_json_file = "test_drone_data.json"

    def test_calculate_total_mass(self):
        """
        Тестирует функцию calculate_total_mass.
        """
        # Правильный расчет общей массы с учетом коэффициентов и массы топлива
        expected_mass = (1200 * 0.95) + (800 * 0.90) + (1000 * 0.85) + self.payload_mass + (1000 * 0.02)
        result = calculate_total_mass(self.test_weights, payload_mass=self.payload_mass)
        self.assertEqual(result, expected_mass, "Общая масса рассчитана неверно.")

    def test_save_to_json_and_load_from_json(self):
        """
        Тестирует функции сохранения и загрузки JSON.
        """
        save_to_json(self.test_weights)  # Сохраняем тестовые данные
        loaded_data = load_from_json()  # Загружаем их обратно
        self.assertEqual(self.test_weights, loaded_data, "Сохранённые и загруженные данные не совпадают.")

    def test_save_report(self):
        """
        Тестирует функцию сохранения текстового отчёта.
        """
        total_mass = calculate_total_mass(self.test_weights, payload_mass=self.payload_mass)
        save_report(self.test_weights, total_mass, filename=self.test_file)

        # Проверяем, что файл успешно создан
        with open(self.test_file, "r", encoding="utf-8") as file:
            content = file.read()
        expected_content = (
            "Отчёт о массе дрона\n"
            "--------------------\n"
            "Корпус: 1200 г\n"
            "Двигатели: 800 г\n"
            "Аккумуляторы: 1000 г\n"
            f"Общая масса: {total_mass} г\n"
        )
        self.assertEqual(content, expected_content, "Содержимое отчёта некорректно.")

    def tearDown(self):
        """
        Удаляем тестовые файлы после завершения каждого теста.
        """
        import os
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.test_json_file):
            os.remove(self.test_json_file)

if __name__ == "__main__":
    unittest.main()
