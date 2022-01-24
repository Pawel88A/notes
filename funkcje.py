# Napisz program w Pythonie, aby znaleźć liczby podzielne przez 7 i będące wielokrotnością 5 między 1500 a 2700 (obie uwzględnione)
#
# for numer in range(1500,2701):
#     if numer % 7 == 0 and numer % 5 == 0:
#         print(numer)
#
# nl = []
# for x in range(1500,2701):              #rozwiązanie prowadzącego
#     if x % 7 == 0 and x % 5 == 0:
#         nl.append(str(x))
# # print(nl)
# print(';'.join(nl))                     #każdy element musi być stringiem, format łatwo można kopiować CSV
#
#
#
# # FUNKCJE
# #funkcja drukująca "Hello world!" i "Wikipedia"
# def simple_function():
#     print('Hello world!')
#     print('Wikipedia')
#
# simple_function()
#
#
# #instrukcja return kończy działanie funkcji i zwraca to co po niej następuje
# def my_function():
#     return 3+3
#
# print(my_function())
#
#
# def add(x, y):
#     print('x =', x, ',y =', y)
#     return x + y
#
# print(add(2, 3))
# # print(add(x = 2, y = 3))
#
# Docstring czyli informacja o funkcji zawarta w potrójnych cudzysłowach
#
# def my_function():
#     """Dokumentacja funkcji"""
#
# help(my_function)
#
# Rekurencja czyli rekursja (ang.recursion)
# Odwoływanie się do samej siebie np.:funkcji, lub definicji.
# np.: Każdy ojciec jest starszy od swojego syna, każdy ojciec jest czyimś synem
# Efekt Droste(np odbicie w dwóch lustrach)
#
#
# Ciąg Fibanacciego! (wzór a, b = b, a+b)
# Zadanie o rozmnazaniu się królików
# ile par królików może spłodzić jedna para w ciągu roku?
# jeżeli:
# każda para rodzi nową parę w ciągu jednego miesiąca
# para staje się płodna po miesiącu
# króliki nie zdychają
#
# def fibbonaci_numbers(n):
#     ''' zwraca liczby Fibonacciego mniejsze od n '''
#     wynik = []
#     a, b = 0, 1
#     # while a < n:
#     while len(wynik) < n:
#         wynik.append(a)
#         a, b = b, a+b
#     return wynik
#
# x = fibbonaci_numbers(12+2)
# print(x)
# print(fibbonaci_numbers.__doc__)#atrybut zwraca docstring/help
#
#
# Funkcja do obliczania długości łańcucha bez używania funkcji len()
#
# def sumowanie(x):
#     licznik = 0
#     for y in x:
#         licznik += 1
#     return licznik
#
# c = sumowanie("Jakaś wartość")
# print(c)
#
# Funkcja, ktora zsumuje wszystki elementy na liście.
#
# def lista(l):
#
# def sum_list(items):
#     sum_numbers = 0
#     for x in items:
#         sum_numbers += x
#     return sum_numbers
#
# print(sum_list([1, 2, -8]))
#
# koniec 4 nagrania 1.22
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# f = open('write_file_name', 'w')
# f = open('append_file_name', 'a')
# f = open('read_file_name', 'r')
#
# f.read()
#
# f.readline()
#
# f.write('Witaj\n')
# value = 42
# f.write(value)
#
# >>>Traceback (most recent call last):
# >>> File "<stdin>", line 1, in <module>
# >>>TypeError: must be str, not int
#
# s = str(value)
# f.write(s)
#
# # Otwórz plik
# fo = open("text.txt", "r")
# print("Nazwa pliku: ", fo.name)
#
# line = fo.readline()
# print("Czytaj linię: >" + line + "<")
#
# # Ponownie ustaw wskaźnik na początek
# fo.seek(0, 0)  # fo.seek(0)
# line = fo.readline()
# print("Czytaj linię: >" + line + "<")
#
# # Zamknij otwarty plik
# fo.close()
#
# # Otwórz plik
# fo = open("text.txt", "r")
# print("Nazwa pliku: ", fo.name)
#
# # Uzyskaj aktualną pozycję pliku.
# pos = fo.tell()
# print("Aktualna pozycja: " + str(pos))
#
# line = fo.readline()
# print("Czytaj linię: >" + line + "<")
#
# # Uzyskaj aktualną pozycję pliku.
# pos = fo.tell()
# print("Aktualna pozycja: " + str(pos))
#
# # Zamknij otwarty plik
# fo.close()
#
# #otwarcie i wyświetlenie pliku
# fo = open("text.txt", "r")
# print(fo.read())
#
#
# 1) bez użycia instrukcji with
# file = open('file_path', 'w')
# file.write('hello world !')
# file.close()
#
# # 2) bez użycia instrukcji with
# file = open('file_path', 'w')
# try:
#     file.write('hello world')
# finally:
#     file.close()
#
# używanie instrukcji with
# with open('file_path', 'w') as file:        #prowadzący poleca :-)
# 	file.write('hello world !')
#
# content_list = []
# with open('text.txt', 'r') as tekst:
#     treść = tekst.readlines()
# print(treść)
#
# with open('text.txt', 'r') as text:
#     a = text.read()
# b = a.split()
# c = "_"
# for n in b:
#     if len(n) > len(c):
#         c = n
# print(c)
#
# Zapisywanie listy do pliku
# Ćwiczenie
# Napisz program w Pythonie, który zapisze listę do pliku.
#
# lista = ["aaa", "bbb", "ccc","1", 1, 3]
# with open("testowy.txt", "w") as file:
#     for i in lista:
#         file.write(str(i) + "\n")
#
# Ocenianie, czy plik jest zamknięty, czy nie
# Ćwiczenie
# Napisz program w Pythonie, aby ocenić, czy plik jest zamknięty, czy nie.
#
# file = open("testowy.txt", "r")
# print(file.closed)
# if not file.closed:
#         file.close()
# print(file.closed)
#
#
# MODUŁY
# import os
# os.system("dir")
#
# import time
# print("Dobranoc")
# time.sleep(2)
# print("Dzień dobry")
# from time import sleep
# print('Dobranoc')
# sleep(2)
# print('Dzień dobry')
#
# import time             #zawartość
# print(dir(time))
#
# from math import sin, pi
# print(sin(pi/2))














