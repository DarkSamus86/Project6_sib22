import matplotlib.pyplot as plt

def save_report(weights, total_mass, filename="report.txt"):
    """
    Сохраняет текстовый отчёт о массе дрона в файл.
    :param weights: словарь с массами частей
    :param total_mass: итоговая масса
    :param filename: имя файла для сохранения отчёта
    """
    with open(filename, "w", encoding='utf-8') as file:
        file.write("Отчёт о массе дрона\n")
        file.write("--------------------\n")
        for part, weight in weights.items():
            file.write(f"{part.capitalize()}: {weight} г\n")
        file.write(f"Общая масса: {total_mass} г\n")
    print(f"Отчёт сохранён в файл: {filename}")


def plot_mass_distribution(weights):
    """
    Строит диаграмму распределения массы частей.
    :param weights: словарь с массами частей
    """
    labels = list(weights.keys())
    values = list(weights.values())

    plt.figure(figsize=(8, 6))
    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("Распределение массы частей дрона")
    plt.show()