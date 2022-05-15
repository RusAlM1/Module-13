# Задание 13.5.1
# Запишите вместо вопросительных знаков выражение, которое вернет True,
# когда каждое из чисел А и В нечетное.
# def are_both_odd(A, B):
#     return
#     if A % 2 == 1 and B % 2 == 1:
#         print('Числа А и B нечетные')

#   РЕШЕНИЕ не полное!!!!

# A = int(input('введите число А: '))
# B = int(input('введите число В: '))
# if A % 2 == 1 and B % 2 == 1:
#     print('Числа А и В не четные')
# else:
#     A % 2 == 0 and B % 2 == 0
#         print('числа А и В четные')


# Задание 13.5.2

# if x > 0 and y > 0:
#     print("Первая четверть")
# if x > 0 and y < 0:
#     print("Четвертая четверть")
# if x < 0 and y > 0:
#     print("Вторая четверть")
# if x < 0 and y < 0:
#     print("Третья четверть")

# Пример 3. Введите с клавиатуры номер месяца. Определите сезон в зависимости от номера месяца и выведите сообщени
# month = int(input('введите месяц: '))
# if month in [3, 4, 5]:
#     print("Весна")
# elif month in [6, 7, 8]:
#     print("Лето")
# elif month in [9, 10, 11]:
#     print("Осень")
# elif month in [12, 1, 2]:
#     print("Зима")

# Задание 13.5.3
# У вас есть заготовка функции — def get_wind_class(speed):
# Вам нужно вместо "???" написать цикл, который возвращает из функции класс ветра в зависимости от его характера:
# от 1 до 4 м/с - "weak [1]"
# от 5-10 м/c - "moderate [2]"
# от 11-18 м/c - "strong [3]"
# от 19 м/c - "hurricane [4]"
# В последней строке мы просим программу напечатать результат (в зависимости от цифры в скобках) —
# def get_wind_class(speed):  # Объявление функции
# ???
# print(get_wind_class(3))  # Печатаем результат выполнения

# Мое решение

# def get_wind_class(speed):
#     speed = int(input('введите скорость ветра: '))
#     if 1 <= speed <= 4:
#         return "weak [1]"
#     elif 5 <= speed <= 10:
#         return "moderate [2]"
#     elif 11 <= speed <= 18:
#         return "strong [3]"
#     elif speed >= 19:
#         return "hurricane [4]"
# print(get_wind_class(3))

# Решение из задачника
# def get_wind_class(speed): #объявление функции
#     if 1 <= speed <= 4: #только аргумент
#         return "weak [1]"
#     elif 5 <= speed <= 10:
#         return "moderate [2]"
#     elif 11 <= speed <= 18:
#         return"strong [3]"
#     elif speed >= 19:
#         return "hurricane [4]"
# print(get_wind_class(3)) #мы просим программу напечатать то, что в скобках


# Задание 13.5.4 Допишите функцию check_user так, чтобы она по логину пользователя
# проверяла, существует он или нет,
# после чего с помощью вложенного условия проверяла
# правильность пароля этого пользователя.
# Функция должна возвращать только True или False.
# Чтобы вернуть True, напишите "return True";
# чтобы вернуть False, напишите "return False".

# user_database = {
#     'user': 'password',
#     'iseedeadpeople': 'greedisgood',
#     'hesoyam': 'tgm'
# }
#
# def check_user(username, password):
#     ???

# user_database = {
#     'user': 'password',
#     'iseedeadpeople': 'greedisgood',
#     'hesoyam': 'tgm'
# }
# def check_user(username, password):
#     if username in user_database:
#         if password == user_database[username]:
#             return True
#         else:
#             return False
#     else:
#         return False


# a = 39
# b = 41
# result = a if a > b else b
# print(result)

# Задание 13.5.5    Запишите условие, которое является истинным, когда только одно из чисел А, В и С меньше 45.

# A = int(input('введите число А: '))
# B = int(input('введите число В: '))
# C = int(input('введите число C: '))
# if ((A < 45) and (B >= 45) and (C >=45)) or \
#     ((A >= 45) and (B < 45) and (C >=45)) or \
#     ((A >= 45) and (B >= 45) and (C < 45)):
#     print('Есть число меньше 45 и только одно')
# else:
#     print('Числа меньше 45 нет или их несколько')

# Задание 13.5.6    Запишите логическое выражение, которое определяет, что число А не принадлежит интервалу от -10 до -1
# или интервалу от 2 до 15

# A = int(input('введите число А: '))
# if not (-10 <= A <= -1 or 2 <= A <= 15):
#     print("Число не принадлежит интервалу")
# else:
#     print("Число принадлежит интервалу")

# Задание 13.5.7    Дано двузначное число. Определите, входит ли в него цифра 5. Попробуйте решить задачу с
# использованием целочисленного деления и деления с остатком.

# n = int(input('введите двухзначное число: '))
# first_digit = n // 10
# second_digit = n % 10
#
# print((first_digit == 5) or (second_digit == 5))

# Задание 13.5.8    Проверьте, все ли элементы в списке являются уникальными.

# list_ = [-5, 2, 4, 8, 12, -7, 5]
# print(len(list_) == len(set(list_)))

# Задание 13.5.9    Дано натуральное восьмизначное число. Выясните, является ли оно палиндромом (читается одинаково
# слева направо и справа налево).

n = int(input('введите число: '))
print(str(n) == str(n)[::-1])