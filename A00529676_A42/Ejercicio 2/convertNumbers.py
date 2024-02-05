#pylint: disable=invalid-name
""" Exercise: Converter """
import sys
import os
import time

# captura tiempo de inicio
start_time = time.time()

# archivo para resultado
FILE_RESULT = 'ConvertionResults.txt'

# Verifica la cantidad de argumentos
if len(sys.argv) != 2:
    print("Usar: python computeStatistics.py <nombre de archivo>")
    sys.exit(1)

# Lee el nombre de archivo de la linea de comandos
file_name = sys.argv[1]

numbers_list = []

try:
    # Abrir archivo en modo lectura
    with open(file_name, 'r', encoding="utf-8") as file:
        # Lee el contenido por renglon
        lines = file.readlines()
        # lee linea por linea, si existe un error al convertir a numerico, lo ignora y continua
        for index, line in enumerate(lines):
            try:
                numeric_value = int(line)
                binary_digits = []
                hex_digits = []
                n = abs(numeric_value)
                while n > 0:
                    binary_digits.insert(0, str(n % 2))
                    n //= 2
                bin_value = ''.join(binary_digits) if binary_digits else '0'
                n = abs(numeric_value)
                while n > 0:
                    remainder = n % 16
                    hex_digit = str(remainder) if remainder < 10 else chr(ord('A') + remainder - 10)
                    hex_digits.insert(0, hex_digit)
                    n //= 16
                hex_value = ''.join(hex_digits) if hex_digits else '0'
                if numeric_value < 0:
                    # realiza la conversion a negativo para menores de 0
                    bin_value = bin_value.rjust(10, '1')
                    # hex a negativo, realiza complemento
                    complement_hex = ''.join(['F' if digit == '0' else format(16 - int(digit, 16), 'X') for digit in hex_value]) #pylint: disable=line-too-long
                    hex_value = complement_hex.rjust(10, 'F')

                number_values = [f"{index}", f"{numeric_value}", f"{bin_value}", f"{hex_value}"]
            except ValueError:
                print(f"Valor no numerico encontrado: {line}")
                number_values = [f"{index}", line.replace('\n', ''), "#Value", "#Value"]
            numbers_list.append(number_values)

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
    print('\t'.join(["NUMBER", f"{file_noext}", "BIN", "HEX"]))
    print('\t'.join(["NUMBER", f"{file_noext}", "BIN", "HEX"]), file=file)
    for row in numbers_list:
        print('\t'.join(row))
        print('\t'.join(row), file=file)

# captura tiempo final
end_time = time.time()

# calcula el tiempo transcurrido
elapsed_time = end_time - start_time

# muestra el tiempo transcurrido y agrega a archivo
with open(FILE_RESULT, 'a', encoding="utf-8") as file:
    print(f"Elapsed Time: {elapsed_time} seconds\n")
    print(f"Elapsed Time: {elapsed_time} seconds\n\n", file=file)
