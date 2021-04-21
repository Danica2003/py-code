# Napisati program koji definise listu imena od 3 elmenta. 
# Program zatim od korisnika trazi da sa tastature unese cetvrto ime.
#To ime se smesta u kolekciju. Program zatim ispisuje celu kolekciju.
# Nakon toga program ispisuje imena koja imaju vise od 5 karaktera.
# Primer ulaza: Za imena Marko,Vukasin, Nemanja i cetvrto uneto ime Marija, 
# Program ispisuje: Vukasin Nemanja Marija

listaImena=['Marko','Vukasin','Nemanja']
print('Lista imena: ',listaImena)
listaImena.append(input('Unesite novo ime: '))
print('dopunjena lista: ',listaImena)

for ime in listaImena:
    if len(ime)>5:
        print(ime, '- Ime koje ima vise od 5 karaktera')
