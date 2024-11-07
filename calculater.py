class OperationError(Exception):
    pass

d = 0

def summ():
    return a + c

def diff():
    return a - c

def mult():
    return a * c

def div():
    return a / c

try:
    a = int(input("Введите первое число: "))
    b = input("Введите математическую операцию: ")
    c = int(input("Введите второе число: "))
except ValueError:
    print("Ошибка: введено не число")

else:
    if b == "+":
        d = summ()
        print(f"Получается: {a} {b} {c}", "=", d)
    elif b == "-":
        d = diff()
        print(f"Получается: {a} {b} {c}", "=", d)
    elif b == "*":
        d = mult()
        print(f"Получается: {a} {b} {c}", "=", d)
    elif b == "/":
        try:
            d = div()
            print(f"Получается: {a} {b} {c}", "=", d)
        except ZeroDivisionError:
            print("Ошибка: деление на ноль")
    else:
        print ("Ошибка: введена неизвестная математическа операция")