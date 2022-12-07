"""
1. Список из числа.
Дано: натуральное число N.

Задание: написать функцию, которая возвращает список всех цифр этого числа в обратном порядке.

Пример:

 123, результат: [3, 2, 1]
"""


def get_reverse_digits(number):
    """
    Returns a list of digits of this number in reverse order.
    :param
        number (int): natural number
    :return:
        reverse_digits (list): list of digits in reverse order.
    """
    if number < 1:
        return 'Number is not natural'

    number_str = str(number)[::-1]
    reverse_digits = [x for x in number_str]
    return reverse_digits


number = 9542
print(get_reverse_digits(number))

# print(get_reverse_digits.__doc__)
# help(get_reverse_digits)