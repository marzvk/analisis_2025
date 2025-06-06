"subclase para extraer archivos csv"
import pandas as pd
from clases.dataset import Dataset


class DatasetExcel(Dataset):
    """Subclase de Dataset para el excel"""

    def __init__(self, fuente):
        super().__init__(fuente)
        # con la fuente iniciamos la clase Dataset

    # METODOS
    def cargar_datos(self):

        try:
            df = pd.read_excel(self.fuente)

            # fuente , df => datos

            def completar_nulos(df):
                for col in df.columns:
                    if df[col].dtype == 'O':  # columna con type texto
                        df[col] = df[col].fillna('sin datos')

                        # metodo de pd para ver si es typo numerico
                    elif pd.api.types.is_numeric_dtype(df[col]):
                        df[col] = df[col].fillna(0)

                        # para ver si col es de tipo datetime
                    elif pd.api.types.is_datetime64_any_dtype(df[col]):
                        df[col] = df[col].fillna(pd.Timestamp('1900-01-01'))
                return df

            df = completar_nulos(df)
            self.datos = df

            if self.validar_datos():
                print('iniciando carga a db')

        except Exception as e:
            print(f'Error {e} leyendo archivo')
