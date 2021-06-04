#doppio asterisco mi indica elevamento a potenza (**), singolo moltiplicazione (*) ->per elevare a potenza (numero ** potenza)
#DEF è comando che indica funzione
#LE VARIABILI SONO LOCALI, SONO RIFERITE ALLA SINGOLA LEZIONE
import math
def area_rett (b,h):
  area= b*h
  print(area)
#adesso ho definiyo funzione, scrivendo nome funz creata con valori mavrò risultato (FUORI DA INDENTAZIONE)
area_rett (6,7)
#exec(open('C:/Users/tommaso/AppData/Local/Temp/tmpu2xmbrik.py'.encode('utf-8')).read())
#area_rett (6,7)
#42 !!!!!!!!!!!!
#area cerchio
#in modulo math è possibile richiamare area pgreco, richiamare modulo math
#valore pgreco -> math.p
def area_cerchio (r):
    area=(r**2)*math.pi
    print(area)
#ESECUTORE CONDIZIONALE -> if   ->else
#mi produce un indentazione
if a > 2 #questa è variabile, la devo modificare da qua per avere risposta
print("maggiore")
else:
print("minore")
#funzione numero pari/dispari
#un numero è pari se è possibile dividerlo per due
#NB se devo assegnare un valore a una variabiule = / == operatore che verifica ugualianza
#risultatao di questa operazione sonon 2 valori: 0=pari   no 0=dispari
#nb, in output sommo stringa a (n) che è variabile numerica -> devo rendere (n) string -> str(n)
def num_pari (n):
    if n % 2 == 0:
        print("il numero "+ str(n)+" è pari")
    else:
        print ("il numero" + str(n)+" è dispari")
#output
#num_pari (9876543)
#il numero9876543 è dispari  
# operatore != mi definisce diversita (== ugualianza)
num_pari (896)
il numero 896 è pari

#creare ora funzione per sapere se numero variabile è compreso tra alti due 
#nb. ovviamente in esecuzione funzione i valori di variabili devono essere in stesso ordine da me indicato in funzione
def num_compreso (n,a,b):
    if n > a and n < b:
        print (str(n) + " è compreso tra i due valori")
    else:
        print (str(n) + " non è compreso tra i due valori")
#output
#num_compreso (3,1,7)
#3 è compreso tra i due valori
#NB la prima condizione verificata ha precedenza sulle altre !!!!!!!!!!!!!!!!!!!!!!
def num_compreso (n,a,b):
    if n > a and n < b:
        print (str(n) + "è compreso tra i due valori")
    elif n==a:
        print (str(n) + " è uguale a " + str(a))
    elif n==b:
        print (str(n) + " è uguale a " + str(b))    
    else:
        print (str(n) + "non è compreso tra i due valori")
    elif a>b:
        print ("non ha senso")   
 # -> la condizione che invalida le altre deve stare sopra le altre ->così è funzione di prima corretta
 def num_compreso (n,a,b):
    if a>b:
        print ("non ha senso")n > a and n < b:
        print (str(n) + "è compreso tra i due valori")
    elif n==a:
        print (str(n) + " è uguale a " + str(a))
    elif n==b:
        print (str(n) + " è uguale a " + str(b))    
    else:
        print (str(n) + "non è compreso tra i due valori")
    elif n > a and n < b:
        print (str(n) + "è compreso tra i due valori")
#######
#a è il numero da cui voglio che parta conto alla rovescia
#in questo caso bisogna "partire dalla fine come ragionamento
def conto_alla_rovescia (a):
    if a == 0:
        print ("il conto alla rovescia è finito")
    else:
        print (a)
        conto_alla_rovescia (a-1)
#io gli dico scrivi "il cont rov è fin" quando l'if, che ha la precedenza, legge 0, nell'else io gli dico di leggere il mio numero e di sottrargli uno
#->il procedimento si ripete finche lui nonj legge 0 (riga 85)
#output infatti è
#10
#9
#8
#7
#6
#5
#4
#3
#2
#1
#il conto alla rovescia è finito
#ora vediamo il conto alla rovescia con fun "while"
#rispetto a prima while è parola riservata che indica grossomodo "finchè", quindi finche n>0 
def c_n (n):
    while n > 0:
        print(n)
        n = n - 1
    print ("fine conto")
#ho quindi "ciclo while"lui mi stampa numero finchè non arriva ad essere =0 , avendogli detto while >0 / inserendo n=n-1 lui, all'interno di ciclo, il numero diminusce e raggiungerà zero
#scrivo quindi print, fuori da while quando "ciclo while" mi porta n=0, mi stamperà quindi ("fine conto")
#NB, ciclo while continuerà ad andare finche non si verifica condizione (se ad es scivo, in ciclo, + -> non finirà mai)!!!!!!!!!!!!!! -> crasha sistema (poi prova e vedi quanto regge)

#LISTA è serie di valori, ognuno indicato da indice
# [] sono simboli di lista
#in lista posso inserire sia stringhe che num
a = [2,5,8,9,45,78,768,92,1]
print(a)
#mi stapo lista
#lista conta il primo valora come val 0, val 1 è quindi il secondo che vedo
print(a[3])
#stampo solo val tra quadra
#RANGE ->https://www.w3schools.com/python/ref_func_range.asp
l = range(10)
print(list(l))
#creo una lista e gli dico di elevarmi i suoi componentia alla seconda, ma questo non influenzerà valori di mia lista originale, se ribadisco comando di linea 115 su list di linea 124 avro stesso effetto di prima
list = [3,5,8,9,2,78,89]
for num in list:
    quadrato = num**2
print(quadrato)
#output
#print(quadrato)
#7921
#funzione che mi crea frequenze assolute di valori in mia lista
list = [3,5,8,9,2,78,89]
for num in list:
    quadrato = num**2
#qunate volte elento "n" compare in mia lista "l"
#l è variabile locale, mia lista
#n è variabile locale, numero che dovrò contare
def cont_element (l,n):
    for num in l:
        #num è variabile quindi e valore che conteggio
        if num == n:
            print ("val + str(n) + è presente in lista")
#ora però lui mi ripetera come output "val,,, ,,,lista"b ogni volta che incontra quel valore            











