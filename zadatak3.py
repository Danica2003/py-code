# Napisati prgoram koji racuna sumu prvih N prirodnih brojeva. 
# Broj N se unosi sa tastature. Broj N mora biti veci od 0.
 
n=int(input('Unesite N: '))

suma=0
for i in range (1,n+1): 
    suma=suma+i
    
print(suma) 

