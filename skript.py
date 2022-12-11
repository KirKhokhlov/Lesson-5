#!/usr/bin/python3

# Задание 1

border = "=" * 117
print(f"\n{border}\n\nЗадание 1\n")


def is_pass(password):
    flag_str = False
    flag_number = False
    if len(password) >= 6:
        for i in password:
            if i.isdigit():
                flag_number = True
            else:
                flag_str = True
        if flag_number and flag_str:
            if not password.isdigit():
                temp = password.lower()
                if "password" not in temp:
                    return True
    return False

print("1234а -", is_pass("1234а"))
print("12343115125567821 -", is_pass("12343115125567821"))
print("xxx_NOnumbers_xxx -", is_pass("NOnumbers"))
print("ihaveeeeapassword -", is_pass("ihaveapassword"))
print("1234f52paSsWord31 -", is_pass("1234f52paSsWord31"))
print("1234f52fgqR8465Fs -", is_pass("1234f52fgqR"))

print(f"\n{border}\n")

# Задание 2

print("Задание 2\n")


def adder(*args):
    if len(args) == 0:
        return 0
    try:
        rez = args[0]
        for i in range(1, len(args)):
            rez += args[i]
        return rez
    except:
        print("Аргументы разных типов.")


print(adder(1, 2, 3))
print(adder("12", "fasdf", "RE"))
print(adder([1, 2], [3, 4]))
print(adder())
print(adder("12d", 2))
print(f"\n{border}\n")

# Задание 3

print("Задание 3\n")


def fibonacci_number(n):
    try:
        n = int(n)
    except:
        print("Передайте положительное числовое значение.")
        return
    if n <= 0:
        print("Передайте положительное числовое значение.")
        return
    if n in {1, 2}:
        return 1
    return fibonacci_number(n - 1) + fibonacci_number(n - 2)


print(fibonacci_number(0))
print(fibonacci_number(-5))
print(fibonacci_number("asff"))
print(fibonacci_number(8))
print(f"\n{border}\n")
