# first code
day = int(input("Введите номер дня: "))
minutes = 1 + 3 * (day - 1)
print(f"В {day}-й день питон проведет {minutes} минут на солнце")

#second code
name = input("Введите ваше имя: ")
last_name = input("Введите вашу фамилию: ")
print(f"{name} {last_name}, добро пожаловать!")

#third code
first_kurs = input("Введите название первого курса: ")
second_kurs = input("Введите название второго курса: ")
third_kurs = input("Введите название третьего курса: ")

resept = f"Рецепт\n{first_kurs} : 200 г\n{second_kurs} : 300 г\n{third_kurs} : 100 г\nПриправить политической историей. Добавить математические модели по вкусу."

print(resept)

#fourth code
first_mass_g = float(input("Введите массу первого ингредиента в граммах: "))
second_mass_g = float(input("Введите массу второго ингредиента в граммах: "))
third_mass_g = float(input("Введите массу третьего ингредиента в граммах: "))

first_mass_kg = round(first_mass_g / 1000, 3)
second_mass_kg = round(second_mass_g / 1000, 3)
third_mass_kg = round(third_mass_g / 1000, 3)

resept_k = f"Рецепт\nполитическая теория : {first_mass_kg:.3f} кг\nистория политических учений: {second_mass_kg:.3f} кг\nматематика: {third_mass_kg:.3f} кг\nПриправить политической историей. Добавить математические модели по вкусу."

print(resept_k)
