""" clase para conectar a la base de datos"""

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from decouple import config
# con decouple leemos las variables de entorno
# create engine genera motor para la conexion a la db


class Datasaver:
    """conectar a mysql"""

    def __init__(self):
        user = config('DB_USER')
        password = config('DB_PASSWORD')
        host = config('DB_HOST')
        port = config('DB_PORT')
        database = config('DB_NAME')

        # nombre del gestor + nombre del conector para mysql
        url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        # engine usa self porq se accede desde afuera
        self.engine = create_engine(url)

    # metodos
    def guardar_df(self, df, nombre_tabla):
        """carga en una tabla con el nombre asignado"""

        # validaciones
        if df is None:
            print(f'datos vacios en {nombre_tabla}')
            return

        # control si es df de pd
        if not isinstance(df, pd.DataFrame):
            print(f'{type(df)} : no es un df de pandas')

        # conexion y guardado
        try:
            df.to_sql(nombre_tabla,
                      con=self.engine,
                      if_exists="replace",
                      index=False)
            print(f'conexion guardado en db {nombre_tabla} exitosa')

        except SQLAlchemyError as e:
            print(f' Error en datos: {e}')
