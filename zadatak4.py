# Napisati program koji kreira recnik informacija o automobilu. 
# Recnik sadrzi polja Marka, Model,Godiste. Ispisati dati recnik. 
# Zatim dodati novi kljuc: RegBroj i njenu vrednost sa tastature
# Ispisati ponovo novonastali recnik Zatim dodati novi kljuc: 
# Cena i njenu vrednost sa tastature. Ispsiati ponovo novonastali recnik

recnik={
    'marka':'BMW',
    'model':'m318',
    'godiste':'2006'
}
print(recnik)
recnik['regBroj']=str(input('Unesi registarski broj '))
print(recnik)
recnik['cena']=int(input('Unesite cenu '))
print(recnik)