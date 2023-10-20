def pnep(number):
    if number % 2 == 0:
        return True
    else:
        return False

us = int(input("Введіть число "))

res = pnep(us)

print(res)