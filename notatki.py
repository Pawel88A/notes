# print('Hello world!')
#
#
# s = 'First line.\nSecond line.'  # \n oznacza znak nowej linii
# print(s)  # z print(), \n tworzy nową linię
#
# print('C:\some\name')  # tutaj \n oznacza nową linię!
# print(r'C:\some\name')  # zwróć uwagę na r przed cytatem
#
# print("""\
# Usage: thingy [OPTIONS]
#      -h                        Display this usage message
#      -H hostname               Hostname to connect to
# """)
# #Możliwość obejmowania wielu wierszy przez literały ciągów
# #Jeden ze sposobów to użycie potrójnych cudzysłowów:
# #"""...""" lub
# #'''...'''
#
# INDEKSOWANIE                   w Pyton liczymy od zera
# word = 'Python'
# print(word[0]) # znak na pozycji 0
# word[5]  # znak na pozycji 5
# word[-1]  # ostatni znak
#
# Długość łańcucha
# s = 'supercalifragilisticexpialidocious'
# len(s)
# print(len(s))
#
# Dane wejściowe użytkownika w Pythonie
# Aby uzyskać dane wejściowe użytkownika w Pythonie, używa się polecenia input()
# Zapis wyniku w zmiennej i używanie go dalej
# Pamiętaj, że wynik uzyskany od użytkownika będzie ciągiem znaków, nawet jeśli wprowadzi liczbę
#
# Ćwiczenie
# Utwórz kod, który prosi użytkownika o podanie swojego imienia i wieku
# Wydrukuj skierowaną do użytkownika wiadomość z informacją o tym, ile ma lat
#
# name = input("Jak masz na imię: ")
# age = input("Ile masz lat: ")
# print("Twoje imię to " + name + " i masz " + age + " lat.")
#
# LISTY
# squares = [1, 4, 9, 16, 25]
# squares[0]  # indeksowanie zwraca element
# squares[-3:]  # krojenie zwraca nową listę
# squares = [1, 4, 9, 16, 25]
# a = squares[:]
# print("squares:", squares)
# print("a:", a)
# squares = [1, 2, 3]
# print("squares:", squares)
# print("a:", a)
# squares = [1, 4, 9, 16, 25]
# squares = squares + [36, 49, 64, 81]
# print(len(squares))
# print(squares)
#
# cubes = [1, 8, 27, 65, 125]  # coś tu nie gra
# cubes.append(216)  # dodaj sześcian 6
# cubes[3] = 64  # zastąp niewłaściwą wartość
# print(cubes)
#
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# # zamień niektóre wartości
# letters[2:5] = ['C', 'D', 'E']
# print(letters)
# # teraz je usuń
# letters[2:5] = []
# print(letters)
# # wyczyść listę, zastępując wszystkie elementy pustą listą
# letters[:] = []
# print(letters)
# letters = ['a', 'b', 'c', 'd']
# len(letters)
# print(len(letters))
#
# # Zagnieżdżanie list
# a = ['a', 'b', 'c']
# n = [1, 2, 3]
# x = [a, n]
#
# print(x)
# print(x[0])
# print(x[0][1])
