numbers = [1, 5, 6, 8, 10, 21, 25, 1, 0, -9, 9]

user_input = input("Введите целое число от 1 до 10: ")

user_number = int(user_input)
if 1 <= user_number <= 10:
    result = numbers[user_number - 1]
    print(result)
else:
    print("Error, enter correct number in range from 1 to 10")
