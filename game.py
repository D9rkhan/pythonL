#Игра угадай число
#Импортируем библиотеку random
import random

#Генерация случайного числа и присвоение его в переменную random_number
random_number = random.randint(1, 5)

#Пользователь вводит число
user_number = input("Введите число (от 1 до 5): ")

#Условие
if int(user_number) == random_number:
    print("Вы угадали!")
else:
    print("Вы не угадали :(")
    print(f"Было загадано число: {random_number}")