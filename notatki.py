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
#
# a = "Python"
# b = 317
# print("a: {}, b: {}".format(a, b))
# b, a = a, b
# print("a: {}, b: {}".format(a, b))
#
# for x in range(1500,2701):
#     if x%7==0 and x%5==0
#         print(x)
#
#
# PONIEDZIAŁEK
# def simple_function():
#     print('Hello world!')
#     print('Wikipedia')
#
# simple_function()
#
# def my_function():
#     return 3+3
#
# print(my_function())
#
# def my_function():
#     """Dokumentacja funkcji"""
# help(my_function)
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
# x = fibbonaci_numbers(12+2)
# print(x)
# print(fibbonaci_numbers.__doc__)
#
# # funkcja len zlicza
# def fukcja(x):
#     a = 0
#     for y in x:
#         a += 1
#     return a
#
# c = fukcja("jakaś wartość")
# print(c)
#
# def lista(l):
#     a = 0
#     for i in l:
#         a+=i
#     return a
# b=lista(1;5;6;8)
# print(b)
# #szukać gdzie jest błąd
#
# # mnożenie listę
# def lista(x):
#     a = x[0]
#     for i in x[1:]:
#         a*=i
#     return a
# b = lista([2,4,5])
# print(b)
#
#największa z listy
# def największ_zlisty(x):
#     a = x[0]
#     for i in x:
#         if i>a:
#             a = i
#     return a
# b=[-42,4,-7,-8]
# c= największ_zlisty(b)
# print(c)
#
#zliczanie ilości znaków
# def zliczanie(x):
#     a = {}
#     for i in x:
#         b = a.keys()
#         if i in b:
#             a[i]+=1
#         else:
#             a[i] = 1
#     return a
#
# z = zliczanie("policz ilość znaków")
# print(z)
#
# Funkcja w Pythonie do zliczania ciągów znaków, w których długość ciągu wynosi 2 lub więcej, a pierwszy i ostatni znak są takie same z podanej listy ciągów
# 8:39
# Ćwiczenie
# Napisz funkcję w Pythonie, który zlicza ciągi znaków, w których długość ciągu wynosi 2 lub więcej, a pierwszy i ostatni znak są takie same z podanej listy ciągów.
# Przykładowa lista : ['abc', 'xyz', 'aba', '1221']
# Oczekiwany wynik: 2
#
# def ciąg(x):
#     licznik = 0
#     for i in x:
#         if len(i) >= 2 and i[-1] == i[0]:
#             licznik += 1
#     return licznik
# print(ciąg(['abc', 'xyz', 'aba', '1221']))
#
# Funkcja Pythona do pobrania listy, posortowanej w porządku rosnącym według ostatniego elementu w każdej krotce z podanej listy niepustych krotek
# Ćwiczenie
# Napisz funkcję w Pythonie, aby uzyskać listę posortowaną w porządku rosnącym według ostatniego elementu w każdej krotce z podanej listy niepustych krotek.
# Przykładowa lista: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Oczekiwany wynik : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
# def funkcja1(krotka):
#     return krotka[1]
#
# def sortowanie(lista):
#     posortowana = sorted(lista, key=funkcja1)
#     return posortowana
# print(sortowanie( [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
#
# Ćwiczenie
# Napisz funkcję w Pythonie, aby uzyskać łańcuch składający się z pierwszych 2 i ostatnich 2 znaków z danego łańcucha. Jeśli długość ciągu jest mniejsza niż 2, zwróć zamiast tego pusty ciąg.
# Przykładowy ciąg : Python
# Oczekiwany wynik: Pyon
# Przykładowy ciąg : Py
# Oczekiwany wynik: PyPy
# Przykładowy ciąg : P
# Oczekiwany wynik: pusty ciąg
#
# def ciąg_znakow(x):
#     i = ()
#     if len(x) < 2:
#         return ""
#     else:
#         return x[:2] + x[-2:]
# print(ciąg_znakow("Python"))
#
# Ćwiczenie
# Napisz program, policzy silnię dla liczby n tj.
# n! = 1*2*3*4...*(n-2)*(n-1)*n
# Zrób to przez napisanie funkcji, która rekurencyjne będzie się odwoływała do samej siebie do momentu gdy będzie liczyła silnie dla 1, która wynosi 1.
#
# def silnia(n):
#     if n==1:
#         return 1
#     return silnia(n-1)*n
# print(silnia(4))
#
# def ciagF(x):
#     if x<=1:
#         return x
#     return ciagF(x-1)+ciagF(x-2)
# print(ciagF(11))
#
# import sys
# try:
#     f = open("plik.txt")
#     s = f.readline()
#     i = int(s.strip())  # Usuń spacje
#     print(i)
# except OSError as err:
#     print("Błąd systemu: {0}".format(err))
# except ValueError:
#     print("Nie można dokonać konwersji.")
# except:     # PEP 8: E722 nie używaj pustego 'except'
# print("Nieoczekiwany wyjątek:", sys.exc_info()[0])
#
# raise
#
# #Blok try zgłosi błąd podczas próby zapisu do pliku tylko do odczytu::
#
# try:
#     file = open("demofile.txt")
#     try:
#         file.write("Lorum Ipsum")
#     except:
#         print("Coś poszło nie tak podczas ZAPISYWANIA do pliku")
#     finally:
#         file.close()
# except:
#     print("Coś poszło nie tak podczas OTWIERANIA pliku")
#
# x = -1
#
# if x < 0:
#     raise Exception("Przepraszamy, brak liczb poniżej zera")
#
# Ćwiczenie
# Podczas pisania funkcji najlepiej jest przeprowadzić walidację liczb.
# Jeśli użytkownicy wprowadzą tekst, pojawi się błąd podczas próby konwersji na int.
# Napisz program, który poprosi użytkownika o podanie dwóch liczb.
# Dodaj i wydrukuj wynik.
# Jeśli nie zostanie wprowadzona liczba, zwróć komunikat o błędzie i poproś ponownie.
#
# while True:
#     try:
#         x= int(input("Podaj pierwszą liczbę: "))
#         y= int(input("Podaj drugą liczbę: "))
#         print(int(x+y))
#         break
#     except ValueError:
#         print("błąd")
#
# Podziel przez siebie dwie liczby
# Umieść:
# result = "Nie możesz podzielić przez 0"
# we właściwym miejscu, aby program uniknął ZeroDivisionError
# Podpowiedź 1: Po prostu umieść przypisanie wartości dla wyniku po linii Except
# Podpowiedź 2: Zwróć uwagę na wcięcia
#
# a = 4
# b = 0
#
# try:
#     result= a / b
# except ZeroDivisionError:
#     result = "Nie możesz podzielić przez 0"
# print(result)
#
# Ćwiczenie
# Napisz dowolny kod.
# Wychwyć w nim wyjątek, ale nic nie rób.
#
# a = 4
# b = 0
#
# try:
#     result= a / b
# except ZeroDivisionError:
#     pass  #chamskie omijanie wyjątków TAK NIE ROBIĆ
#
# Ćwiczenie
# Spróbuj dodać int do ciągu.
# Umieść:
# msg = "Nie możesz dodać int do string"
# aby program uniknął błędu BaseException.
# Możesz użyć wyjątku Exception, chociaż zwykle powinno się ostrożnie używać tak potężnych instrukcji wyjątków.
#
# a = 5
# b = 'abc'
# try:
#     msg = a + b
# except ValueError:
#     msg = "Nie możesz dodać int do string"
# print(msg)
#
# Ćwiczenie
# Stwórz trójelementową listę.
# Spróbuj wydrukować piąty element.
# Umieść:
# msg = "Jesteś poza zakresem listy"
# aby uniknąć wyjątku IndexError.
#
# x = ["A",3,55]
# try:
#     msg = x[5]
# except IndexError as err:
# # except IndexError
#     msg = err
#     # msg = "Jesteń poza zakresem listy"
# print(msg)
#
# Ćwiczenie
# Spróbuj otworzyć do czytania plik (podpowiedź: f = open(arg, "r")).
# W razie braku możliwości otwarcia pliku, obsłuż wyjątek.
# W przeciwnym przypadku wypisz:
# Nazwę pliku;
# Liczbę wierszy (podpowiedź: len(f.readlines()).
# Na koniec zamknij ten plik (podpowiedź: f.close()).
# arg = "testowy.txt"
# try:
#     f = open(arg,"r")
# except IOError:
#     print("Nie można otworzyć pliku")
# else:
#     print("Ilość wierszy: "+ str(f.readlines()))
#     f.close()   #poprawić
#
# Ćwiczenie
# Użyj finally do zamykania obiektów i czyszczenia zasobów.
# Spróbuj otworzyć i zapisać (podpowiedź: write) w pliku, którego nie można zapisać.
# Zapewnij, aby program mógł kontynuować bez pozostawiania otwartego obiektu pliku.

try:
    plik = open(testowy.txt,"r")
    plik.write("string")
except IOError:
    print("coś poszło nie tak")
finally:
    plik.close()   #poprawić

