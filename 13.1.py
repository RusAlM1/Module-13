# Запишите вместо вопросительных знаков выражение, которое вернет True,
# если указывается високосный год, иначе False.
# Например, x = 2000 -> True; x = 1900 -> False; и т.д.
# Если есть сомнения в том, какие именно годы високосные,
# обратитесь к Википедии:
# https://ru.wikipedia.org/wiki/Високосный_год#Григорианский_календарь

# x = input('введите год: ') #НЕ РАБОЧЙИ КОД!!!!!!!
# def is_leap_year(x):
#     return (x % 400 == 0) or (( x % 4 == 0) and ( x % 100 != 0))


a = 3
b = 4
print(a >= 1 and a > b)
print(a > b or a <= b)
print(not (a > b) and a != b)
print(b != 4 or not (a <= 3))





# import unittest
# from Root.src.main import is_leap_year
#
# class basicTest(unittest.TestCase):
#     def test_leap(self):
#         self.assertTrue(is_leap_year(2000))
#
#     def test_not_leap(self):
#         self.assertFalse(is_leap_year(2001))
#
# if __name__ == '__main__':
#     unittest.main()