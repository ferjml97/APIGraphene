import csv

# Nombres de los archivos
archivo_entrada = "stops.csv"
archivo_salida = "stops_mod.csv"
archivo_valores = "alcaldias.txt"

# Leer los valores para la nueva columna desde el archivo de texto
def leer_valores(archivo):
    """
    Lee los valores desde un archivo de texto y los devuelve como una lista.
    
    :param archivo: Nombre del archivo de texto
    :return: Lista de valores
    """
    valores = []
    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            valores.append(linea.strip())
    return valores

# Nueva columna
nueva_columna = "alcaldia"
valores = leer_valores(archivo_valores)

# Leer el archivo CSV original y agregar la nueva columna con los valores
with open(archivo_entrada, "r", encoding="utf-8") as entrada, open(archivo_salida, "w", newline='', encoding="utf-8") as salida:
    lector_csv = csv.reader(entrada)
    escritor_csv = csv.writer(salida)
    
    # Leer la primera fila (cabecera)
    cabecera = next(lector_csv)
    # Agregar el nombre de la nueva columna a la cabecera
    cabecera.append(nueva_columna)
    # Escribir la nueva cabecera en el archivo de salida
    escritor_csv.writerow(cabecera)
    
    # Leer y escribir las filas con la nueva columna
    for i, fila in enumerate(lector_csv):
        if i < len(valores):  # Asegurarse de que hay un valor disponible
            fila.append(valores[i])
        else:
            fila.append("")  # Agregar un valor vacío si no hay más valores disponibles
        escritor_csv.writerow(fila)

print("El archivo CSV actualizado se ha guardado en 'stops_mod.csv'.")
