# Проект FitLife - MVP версия 1.0
import constants


# 1. Знакомство
print("Добрый день!")
user_name = str(input("Как вас зовут? "))
user_age = int(input("Сколько вам лет? "))


# 2. Сбор данных вес и рост
user_weight = float(input("Какой вес у вас на сегодня? "))
user_height = float(input("Какой рост у вас на сегодня? "))

# Рассчитай bmi (Индекс массы тела)
bmi = user_weight / (user_height ** 2)

# Подсчет воды: вес * 30 мл
# Рассчитай water_needed
water_ml = user_weight * constants.WATER_PER_KG
water_l = water_ml / 1000

# 4. Вывод красивого результата
# Используй f-строку, чтобы вывести приветствие, например: "Привет, Иван!"
# Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.
print(f"Добрый день, {user_name}.")
print("Твой Индекс Массы Тела ", round(bmi, 1))
print("Рекомендуемая норма воды ", round(water_l, 1), "л. в день")
print()
print("Расчет окончен. Будьте здоровы!")
