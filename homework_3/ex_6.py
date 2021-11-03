# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 23:05:44 2021

@author: Ксения Камнева
"""

def int_func(new_str, only_first_word):
    if only_first_word == True:   
        return new_str.capitalize()
    else:
        return new_str.title()
    
new_str = input('Введите строку в нижнем регистре: ')
if new_str.islower():
    print(int_func(new_str, True))
    print(int_func(new_str, False))
else:
    print('Некорректный ввод двнных!')
   