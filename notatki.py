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
#
# Podstawowe typy danych
# Wyświetlanie w Pythonie
# Do wyświetlania napisów, oraz zawartości zmiennych, stałych i innych obiektów w języku Python służy funkcja print(x), gdzie x jest rzeczą, która zostanie wyświetlona
# W Pythonie funkcje są zapisywane podobnie jak w matematyce, czyli f(x,y), gdzie f to nazwa funkcji a x oraz y to argumenty przekazywane do funkcji
# Jedną z dostępnych funkcji jest type(obj), która zwraca informacje o typie zmiennej lub obiektu obj
# Typ numeryczny
# Python rozróżnia typy liczb:
# Całkowite np. 0, 1, 5, 2137670, -45600, …
# Rzeczywiste np. 0.5, 1/3, 1.67e-10, 6.023e+23, …
# Zespolone
# Można konwertować między sobą również zmienne zawierające liczby całkowite na liczby rzeczywiste:
# float() oraz na odwrót
# int()
# Typ danych na który wskazuje dana zmienna możemy sprawdzić poleceniem (funkcją) type()
#
# i = 2
# print(type(i))
#
# f = 2.71828
# print(type(f))
#
# c = 0.5 + 1j
# print(type(c))
#
# print(float(i), " ", int(f), " ", c)
#
# # Typ logiczny
#
# a = 2 > 1
# print(a)
# print(type(a))
#
# b = 2.71828 > 3
# print(b)
# print(type(b))
#
# Typ znakowy
# Zawiera pojedyncze znaki lub ciągi znaków
#
# znak = "A"
# print(znak)
# print(type(znak))
#
# napis = "Ala ma kota"
# print(napis)
# print(type(napis))
#
# print(napis[0])
# print(napis[-2])
# print(napis[:-5])
# print(type(napis[0]))
# print(napis[-3:-1])
# print(type(napis[-3:-1]))
#
# Istnieje również wartość kroku (step), której można użyć z dowolnym z powyższych:
# a[start:stop:step]  # elementy od start do stop-1, co step
# print(napis[::2])
# print(type(napis[::2]))
# Napisów, w przeciwieństwie do list, nie można zmieniać
#
# napis = "Ala ma kota"
# napis = "Ala ma koty"
# napis = "Ala będzie miała kotki dwa"
# zmienna = "Ala ma kota a kot ma psa"
# print(zmienna)
# print(type(zmienna))
# zmienna = 127
# print(zmienna)
# print(type(zmienna))
# zmienna = "127"*127
# print(zmienna)
# print(type(zmienna))
#
# napis = "Ala ma kota a kot ma psa"
# liczba_calkowita = 2
# print(napis + liczba_calkowita) #wywali błąd różne typy znaków
#
# napis = "Ala ma kota a kot ma psa"
# liczba_calkowita = 2
# print(napis + str(liczba_calkowita))
#
# sampleStr = "Datatypes"
# middleindex = int(len(sampleStr)/2)
# print(middleindex)
# print("Oryginalny ciąg to", sampleStr)
# middleThree = sampleStr[middleindex -1:middleindex +2]
# print("To są trzy środkowe znaki",middleThree)
#
# sampleStr="FullStack"
# middleIndex = int(len(sampleStr) / 2)
# print("Oryginalny ciąg to", sampleStr)
# middleThree = sampleStr[middleIndex - 1:middleIndex + 2]
# print("To są trzy środkowe znaki", middleThree)
#
# s1 = "FullStack"
# s2 = "Python"
# middleIndex = int(len(s1)/2)
# # print(middleIndex)
# print("Oryginalne ciągi to:", s1, s2)
# middleThree = s1[:middleIndex]+ s2 +s1[middleIndex:]
# print("Po dołączeniu nowego ciągu w środku", middleThree)
#
# s1 = "America"
# s2 = "Japan"
# first_char = s1[:1] +s2[:1]
# # print(first_char)
# middle_char = s1[int(len(s1) / 2):int(len(s1) / 2)+1] + s2[int(len(s2) / 2):int(len(s2) / 2) +1]
# # print(middle_char)
# last_char = s1[len(s1)-1] + s2[len(s2)-1]
# # print(last_char)
# res = first_char + middle_char + last_char
# print("Mix String to ", res)



