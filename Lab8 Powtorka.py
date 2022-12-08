import math

lista=['Dawid','Kamil','Dominik','Radosław','Dominik']
def find(list, value):
    for i in lista:
        if i==value:
            print(list.index(value))

find(lista,'Dominik');


# Zadanie 2
dict1 = {'data1':10, 'data2':-4, 'data3':2}
dict2 = {'asfsaf':1, 'asfasfasdfgasd':-5, 'sdgdsjghdsjakajskghd':10000}
def sum_of_values(s1):
    j = 0
    for i in s1.values():
        j = j + i
    return(j)
b= sum_of_values(dict1)
c = sum_of_values(dict2)
print(b)
print(c)

# Zadanie 3
firstList=[1,2,3,4]
secondList=[2,2,3,4]

def potega(firstList,secondList):
    if len(firstList)!=len(secondList):
        print("Długości list są różne")
        return 0;
    else:
        for i in range(0,len(firstList)):
            print(f"L1 {i}")
            print(firstList[i]**secondList[i])
        for j in range(0,len(secondList)):
            print(f"L2 {j}")

potega(firstList,secondList)

# Zadanie 4

def znaki(string):
    dic1 = {}
    for i in string:
        if i in dic1:
            dic1[i] = dic1[i] + 1
        else:
            dic1[i] = 1
    return dic1
slownik = znaki('znaki napisu')
lista_kluczy = sorted(slownik)
for i in lista_kluczy:
    print(i, slownik.get(i))
print(znaki('znaki napisu'))

# Zadanie 5
def dodawanie(a,b):
    suma=a+b
    return suma

def odejmowanie(a,b):
    roznica=a-b
    return roznica
def mnozenie(a,b):
    iloczyn= a*b
    return iloczyn
def dzielenie(a,b):
    if b!=0:
        return a/b
    else:
        return None
dictionar={'+':dodawanie,'-':odejmowanie,'*':mnozenie, '/':dzielenie}
x=int(input("Podaj liczbę 1"));
y=int(input("Podaj liczbę 2"))
z=input('Podaj działanie')

dictionar[z](x,y)
print(dictionar[x](x,y))