literka= input("Wprowadź literkę ")

if len(literka)>1 or len(literka)==0:
    print("Nieprawidłowe dane")
    exit()
if 'a'<= literka <='z':
    print("Literka jest mala")
elif 'A'<= literka <='Z':
    print("Literka jest duza")
else:
    print("Podany znak nie jest literą")