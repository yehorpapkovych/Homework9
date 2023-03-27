a = input('a = ')
b = input('b = ')

try:
    c = int(a) / int(b)
    print(c)
except (ZeroDivisionError, ValueError):
    print('Wrong!')