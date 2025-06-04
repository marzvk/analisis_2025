from os import path
from clases.dataset_csv import DatasetCSV
from clases.dataset_excel import DatasetExcel

csv_ruta = path.join(path.dirname(__file__), "archivos/Dengue_Dataset.csv")
excel_ruta = path.join(path.dirname(__file__),
                       "archivos/Road_Accident_Data_2022.xlsx")

# csv = DatasetCSV(csv_ruta)
# csv.cargar_datos()
# csv.mostrar_info()

excel = DatasetExcel(excel_ruta)
excel.cargar_datos()
# excel.mostrar_estructura()
