import os

# Obtener la lista de nombres de carpetas, subcarpetas y archivos
# en el directorio actual
nombres = os.listdir('.')

# Crear un archivo de texto llamado "folder_names.txt"
# en el directorio actual
with open('nombres_folder.txt', 'w') as f:
    for nombre in nombres:
        # Escribir cada nombre en una línea en el archivo
        f.write(nombre + '\n')