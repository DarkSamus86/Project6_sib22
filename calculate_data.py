def calculate_total_mass(weights, payload_mass=500):
    """
    Рассчитывает общую массу дрона.
    :param weights: словарь с массами частей
    :param payload_mass: масса полезной нагрузки (по умолчанию 500 г)
    :return: итоговая масса
    """

    total_mass = sum(weights.values()) + payload_mass
    return total_mass