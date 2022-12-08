"""
Una de las primeras problemáticas que se enfrenta una investigación o proyecto en Ciencias Sociales
es la cantidad de formatos y documentos que se pueden utilizar.

Recuerda: 

Nombrar los archivos con nombres cortos y relevantes
No utilizar caracteres especiales: ~ ¡ ! @ # $ % ^ & * ( ) ` ; < > ¿ ? , [ ] { } ' " |
Usar el guion bajo, mejor que el espacio en blanco
Ser consistente con la nomenclatura que se escoge, mayúsculas, minúsculas, forma de las fechas, AAAA‐MM‐DD o  AAAA‐MM.

https://bib.us.es/estudia_e_investiga/investigacion/estrategias/gdi/organizar-y-documentar-los-datos

"""

#exporta la libreria Os 

import os 

#indica la ruta de los archivos a renombrar, recuerda que el archivo Py debe estar dentro de esta ruta

os.chdir('C:/Users/Dharma/OneDrive/Escritorio/codigo_bajo')

# genaera un id númerico

i=1

# itera por cada archivo en la ruta el cambio de nombre 

for file in os.listdir():
    src=file
    dst= "programa" +str(i)+".py" #coloca el prefijo que necesites y la id númerico
    os.rename (src, dst)
    i+=1