"subclase para extraer archivos csv"
import pandas as pd
from clases.dataset import Dataset


class DatasetCSV(Dataset):
    """Subclase de Dataset para el csv"""

    def __init__(self, fuente):
        super().__init__(fuente)
        # con la fuente iniciamos la clase Dataset

    # METODOS
    def cargar_datos(self):

        try:
            df = pd.read_csv(self.fuente)
            # fuente , df => datos
            self.datos = df

            if self.validar_datos():
                print('iniciando carga a db')

        except Exception as e:
            print(f'Error {e} leyendo archivo')
