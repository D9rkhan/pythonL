# numexpr библиотека чтобы вывести итог математической операции
import numexpr

#colorama библиотека чтобы перекрасить текст в консоли
from colorama import init
from colorama import Fore, Back, Style
# запуск библиотеки
init()

expr = input("Введите математическую операцию: ")

result = numexpr.evaluate(expr)

#Fore цвет текста
print(Fore.CYAN)

#Back цвет фона
print(Back.BLACK)

print(f"Результат: {result}")

input()

"""
Можно собрать программу .exe с помощью библиотеки pyinstaller
Вводим команду pyinstaller (Название файла с расширением) -F
"""