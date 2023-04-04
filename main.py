a = int(input("Введите кол-во долларпов"))
b = int(input("""Выберите валюту
1- Евро
2 - Рубль"""))
def kurs(a, b):
    if b == 1:
        print(a*1.09)
    else:
        print(a*79.45)
kurs(a, b)