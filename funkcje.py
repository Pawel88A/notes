# Napisz program w Pythonie, aby znaleźć liczby podzielne przez 7 i będące wielokrotnością 5 między 1500 a 2700 (obie uwzględnione)

for numer in range(1500,2701):
    if numer % 7 == 0 and numer % 5 == 0:
        print(numer)
