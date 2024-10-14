# Импортирование функций из библиотеки math
from math import log, sqrt, atan, cos, sin, tan, pi, e, exp

# Ввод переменных
x = float(input("Введите переменную x: "))
y = float(input("Введите переменную y: "))
z = float(input("Введите переменную z: "))

# Нахождение значений функций и их вывод

# Функция k
if (z + x**2 / 4) != 0:
    k = log(abs((y - sqrt(abs(x))) * (x - y / (z + x**2 / 4))))
    print(f"k = {round(k, 2)}")
else:
    print("Нельзя делить на ноль!")

# Функция d
if 0.5 + sin(y) ** 2 != 0:
    d = 2 * cos(x - pi / 6) / (0.5 + sin(y) ** 2) + abs(y - x) / 3
    print(f"d = {round(d, 2)}")
else:
    print("Нельзя делить на ноль!")

# Функция w
if (sin(y) ** 2) - (sin(x) * sin(y)) ** 2 != 0:
    w = ((x / y) * (z + x) * exp(abs(x - y)) + log(1 + e)) / (
        (sin(y) ** 2) - (sin(x) * sin(y)) ** 2
    )
    print(f"w = {round(w, 2)}")
else:
    print("Нельзя делить на ноль!")

# Функция b
if (1 + x**2 * abs(y - tan(z))) != 0:
    b = (3 + exp(y) - 1) / (1 + x**2 * abs(y - tan(z)))
    print(f"b = {round(b, 2)}")
else:
    print("Нельзя делить на ноль!")

# Функция p
if x * y < -2:
    p = sqrt(abs(x * y)) + 2 * z
elif -2 <= x * y <= 2:
    p = x**3 + y**2 - z**2
else:
    p = x**z - x

print(f"p = {round(p, 2)}")

# Функция h
if x < y:
    h = atan(x + abs(y))
elif x > y:
    h = atan(abs(x) + y)
else:
    h = (x + y) ** 2

print(f"h = {round(h, 2)}")

# Функция b1
if x / y > 0:
    b1 = log(x / y) + (x**2 + y) ** 3
elif x / y < 0:
    b1 = log(abs(x / y)) + (x**2 + y) ** 3
elif y != 0 and x == 0:
    b1 = (x**2 + y**2) ** 3
elif y == 0:
    b1 = 0

print(f"b1 = {round(b1, 2)}")

# Функция b2
if x - y > 0:
    b2 = sin(x + y) + 2 * (x + y) ** 2
elif x - y < 0:
    b2 = sin(x - y) + (x - y) ** 3
elif y != 0 and x == 0:
    b2 = abs(x**2 + sqrt(y))
elif y == 0:
    b2 = 0

print(f"b2 = {round(b2, 2)}")
