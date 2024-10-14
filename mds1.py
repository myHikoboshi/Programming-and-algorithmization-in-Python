from math import log, sqrt, atan, cos, sin, tan, pi

# Работа 1
# Ввод данных
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print()

# Операции над числами
sum = a + b
mul = a * b
div = a / b
sub = a - b

# Си-стиль
print("Си стиль:")
print("%d + %d = %d" % (a, b, sum))
print("%d * %d = %d" % (a, b, mul))
print("%d / %d = %.2f" % (a, b, div))
print("%d - %d = %d" % (a, b, sub))
print()

# Метод format
print("Метод format:")
print("{0} + {1} = {2}".format(a, b, sum))
print("{0} * {1} = {2}".format(a, b, mul))
print("{0} / {1} = {2}".format(a, b, round(div, 2)))
print("{0} - {1} = {2}".format(a, b, sub))
print()

# f-строки
print("f-строки:")
print(f"{a} + {b} = {sum}")
print(f"{a} * {b} = {mul}")
print(f"{a} / {b} = {round(div, 2)}")
print(f"{a} - {b} = {sub}")
k = log(abs((y - sqrt(abs(x))) * (x - y / (z + x**2 / 4))))
