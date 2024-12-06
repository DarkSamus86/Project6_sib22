from data_storage import save_to_json, load_from_json

def get_part_weights():
    """
    Получение массы частей дрона от пользователя или из сохранённого JSON файла.
    :return: словарь с массами частей
    """
    existing_data = load_from_json()
    if existing_data:
        print("Найдены сохранённые данные:")
        for part, weight in existing_data.items():
            print(f"{part.capitalize()}: {weight} г")

        use_existing = input("Использовать эти данные? (да/нет): ").strip().lower()
        if use_existing == "да":
            return existing_data

    print("Введите массу частей дрона (в граммах):")
    parts = ["корпус", "двигатели", "аккумуляторы"]
    weights = {}
    for part in parts:
        while True:
            try:
                weight = float(input(f"Масса {part}: "))
                if weight < 0:
                    raise ValueError("Масса не может быть отрицательной!")
                weights[part] = weight
                break
            except ValueError as e:
                print(f"Ошибка: {e}. Повторите ввод.")

    save_to_json(weights)
    return weights