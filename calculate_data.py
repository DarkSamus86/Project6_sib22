def calculate_total_mass(weights, payload_mass=500, fuel_rate_per_gram=0.02, efficiency_coefficients=None):
    """
    Рассчитывает общую массу дрона с учётом коэффициентов эффективности и массы топлива.
    :param weights: словарь с массами частей
    :param payload_mass: масса полезной нагрузки (по умолчанию 500 г)
    :param fuel_rate_per_gram: коэффициент топлива на каждый грамм аккумуляторов (по умолчанию 0.02)
    :param efficiency_coefficients: словарь с коэффициентами эффективности для каждой части (по умолчанию None)
    :return: итоговая масса
    """
    if efficiency_coefficients is None:
        efficiency_coefficients = {
            "корпус": 0.95,
            "двигатели": 0.90,
            "аккумуляторы": 0.85
        }

    # Применяем коэффициенты эффективности для каждой части
    adjusted_weights = {}
    for part, weight in weights.items():
        if part in efficiency_coefficients:
            adjusted_weights[part] = weight * efficiency_coefficients[part]
        else:
            adjusted_weights[part] = weight

    # Добавляем массу топлива (рассчитывается по аккумуляторам)
    fuel_mass = weights.get("аккумуляторы", 0) * fuel_rate_per_gram

    # Рассчитываем итоговую массу
    total_mass = sum(adjusted_weights.values()) + payload_mass + fuel_mass

    return total_mass