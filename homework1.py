# Задача 2: Найдите сумму цифр трехзначного числа
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int (input('трехзначное число: '))
n = str(n)
print(f'сумма цифр трехзначного числа {int (n[0])+ int(n[1]) + int(n[2])}')