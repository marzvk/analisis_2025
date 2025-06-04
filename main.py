from os import path
from clases.dataset_csv import DatasetCSV

csv_ruta = path.join(path.dirname(__file__),"archivos/prueba.csv")

csv = DatasetCSV(csv_ruta)
csv.cargar_datos()

