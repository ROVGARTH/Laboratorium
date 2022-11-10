import random
i=1
empty=[]
while i<=15:
    i+=1;
    empty.append(round(random.uniform(0,50),2));

print(empty)
empty.sort()
print(empty)
# Zadanie 1
print(f"Największa liczba w liście to {empty[-1]}")
print(f"Najmniejsza liczba w liście to {empty[0]}")
# Zadanie 2
a= float(input("Podaj indeks wybranej liczby:"))
if a in empty:
     print(f"Podana liczba znajduje się na pozycji numer {empty.index(a)}")
else:
     print("Podanej liczby nie ma w liście")

# Zadanie 3
total=0
srednia=0
osoba=1
for i in empty:
    total+=i;
    srednia= total/len(empty)
    osoba+=1
    # print(i)
    if i>srednia:
        print(f"Osoba numer {osoba} zdobyła punkty powyżej średniej")
    elif i<srednia:
        print(f"Osoba numer {osoba} zdobyła punkty poniżej średniej")

print(f"Suma punktów w liście wynosi {round(total,3)}")
print(f"Srednia punktów wynosi: {round(srednia,3)}")

#Zadanie 4
