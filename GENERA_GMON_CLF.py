#!/usr/bin/env python
import mysql.connector
import csv



cnx=mysql.connector.connect(user='escalon2',password='3scal0n',host='47.60.8.56',database='escalondb2')
cur2=cnx.cursor()

gmon_clf= open('/home/palonso0/gmonclf_r6.csv','wb')

wr= csv.writer(gmon_clf,delimiter=';',dialect='excel')

#Consulta sobre Escal?n para obtener lista de nodos con coordenadas
cur2.execute("SELECT NODE,SITE_NAME,CELL_NAME,LAC,CI,LATITUDE,LONGITUDE FROM escalondb2.cell WHERE (NODE_ID LIKE 'BU%' OR NODE_ID LIKE 'VA%' OR NODE_ID LIKE 'SA%' OR NODE_ID LIKE 'SG%' OR NODE_ID LIKE 'AV%' OR NODE_ID LIKE 'CT%' OR NODE_ID LIKE 'CYL%' OR NODE_ID LIKE 'SO%' OR NODE_ID LIKE 'PX%' OR NODE_ID LIKE 'ZA%' OR NODE_ID LIKE 'LE%' OR NODE_ID LIKE 'SX%' OR NODE_ID LIKE 'LX%' OR NODE_ID LIKE 'NA%' OR NODE_ID LIKE 'LO%');")
rows_umts=cur2.fetchall()

for fila_umts in rows_umts:
    registro=['21401']
    sector_umts=fila_umts[2]
    nombre_umts=fila_umts[1]
    lac=fila_umts[3]
    ci=fila_umts[4]
    lat=fila_umts[5]
    lon=fila_umts[6]
    registro.append(ci)
    registro.append(lac)
    registro.append('0')
    registro.append(lat)
    registro.append(lon)
    registro.append('-1')
    registro.append(nombre_umts+'_'+sector_umts)
    registro.append('0')
    registro.append(' ')
    registro.append('-1')
    registro.append('-1')
    registro.append('-1')
    try:wr.writerow(registro)
    except:pass
	
    registro=[""]


gmon_clf.close()
cur2.close()
