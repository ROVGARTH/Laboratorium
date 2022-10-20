print('1)Dodawanie')
print('2)Odejmowanie')
print('3)Mnożenie')
print('4)Dzielenie')
print('5)Potegowanie')

x=int(input('Co chcesz wykonać'))
y=int(input('Podaj liczbę 1'))
z=int(input('Podaj liczbę 2'))

if x==1:
    print(y+z)
elif x==2:
    print(y-z)
elif x==3:
    print (y*z)
elif x==4:
    print(y/z)
elif x==5:
    print(pow(y,z))