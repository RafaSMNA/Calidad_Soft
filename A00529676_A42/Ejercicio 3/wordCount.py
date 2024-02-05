#pylint: disable=invalid-name
""" Exercise: Count Words """
import sys
import os
import time

# captura tiempo de inicio
start_time = time.time()

# archivo para resultado
FILE_RESULT = 'WordCountResults.txt'

# Verifica la cantidad de argumentos
if len(sys.argv) != 2:
    print("Usar: python wordCount.py <nombre de archivo>")
    sys.exit(1)

# Lee el nombre de archivo de la linea de comandos
file_name = sys.argv[1]

word_list = {}

try:
    # Abrir archivo en modo lectura
    with open(file_name, 'r', encoding="utf-8") as file:
        # lee linea por linea, si existe un error lo ignora y continua
        for line in file:
            try:
                words = line.split()
                for word in words:
                    # Update word count
                    if word:
                        word_list[word] = word_list.get(word, 0) + 1
            except ValueError:
                print(f"Error al leer la palabra: {line}")
        word_list = sorted(word_list.items(), key=lambda x:x[1], reverse=True)
# verificacion de errores al leer archivo
except FileNotFoundError:
    print(f"Archivo '{file_name}' no encontrado.")
    sys.exit(1)
except IOError:
    print(f"Ocurrio error al leer '{file_name}'")
    sys.exit(1)

# Muestra los resultados y escribe en archivo
file_noext = os.path.splitext(file_name)[0]
with open(FILE_RESULT, 'a', encoding="utf-8") as file:
    print('\t'.join(["Row Labels", f"Count of {file_noext}"]))
    print('\t'.join(["Row Labels", f"Count of {file_noext}"]), file=file)
    for row in word_list:
        row_s = [row[0], str(row[1])]
        print('\t'.join(row_s))
        print('\t'.join(row_s), file=file)

# captura tiempo final
end_time = time.time()

# calcula el tiempo transcurrido
elapsed_time = end_time - start_time

# muestra el tiempo transcurrido y agrega a archivo
with open(FILE_RESULT, 'a', encoding="utf-8") as file:
    print(f"Elapsed Time: {elapsed_time} seconds\n")
    print(f"Elapsed Time: {elapsed_time} seconds\n\n", file=file)
