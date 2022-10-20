cenado18= 10
cenaod18=20
x= int(input('Wprowadź wiek użytkownika'))
def first(x):
    if x<4:
        print("Wstęp jest bezpłatny")
    elif x>4 and x<18:
        print(cenado18)
    elif x>18:
        print(cenaod18)

first(x)