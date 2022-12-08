import numpy as np
# tab_1= np.array([1,2,3], dtype='int32');
# print(tab_1)
#
# tab_2= np.array([5,6,7,8])
# print(tab_2)

# Zadanie 1

# arr=[128,64,32,16,8,4,2,1]
# arr=[]
# for i in range(7,-1,-1):
#     arr.append(2**i)
#
arr=[2**i for i in range(7,-1,-1)]
print(arr)

wagi= np.array(arr)
print(wagi)

liczba_bin= np.random.randint(low=0, high=2, size=8);
print(liczba_bin)

dziesietny= wagi*liczba_bin
print(dziesietny)

suma= dziesietny.sum()
print(suma)

# Zadanie 2

macierz= np.random.randint(low=0, high=100, size=(5,5))
print(macierz)
print(f"Największą liczbą jest {macierz.max()}")

print(f"Najmniejszą liczbą jest {macierz.min()}")

print(f"Największe liczby: wiersz 0{macierz.max(axis=1)}")



print(f"Największa liczby: wiersz 1{macierz.min(axis=1)}")
sumaMaksymalnychOsX= macierz.max(axis=1).sum()
sumaMaksymalnychOsY= macierz.max(axis=0).sum()

sumaMinimalnychOsX= macierz.min(axis=1).sum()
sumaMinimalnychOsY= macierz.max(axis=0).sum()


print(f"suma maksymalnych wartości po osi X(axis=1):{sumaMaksymalnychOsX}")
print(f"suma Maksymalnych wartości po osi Y(axis=0):{sumaMaksymalnychOsY}")

print(f"suma Minimalnych wartości po osi X(axis=1):{sumaMinimalnychOsX}")
print(f"suma Minimalnych wartości po osi Y(axis=0):{sumaMinimalnychOsY}")

# Zadanie 3

tabWith0= np.zeros((3,3))
print(tabWith0)
# print(tabWith0[:,2].fill(1))
print(tabWith0[:2].fill(1))
print(tabWith0)

# Zadanie 4
