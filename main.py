# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
include_digits = 0
include_lowercase_letters = 0
include_uppercase_letters = 0
include_punctuation = 0
include_vcc = 0

print('Введите количество паролей, которое требуется сгенерировать.')
count_pass = int(input())
print('Введите требуемую длину пароля.')
len_pass = int(input())
print('Нажмите "д", если пароль должен включать в себя цифры "0123456789"')
if input().lower() == 'д':
    include_digits += 1
    chars += digits
print('Нажмите "д", если пароль должен включать в себя строчные буквы "abcdefghijklmnopqrstuvwxyz"')
if input().lower() == 'д':
    include_lowercase_letters += 1
    chars += lowercase_letters
print('Нажмите "д", если пароль должен включать в себя заглавные буквы "ABCDEFGHIJKLMNOPQRSTUVWXYZ"')
if input().lower() == 'д':
    include_uppercase_letters += 1
    chars += uppercase_letters
print('Нажмите "д", если пароль должен включать в себя специальные символы "!#$%&*+-=?@^_"')
if input().lower() == 'д':
    include_punctuation += 1
    chars += punctuation
print('Нажмите "д", если пароль НЕ должен включать в себя "неоднозначные символы" "il1Lo0O"')
if input().lower() == 'д':
    include_vcc += 1
    for char in chars:
        if char in 'il1Lo0O':
            chars = chars.replace(char, '')


def generate_password(len_pass, chars):
    password = ""
    for _ in range(len_pass):
        password += choice(chars)
    return password

for _ in range(count_pass):
    print(generate_password(len_pass, chars))
