"Archivo para ejecutar todos los metodos"
from os import path
from clases.dataset_csv import DatasetCSV
from clases.dataset_excel import DatasetExcel
from data.data_saver import Datasaver

# # armar ruta
csv_ruta = path.join(path.dirname(__file__), "archivos/Dengue_Dataset.csv")
excel_ruta = path.join(path.dirname(__file__),
                       "archivos/Road_Accident_Data_2022.xlsx")

# # cargar y gestionar

csv = DatasetCSV(csv_ruta)
csv.cargar_datos()
# csv.mostrar_info()

excel = DatasetExcel(excel_ruta)
excel.cargar_datos()
# excel.mostrar_estructura()

# # llevar a la base de datos
db = Datasaver()
db.guardar_df(csv.datos, "Dengue_Dataset_csv")
db.guardar_df(excel.datos, "Road_Accident_Data_2022_xlsx")
