# Napisati program koji ispisuje parne brojeve od 0 do N. 
# Provera parnosti se radi koristeci operator ostatka pri
# celobrojnom deljenju nekog broja sa dvojkom %, 
# Ukoliko je uslov x % 2 == 0 zadovoljen, onda je x paran broj. 

n=int(input('Unesite broj: '))
for paranBr in range (0,n+1,2):
    print(paranBr)

# nisam koristila % zato sto je svaki ceo paran broj svakako deljiv sa 2 bez ostatka
# int uslovljava da to bude ceo broj bez ostatka pri unosu za razliko od float
# rang 0 - znaci da brojevi idu od nule, 
# n+1 - ceo niz parnih brojeva od 0-12 i broj 12
# n - kada je do poslednjeg broja pre broja 12
# 2 - ispis samo brojeva koji su deljivi sa 2