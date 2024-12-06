import json
import os

DATA_FILE = 'drone_data.json'

def save_to_json(data):
    """
    Сохраняет данные в JSON файл.
    :param data: словарь с данными
    """
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"Данные сохранены в файл {DATA_FILE}.")

def load_from_json():
    """
    Загружает данные из JSON файла, если он существует.
    :return: словарь с данными или пустой словарь
    """
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                print("Ошибка: файл повреждён. Данные не загружены.")

    return {}