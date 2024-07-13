from random import choice
import time

pass_symbol = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
lenght_pass = int(input('Введите длину пароля'))
password = ''

for i in range (lenght_pass):
    password += choice(pass_symbol)

time.sleep(3)

print("Ваш пароль", password)
 