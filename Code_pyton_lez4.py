#importo csv (ricordati vicende liste)
import math
import csv
my_csv = open ("C:/Users/tommaso/Desktop/GIS DataBase/lab 2/base dati/name.csv","r")
print(type(my_csv))
tab = csv.reader (my_csv, delimiter = ",") 
for row in tab:
    print(row)
#quota elliodica diversa quota geoidica-> noi si ha quota ortometrica-> algoritmo che modifica e la trasforma in ellissioidica 
#questo è quello che ho al momento-> creare nuova colonnna
#''' inizio e ''' fine ->non leggere da.. ...a...
'''
['id', 'x', 'y', 'h']
['1', '606879.9262', '4688202.499', '165']
['2', '607544.5893', '4688664.52', '345']
['3', '608484.8444', '4688072.808', '405']
['4', '608833.3872', '4686970.44', '185']
['5', '608274.0976', '4686240.932', '190']
['6', '607074.4618', '4686078.819', '214']
['7', '606734.0246', '4686435.468', '151']
['8', '607495.9554', '4686565.158', '382']
['9', '608249.7806', '4687083.919', '473']
['10', '608128.1959', '4687926.907', '558']
['11', '607106.8844', '4687359.511', '199']
['12', '607479.7441', '4687999.857', '336']
['13', '608209.2524', '4689110.331', '225']
['14', '607706.7023', '4687181.187', '284']
['15', '608890.1268', '4687797.216', '175']
['16', '607714.8079', '4685997.763', '150']
['17', '609076.5566', '4686565.158', '261']
['18', '608111.9846', '4686678.637', '387']
['19', '607098.7787', '4686848.856', '204']
['20', '608492.95', '4687602.681', '416']
['21', '608087.6677', '4688559.147', '424']
['22', '607301.4199', '4689118.437', '207']
['23', '607398.6877', '4688315.978', '404']
['24', '607901.2378', '4688137.653', '600']
['25', '607682.3853', '4687545.941', '221']
['26', '608809.0703', '4687246.032', '327']    
'''    
#nel caso di isola di montecristo, dove è georeferianto mio csv(punti rappresentati da mio file) ellissoide sopra geoide di 48 m
for row in tab:
    #creo lista di liste(cordiate miei punti), e aggiungo valore di differenza
    h_ell = int(row[3]) + 48
    print(h_ell)
    
#per aggiornare mio csv creo lista di liste    
import csv
my_csv = open ("C:/Users/tommaso/Desktop/GIS DataBase/lab 2/base dati/montecristo_point.csv","r")
print(type(my_csv))
tab = csv.reader (my_csv, delimiter = ",") 

lista = []


for row in tab:
    h_elips = int(row[3]) + 48
    row.append(h_elips)
    lista.append (row)

out_data = open ("C:/Users/tommaso/Desktop/GIS DataBase/lab 2/base dati/montecristo_point_ell.csv","w")
tab_new = csv.reader (my_csv, delimiter = ",")
tab_new.writerow(header)
tab_new.writerow(lista)

my_csv.close()
tab_new.close()
print("fatto")


#nuovo con panda -> https://pandas.pydata.org/

import pandas
data = pandas.read_csv("C:/Users/tommaso/Desktop/GIS DataBase/lab 2/base dati/name.csv")
#aggiungere nuova colonna in questo caso è molto più semplice
data["h_elips"] = data["h"] + 48

print (data)
#per creare nuovo file_senza sovrascivere(cambiando nome)
import pandas
data = pandas.read_csv("C:/Users/tommaso/Desktop/GIS DataBase/lab 2/base dati/name.csv")
#aggiungere nuova colonna in questo caso è molto più semplice
data["h_elips"] = data["h"] + 48

data.to_csv("C:/Users/tommaso/Desktop/GIS DataBase/lab 2/base dati/name_elips_panda.csv")
print("fatto")
#vedi file output in base dati in gis data base





















    
