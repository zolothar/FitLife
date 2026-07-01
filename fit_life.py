# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
ML_PER_L = 1000


def calculate_bmi(weight, height):
    """Calculate body mass index."""
    bmi = weight / (height ** 2)
    return round(bmi, 1)


def calculate_water_norm(weight):
    """Calculate water consumption rates."""
    water = weight * WATER_PER_KG / ML_PER_L
    return round(water, 2)


def main():
    """Run FitLife application."""
    user_name = input("Введите ваше имя: ")

    try:
        user_age = int(input("Введите ваш возраст: "))
        user_weight = float(
            input("Введите ваш вес в килограммах (например 75.5): "))
        user_height = float(
            input("Введите ваш рост в метрах (например 1.75): "))
    except ValueError:
        print("Вы ввели не число!")
        return

    bmi = calculate_bmi(user_weight, user_height)
    water_norm = calculate_water_norm(user_weight)

    print(f"Отчет для пользователя {user_name}, возраст {user_age}",
          f"Ваш Индекс Массы Тела: {bmi}",
          f"Рекомендуемая норма воды: {water_norm:.1f} л. в день",
          "Расчет окончен. Будьте здоровы!",
          sep="\n")


if __name__ == "__main__":
    main()
