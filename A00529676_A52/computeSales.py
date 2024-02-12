# pylint: disable=invalid-name
""" Exercise: Compute sales """
import sys
import json
import time


def validate_json(file_path):
    """ Funcion para validar archivo json """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            json.load(file)
    except ValueError as e:
        print(f"JSON file {file_path} is not valid:", e)
        sys.exit(1)


def read_json(file_path):
    """ Funcion para leer archivo json """
    with open(file_path, 'r', encoding='utf-8') as file_to_read:
        data = json.load(file_to_read)
    return data


# captura tiempo de inicio
start_time = time.time()

# archivo para resultado
FILE_RESULT = 'SalesResults.txt'

# Verifica la cantidad de argumentos
if len(sys.argv) != 3:
    print("Usar: python computeSales.py <archivo productos> <archivo sales>")
    sys.exit(1)

# Lee el nombre de archivo de la linea de comandos
file_prices = sys.argv[1]
file_sales = sys.argv[2]

# Validar que sean  archivos json
validate_json(file_prices)
validate_json(file_sales)

# Lee los archivos y los pone en un diccionario
data_products = read_json(file_prices)
data_sales = read_json(file_sales)

# Agrega el precio de Producto a ventas total
ventas_total = 0
for sale in data_sales:
    for product in data_products:
        try:
            if sale['Product'] == product['title']:
                # suma las ventas totales
                ventas_total += sale['Quantity'] * product['price']
        except IOError as ex:
            print("Ocurrio error en el proceso de calculo. ", ex)
# captura tiempo final
end_time = time.time()

# calcula el tiempo transcurrido
elapsed_time = end_time - start_time

# muestra el tiempo transcurrido y agrega a archivo
with open(FILE_RESULT, 'a', encoding="utf-8") as f:
    print(f"\tTOTAL:\n{file_sales[:3]}\t" + f"{ventas_total:.2f}")
    print(f"\tTOTAL:\n{file_sales[:3]}\t" + f"{ventas_total:.2f}", file=f)
    print(f"Elapsed Time: {elapsed_time} seconds\n")
    print(f"Elapsed Time: {elapsed_time} seconds\n\n", file=f)
