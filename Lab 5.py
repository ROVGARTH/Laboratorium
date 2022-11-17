# Slowniki

# Zadanie 1
values={10,20,30}
keys=['ten','twenty','thirty']

x= zip(values,keys)
print(dict(x))

# Zadanie 1 c.d
dictionary= dict(trzydziesci=30,czterdziesci=40,piedziesiat=50)
print(dictionary)
dictionary.update(x)
D=dict(zip(keys,values))
print(D)
D3= D.copy()
D3.update(dictionary)
print(D3)

# Zadanie 2
# sprawdzenie= input('Sprawdź słownik')
sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"
}

for s in sample_dict.keys():
    print(s, sample_dict[s])

for k,v in sample_dict.items():
    print(f"{k:<10}={v:>8}")

l=["name","age","city",'a']
# emptyDict={}
# for klucz in l:
#     if klucz in sample_dict.keys():
#         emptyDict[klucz]=sample_dict[klucz]

# emptyDict={for k in l if k in sample_dict.keys()}
# print(emptyDict)

d3= sample_dict.copy()

for i in l:
    if i in d3:
        d3.pop(i)
print(d3)

if "Jones" in sample_dict.values():
    print("Wystepuje")

else:
    print("Nie wystepuje")

sample_dict["location"]=sample_dict['city']

for k,v