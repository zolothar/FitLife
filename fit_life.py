# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
ML_PER_L = 1000

user_name = input("Введите ваше имя: ")

try:
    user_age = int(input("Ввдите ваш возраст: "))
    user_weight = float(
        input("Введите ваш вес в килограммах (например 75.5): "))
    user_height = float(input("Введите ваш рост в метрах (например 1.75): "))
except ValueError:
    print("Вы ввели не число!")
    exit()


def calculate_bmi(weight, height):
    """Calculating body mass index"""
    bmi = weight / (height ** 2)
    return round(bmi, 1)


bmi = calculate_bmi(user_weight, user_height)


def calculate_water_norm(weight):
    """Calculating water consumption rates"""
    water = weight * WATER_PER_KG / ML_PER_L
    return round(water, 2)


water_norm = calculate_water_norm(user_weight)

print(f"Отчет для пользователя {user_name}")
print(f"Ваш Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_norm} л. в день")
print("Расчет окончен. Будьте здоровы!")
