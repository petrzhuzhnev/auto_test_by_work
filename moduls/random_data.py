import random
import string
import re


# метод получает строку, берет из нее цифры и добавлеяет в новую строку
def extract_nbr(str_with_number):
    if str_with_number is None or str_with_number == '':
        return 0
    just_number = ''
    for i in str_with_number:
        if i.isdigit():
            just_number += i  # работа со строкой
    return just_number


def extract_full_numbers(str_with_number):
    if str_with_number is None or str_with_number == '':
        return 0
    nums = re.findall(r'\d*\.\d+|\d+', str_with_number)
    nums = [float(i) for i in nums]
    return nums[0]


def extract_full_numbers_second(str_with_number):
    if str_with_number is None or str_with_number == '':
        return 0
    nums = re.findall(r'\d*\.\d+|\d+', str_with_number)
    nums = [float(i) for i in nums]
    return nums[1]


def random_numbers(value):
    numbers = string.digits
    return ''.join(random.choice(numbers) for i in range(value))


def random_letters(value):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    upper = random.choice(uppercase)
    random_string = ''.join(random.choice(lowercase) for i in range(value))
    return upper + random_string


def random_email():
    repeat_service = '@gmail.com'
    return random_letters(8) + repeat_service


def random_password():
    password = ''
    numbers = string.digits
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    punctuation = '!@$%&?*;:(-_+={/~<,.'
    list_value = numbers, lowercase, uppercase, punctuation
    for symbol in list_value:
        value = ''.join(random.choice(symbol) for i in range(2))
        password += value
    return password
