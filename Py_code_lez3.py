#importare modulo math
import math

#funz trasformazione gradi celsius in fharenheit
def c_f (c):
    fharenheit= (9*c + (32*5))/5
    print (fharenheit)
    
#attivazione script
   c_f(c)
    
lista_1 = [4,98,76,98,2,1,6,4,9]
lista_2 = [8,8,9,3,5,76,24,56,4]

#verificare ugualianza primi elemtnti di lista
#lista è serie di valori identificati da indice (primo valore contato con zero)
def first (list_1, list_2):
    if list_1 [0] == list_2 [0]:
       print ("primi elemti sono uguali")
    else:
       print ("primi elenti sono diversi")

#in programmzione è untile il concetto di casualità
#modulo random permette di generare numeri casuali
#"random" va importato -> si veda https://docs.python.org/3/library/random.html
#"pseudo" random -> numeri per noi sono casuali ma in realta pc lavora ovviamente su algoritmo, che genra numero "casuale"
import random
#generazione numero, richede parentesi
a= random.random()
print(a)
#funz int, per trasformane numero a virgola mobile in intero
#esegue una approssimazione
a= int(random.random())
print(a)


#LA FUNZIONE E SOLO BUTTATA GIù, NON GIURA, DEVI SISTEMASRE LA POSIZINE DEI COMNDI
#funzione per creare lista casuale e vedere seu parametro è presente all'interno di lista
#"range" è funz che genera lista di n numeri
def ind_n (n):
    lista = []
    #ripetimi questo ciclo 10 volte
    for num in range(10):
      #random.randint(a, b)
#Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
        b = random.randint(1, 100)
        print(b)
    #cosi facendo aggiungo alla mia lista (il ciclo for) il valore b
        lista.append (b)
#devo ora creare nuovo ciclo for che mi permette di analizzare tutti numeri che io ho creato
     for elem in lista:
        if n in lista:
          print(str(n) + " è presente")
        else:
            print (str(n) + "non è presente")
            



#importare filke csv
#https://docs.python.org/3/library/csv.html
import csv
my_csv = open ("C:/Users/tommaso/Desktop/GIS DataBase/lab 2/base dati/montecristo_point.csv","r")
print(type(my_csv))
#con questa riga io ho aperto, ora devo leggere
#creo nuova varavile "tab", e uso funz di modulo csv: "csv reader"
tab = csv.reader (my_csv, delimiter = ",") #imposto virgola come separatore
#utilizzando ciclo FOR 
for row in tab:
    print(row)
'''
    ['1', '606879.926248845', '4688202.49859414', '165']
['2', '607544.589320929', '4688664.52048571', '345']
['3', '608484.844398512', '4688072.80823861', '405']
['4', '608833.387228996', '4686970.44021662', '185']
['5', '608274.097570778', '4686240.93196677', '190']
['6', '607074.461782138', '4686078.81902236', '214']
['7', '606734.024598875', '4686435.46750006', '151']
['8', '607495.955437606', '4686565.15785559', '382']
['9', '608249.780629117', '4687083.91927771', '473']
['10', '608128.195920808', '4687926.90658864', '558']
['11', '607106.88437102', '4687359.5112832', '199']
['12', '607479.744143165', '4687999.85741363', '336']
['13', '608209.252393014', '4689110.33108284', '225']
['14', '607706.70226534', '4687181.18704435', '284']
['15', '608890.126759539', '4687797.21623311', '175']
['16', '607714.807912561', '4685997.76255015', '150']
['17', '609076.556645612', '4686565.15785559', '261']
['18', '608111.984626367', '4686678.63691668', '387']
['19', '607098.7787238', '4686848.85550831', '204']
['20', '608492.950045733', '4687602.68069982', '416']
['21', '608087.667684706', '4688559.14707184', '424']
['22', '607301.419904313', '4689118.43673006', '207']
['23', '607398.68767096', '4688315.97765523', '404']
['24', '607901.237798633', '4688137.65341638', '600']
['25', '607682.385323679', '4687545.94116928', '221']
['26', '608809.070287334', '4687246.03222212', '327']    
'''
#esegue ciclo for per ogni elemento riga, stapando per ogni for una riga diversa
#sono inserite tra apici, per py al momento sono valori di stringa, bisogna quindi trasformarli in num
#inserendo 1,2,3 posso stampare singole colonne -> es:
for row in tab:
    print(row[2])
#line 99 -> devo strasformare in num
#comado DicReader -> class csv.DictReader(f, fieldnames=None, restkey=None, restval=None, dialect='excel', *args, **kwds)
#Create an object that operates like a regular reader but maps the information in each row to a dict whose keys are given by the optional fieldnames parameter.
my_csv = open ("C:/Users/tommaso/Desktop/GIS DataBase/lab 2/base dati/name.csv","r")
tab = csv.DictReader (my_csv, delimiter = ",")
for row in tab:
    print(type(y))
#mi stampa ora colonna con nume inserito

#inserire intestazioni colonne con coordiante direttamente da py_compile
#comendo HEADER https://stackoverflow.com/questions/16220930/python-what-is-a-header/27462911
#per non sovrascrivere file originale devo ricopiare ogni riga aggiungendo nuva riga come header
#creo ciclo for per inserire lista "tab" 
my_csv = open ("C:/Users/tommaso/Desktop/GIS DataBase/lab 2/base dati/no_name.csv","r")
tab = csv.reader (my_csv, delimiter = ",")
header = ["id", "x", "y", "h"]
for row in tab:
    lista.append(row)

print(type(lista))
#vedi bene vicenda di crare lista di liste- per ogni riga di mia lista iniziale creo nuova lista, infatti verra indicata tra [], poi ad ogni lista con ciclo for aggiungo cio che mi interessa
#for row in tab:
#    lista.append(row)
#ora dovrò salveare nuova lista creata, che in realtà come visto è lista di liste, creo quindi nuova variabile
#NB. gli do nuovo nume per evitare di sovrascrivere
new_csv = open("C:/Users/tommaso/Desktop/GIS DataBase/lab 2/base dati/si_name.csv","w")
#creo nuova variabile e con comando csv.writer do comando di output
new_tab =csv.writer(new_csv, delimiter = ",")
#vedi comando writerow su link package csv
new_tab.writerow(header)
#quandoi finisco questa operazione per permettere di salvare devo chiudere file che ho aperto
my_csv.close()
new_csv.close()
#ora, in cartella indicata in line 127 avro nuovo file

        
        
        
        
        
        
        
        
        
        
#        
