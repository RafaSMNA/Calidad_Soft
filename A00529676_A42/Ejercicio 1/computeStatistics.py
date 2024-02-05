#pylint: disable=invalid-name
""" Exercise: Compute statistics """
import sys
import time
import numpy as np


# captura tiempo de inicio
start_time = time.time()

# archivo para resultado
FILE_RESULT = 'StatisticsResults.txt'

# Verifica la cantidad de argumentos
if len(sys.argv) != 2:
    print("Usar: python computeStatistics.py <nombre de archivo>")
    sys.exit(1)

# Lee el nombre de archivo de la linea de comandos
file_name = sys.argv[1]
numeric_array = np.array([])

try:
    # Abrir archivo en modo lectura
    with open("P1/" + file_name, 'r', encoding="utf-8") as file:
        # Lee el contenido por renglon
        lines = file.readlines()
        # lee linea por linea, si existe un error al convertir a numerico, lo ignora y continua
        for line in lines:
            try:
                numeric_value = float(line)
                numeric_array = np.append(numeric_array, numeric_value)
            except ValueError:
                print(f"Valor no numerico encontrado: {line}")

# verificacion de errores al leer archivo
except FileNotFoundError:
    print(f"Archivo '{file_name}' no encontrado.")
    sys.exit(1)
except IOError:
    print(f"Ocurrio error al leer '{file_name}'")
    sys.exit(1)

# Calcular mean, median, mode, standard deviation, and variance
# count
count_value = len(numeric_array)

# mean
mean_value = sum(numeric_array) / len(numeric_array)

# median
sorted_array = sorted(numeric_array)
n = len(sorted_array)
median_value = (sorted_array[n // 2] + sorted_array[(n - 1) // 2]) / 2 if n % 2 == 0 else sorted_array[n // 2] #pylint: disable=line-too-long

# mode
def calculate_mode(arr):
    """ Funcion para calcular mode """
    frequency = {}
    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    mode_value = [num for num, freq in frequency.items() if freq == max_freq]
    return mode_value

mode_values = calculate_mode(numeric_array)

# standard deviation & variance
mean_diff_squared = [(x - mean_value) ** 2 for x in numeric_array]
variance_value = sum(mean_diff_squared) / len(numeric_array)
std_deviation = variance_value ** 0.5

# Muestra los resultados y escribe en archivo
text_result = f"Data file: {file_name}\n"
text_result += f"Count: {count_value}\n"
text_result += f"Mean: {mean_value}\n"
text_result += f"Median: {median_value}\n"
text_result += f"Mode: {mode_values[0]}\n"
text_result += f"Standard Deviation: {std_deviation}\n"
text_result += f"Variance: {variance_value}"
with open(FILE_RESULT, 'a', encoding="utf-8") as file:
    print(text_result)
    print(text_result, file=file)
# captura tiempo final
end_time = time.time()

# calcula el tiempo transcurrido
elapsed_time = end_time - start_time

# muestra el tiempo transcurrido y agrega a archivo
with open(FILE_RESULT, 'a', encoding="utf-8") as file:
    print(f"Elapsed Time: {elapsed_time} seconds\n")
    print(f"Elapsed Time: {elapsed_time} seconds\n\n", file=file)
