import numpy as np

L = [1, 2, 3, 4, 5]

print("Все элементы списка L:")
for item in L:
    print(item)

print("Логарифмированные значения элементов списка L:")
for item in L:
    print(np.log(item))

L[4] = 0

print("Все элементы списка L после замены пятого элемента на 0:")
for item in L:
    print(item)

print("Логарифмированные значения элементов списка L после замены:")
for item in L:
    try:
        print(np.log(item))
    except ValueError as e:
        print("Ошибка:", e)
