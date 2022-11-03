n = int(input("Proszę podać liczbę studentów: "))
a = 1  # wyświetlanie od 1 studenta
suma = 0  # podstawienie pod dodawanie punktów
while True:
    b = int(input(f"Proszę podać punkty studenta {a}: "))
    if b<0 or b>100:
        continue
    suma += b  # sumowanie punktów studentów
    a += 1  # przechodzenie do kolejnego studenta
    if a>n:
        break
y = suma / n  # obliczanie średniej
print("Średnia wszystkich studentów", round(y, 2))