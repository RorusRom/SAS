'''def pnep(number):
    if number % 2 == 0:
        return True
    else:
        return False

us = int(input("Введіть число "))

res = pnep(us)

print(res)'''

'''def count_gol(t):
    t = t.lower()

    gol = "aeiouy"

    golc = 0

    for f in t:
        if f in gol:
            golc += 1

    return golc

us = input("Введіть рядок: ")
res = count_gol(us)
print(f"Кількість голосних у рядку: {res}")'''

def factorial(n):
    if n < 0:
        return "Факториал невозможно вычислить"

    elif n == 0 or n == 1:
        return 1

    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

input = input("Введите целое положительное число: ")

n = int(input)

result = factorial(n)

print(result)