imiona=['Kasia','Tomek','Jan','Ola','Jerzy',
        'Marek','Piotr','Zuzia','Bartek','Jacek']

imiona[3]='Kamil'
imiona[4]='Robert'
imiona.remove(imiona[7])

imiona.insert(0,'Piotr')
imiona.insert(1,'Mateusz')
imiona.insert(2,'Kuba')
print(imiona)

wpiszImie= str(input('Wpisz imię, które chcesz usunąć'))
wpiszImie.strip()

if(wpiszImie==imiona):
    imiona.remove(wpiszImie)
    print(imiona)
    print(wpiszImie)

else:
    print("Podane imie nie istnieje w zbiorze")

imiona[:len(imiona)-1]

imiona.sort();
print(imiona)

imiona.sort(reverse=True)
print(imiona)

imiona[:len(imiona)//2]=[]
print(imiona)