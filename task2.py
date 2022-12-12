import re

# 2. Палиндром.
# Дано: слово, состоящее только из строчных латинских букв.
#
# Задание: написать функцию, которая возвращает True, если слово палиндромом, иначе False.
#
# Палиндро́м — число, буквосочетание, слово или текст,
# одинаково читающееся в обоих направлениях.
# Например, число 404; слова «топот» в русском языке; текст «а роза упала на лапу Азора» и пр.
#
# Примеры:
#  'lol', результат: True
#  'hi', результат: False


def is_palindrome(word):
    if not (re.search('[a-z]', word)):
        return 'Text not in lowercase Latin letters!'

    reverse_text = word[::-1]
    if word == reverse_text:
        return True
    else:
        return False


word = 'racecar'
print(is_palindrome(word))
