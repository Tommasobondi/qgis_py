#posso inserire comme ti in py, con # !!!!!!!!!
#per saltare più righe di codici uso apici ("), uno per ongni riga sotto ad apici che voglio saltare !!!!!!!!!!!
#word flow di pyton sempre da alto a basso
#import -> importare librerie e funzioni da ambiente esterno
print ("hello world")
#per creare un programma fondamnetale assegnare valore a variabile
#il programma non mi dara risposta come nel caso di print, prog mi legge semplicemente info e registra, 
a= 45
g=6723
#comando print mi pernmette di "stampare risultato"
print (a)
#pyton mi rende valore assegnato a varibile
#NB NO SPAZI QUANDO ASSEGNO VALORE A VARIABILE
print (a+g)
#ovviamente cambiando valore variabile si modifica poi risultato, valore di mia variabile "a" viene sostituito
a=2
print (a+g)
c= a+b
#type
#visualizzare che tipo di varibile è (usare . come separatore decimali)
print(type(a))
#<class 'int'> ->int: numero intero
# "hgjk" mi segnala al programma che hgjk è una stringa
#In informatica, serie di bit ( s. di bit o binaria ), o di caratteri alfanumerici da quelli rappresentati ( s. alfanumerica ), presente in una memoria o su un supporto.
a= "ciao"
print(type(a))
#<class 'str'> -> str: è una stringa, se poi faccio print ora il programma mi visulaizzerà variabile a, come stringa
#sist riferimento è variabile particolare, visualizzato come EPSG me lo renderà stringa invece
#importanza fondamentale conoscere dato con cui sto lavorando
#per cambiare tipo di variabile, modifico tipo di dato, utilizzo FUNZIONE
#funzione "str"
a=5
b=str(a)
print (b)
print(type(b))
#ho assegnato valore ad a, lo trasbormo in stringa (da int), rinominandolo b, con print visualizzo -><class 'str'>
#inverso, assegno ad a valore "ciao", che quindi è stringa, in in int
#funz e FLOAT
a="ciao"
b=float(a)
print(type(b))
#Traceback (most recent call last):
#  File "C:\PROGRA~1\QGIS3~1.10\apps\Python37\lib\code.py", line 90, in runcode
#    exec(code, self.locals)
#  File "<input>", line 1, in <module>
#ValueError: could not convert string to float: 'ciao'
#NB mi da ERRORE, non è ovviamente possibile trasfomare stringa in numero
#line 5, ho crato nuova varibile "c" sommando a e b
a=2
b=3
c= a+b
print(type(c))
#posso moltiplicare stringa per numero
a= "ciao"
b= 3
c=a*b
print (c)
#risultato è "ciaociaociao"
#non posso concatenare stringa a intero ->trasformo int in stinga
c= a+ str(b)
print(c)
#ciao3 a questo punto è il risulatato
#parola RISERVATA, è parola con significato per pyton (ad es. print, end, or, not), le variabili non possono essere denominate con parole riservate ne con valori numerici 8ne iniziare per valori numerici)
#nome variabile deve essere stringa che non sia parola riservata
#FUNZIONI
a= str(3)
print(type(a))
#print è funzione, (bhcddc) è argomento
#per utilizzare funz mate (sin, cos...) devo imposrtare
#import, mi permette di imposrtare da esterno in ambiente di lavoro (funzioni e librerie)
import math
a=math.sin(45)
print (a)
#Python code in one module gains access to the code in another module by the process of importing it. The import statement is the most common way of invoking the import machinery, but it is not the only way. Functions such as importlib.import_module() and built-in __import__() can also be used to invoke the import machinery.  
#libreria math -> https://www.python.org/doc/
#creare funzioni -> "def"
#DEF è parola riservata che mi permette di creare funzioni
def stampa_val #scrivo def, poi definisco nome mia funzione (stampa_val), poi devo assegnare variabili all'interno di funzione
def stampa_val (a):
#a questo punto py mi crea indentazione, ossia 4 righe in cui console sa che sto lavorando in funzione
#a è paramentro, ossia variabile valida all'interno di funzione, ora vado a scrivere cosas deve fare funz in spazio indentato, nel caso voglio stapare a, quindi:
print (a)
#a questo punto posso eseguire mia finzione
stampa_val (45)
stampa_val ("ciao")
# funzione creata esuegue ora sia per stringa che per int
#ovviamente poi posso assegare valore a nome e poi inserisco nome in funzione
jari= 100
stampa_val (jari)
#creo funzione che calcola area rettangolo, siuamilare a prima, con due variabili, gli assegno operazione e poi inserisco print, per visualizzare risultatao
def area_rett (b,h):
  area= b*h
  print(area)
#adesso ho definiyo funzione, scrivendo nome funz creata con valori mavrò risultato (FUORI DA INDENTAZIONE)
area_rett (6,7)
#exec(open('C:/Users/tommaso/AppData/Local/Temp/tmpu2xmbrik.py'.encode('utf-8')).read())
#area_rett (6,7)
#42 !!!!!!!!!!!!













