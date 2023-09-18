fio = input("Введите Ваши ФИО: ")

parts = fio.split()

if len(parts) == 3:
    last_name, name, otch = parts[0], parts[1], parts[2]

    print("Ваша фамилия:", last_name)
    print("Ваше имя:", name)
    print("Ваше отчество:", otch)
else:
    print("Вы ввели неверное количество частей ФИО")


input_string = "1; 2; 3; 100"

elements = input_string.split(";")

integer_list = []
float_list = []

for element in elements:
    element = element.strip()
    try:
        integer_value = int(element)
        integer_list.append(integer_value)
    except ValueError:
        try:
            float_value = float(element)
            float_list.append(float_value)
        except ValueError:
            continue

print("Список из целых чисел:", integer_list)
print("Список из чисел с плавающей точкой:", float_list)


phone_number = input("Введите номер мобильного телефона: ")
cleaned_phone_number = phone_number.replace("-", "").replace(" ", "")
print("Очищенный номер:", cleaned_phone_number)


import math
L = [1000, 2000, 3000, 4000, 5000]
L2 = []

for income in L:
    log_income = math.log(income)
    L2.append(log_income)

print("Список логарифмированных значений доходов:", L2)


words = ["Speak ", "to", "me ", "of", "Florence", "And ", "of", "the", "Renaissance"]
words_clean = []

for word in words:
    cleaned_word = word.strip().lower()

    words_clean.append(cleaned_word)

print("Очищенный список слов:", words_clean)

