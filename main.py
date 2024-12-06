from input_data import get_part_weights
from calculate_data import calculate_total_mass
from output_data import save_report, plot_mass_distribution

def main():
    """
    Основной модуль программы. Управляет процессом ввода, расчёта и вывода данных.
    """
    weights = get_part_weights()
    total_mass = calculate_total_mass(weights)
    save_report(weights, total_mass)
    plot_mass_distribution(weights)

if __name__ == "__main__":
    main()