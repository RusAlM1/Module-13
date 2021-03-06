# try:
#     print("Перед исключением")
#     a = int(input("a: "))
#     b = int(input("b: "))
#     c = a / b
#     print(c)  # печатаем c = a / b, если всё хорошо
# except ZeroDivisionError as e:
#     print("После исключения")
# else:  # код в блоке else выполняется только в том случае, если код в блоке try выполнился успешно (т.е. не вылетело никакого исключения).
#     print("Всё ништяк")
# finally:  # код в блоке finally выполнится в любом случае при выходе из try-except
#     print("Finally на месте")
#
# print("После После исключения")

# еще пример исключений
# try:
#     age = int(input("How old are you?"))
#     if age > 100 or age <= 0:
#         raise ValueError("Тебе не может быть столько лет")
# except ValueError as error:
#     print(error)
#     print("Неправильный возраст")
# else:
#     print(f"You are {age} years old!")


# Подведём итоги:
#
# 1. Исключения — это ошибки, которые выбрасываются при неправильной работе программы и останавливают её выполнение, если
# они не обработаны.

# 2. Конструкция try-except выглядит следующим образом и служит для обработки исключений:
#
# try:
#     *код, который может вызвать ту или иную ошибку*
# except *ошибка*:
#     *код, который выполнится в случае возникновения ошибки*
# else:
#     *код, который выполнится только в случае если в try ничего не сломалось*
# finally:
#     *код, который выполнится в любом случае*
#
# 3. Блоки finally и else, являются необязательными, но могут быть использованы для вашего удобства. Код из блока
# finally выполняется в любом случае, независимо от исхода в блоках try-except. Код из блока else выполняется только в
# случае успешного выполнения кода в try.
# 4. Выбрасывать ошибки можно и по своему желанию с помощью конструкции raise *Тип ошибки* (сообщение, которое нужно
# вывести в консоль).


# Задание 13.4.8
try:
    s=int(input('введите число: '))
except ValueError as error:
    print("Вы ввели неправильное число")
else:
    print('Вы ввели: ',s)
finally:
    print('Выход из программы')