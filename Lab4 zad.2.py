# Zadanie 2 LAB 4
import random
x= int(input("Wpisz liczbe"))

zestaw_1=[2, 9]
zestaw_2=[4, 14]
print(zestaw_1)
print(zestaw_2)
if x>zestaw_1[0] and x<zestaw_1[1]:
    print(f"Liczba {x} należy do zestawu_1")
elif x>zestaw_2[0] and x<zestaw_1[1]:
    print(f"Liczba {x} należy do zestawu_2")
else:
    print(f"Liczba {x} nie należy do żadnego zestawu")

zestaw_1_2= zestaw_1+zestaw_2
print(zestaw_1_2)