# Инициализируем список A
A = []

# Вводим 10 элементов списка
for i in range(10):
    element = float(input(f"Введите {i + 1}-й элемент списка: "))
    A.append(element)

# Инициализируем переменную для хранения произведения положительных элементов
product = 1

# Вычисляем произведение положительных элементов
for element in A:
    if element > 0:
        product *= element

# Выводим произведение положительных элементов
print("Произведение положительных элементов списка A:", product)
