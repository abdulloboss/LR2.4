lst = [float(x) for x in input("Введите элементы списка через пробел: ").split()]

sum_positive = 0
max_mod_index = 0
min_mod_index = 0

for i in range(len(lst)):
    if lst[i] > 0:
        sum_positive += lst[i]
    if abs(lst[i]) > abs(lst[max_mod_index]):
        max_mod_index = i
    if abs(lst[i]) < abs(lst[min_mod_index]):
        min_mod_index = i


product_between_max_min = 1

if max_mod_index < min_mod_index:
    start = max_mod_index + 1
    end = min_mod_index
else:
    start = min_mod_index + 1
    end = max_mod_index

for i in range(start, end):
    product_between_max_min *= lst[i]

print("Сумма положительных элементов:", sum_positive)
print("Произведение элементов между максимальным и минимальным по модулю:", product_between_max_min)
