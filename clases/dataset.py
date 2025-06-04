"Clase Padre"
from abc import ABC, abstractmethod
import pandas as pd


class Dataset(ABC):
    """clase principal abstarcta, una clase que no puede ser instanciada, es obligatorio que una subclase la herede para poder instanciar""" 

    def __init__(self, fuente):
        self.__fuente = fuente
        self.__datos = None

    # SET / GET
    @property
    def datos(self):
        """metodo publico para devolver atributo privado"""
        return self.__datos
    
    @datos.setter
    def datos(self, valor):
        """metodo para modificar datos(setter) con el valor pasado,si pasa las validaciones dadas"""
        if not isinstance(valor, pd.DataFrame):
            raise ValueError("El elemento no es un df de pandas")
        self.__datos = valor
    
    @property
    def fuente(self):
        """metodo devolver valor protegido """
        return self.__fuente
    
    # METODOS
    @abstractmethod
    def cargar_datos(self):
        """metodo abstracto para cargar los datos, obliga con el decorador a las subclases a implementar este metodo"""
        

    def validar_datos(self):
        """analizar datos devuelve boolean"""
        
        if self.datos is None:
            raise ValueError('Datos no estan')
            
        # control de nulos
        if self.datos.isnull().sum().sum() > 0:
            print('Existen valores nulos, hay datos faltantes, a continuacion se muestran las columnas con valores nulos')
            print(self.datos.isnull().sum())
            consulta_nulo = input('Desea eliminar los nulos. Ingrese si o no  ').strip().lower()
            if consulta_nulo == 'si':
                self.datos.dropna(inplace=True)
                print('Has eliminado los nulos')
                print(f'El dataframe esta asi: {self.datos}')
            else:
                print('Continuamos con los nulos')
                print(f'El dataframe esta asi: {self.datos}')

        # duplicated da boolean, y sumamos las respuestas con sum    
        if self.datos.duplicated().sum() > 0:            
            print(f'Hay {self.datos.duplicated().sum()} filas duplicadas')
            print(f'Las filas duplicadas son {self.datos[self.datos.duplicated()]}')
            consulta = input('Desea eliminar los duplicados? Ingrese si o no:  ').strip().lower()
            if consulta == 'si':
                self.datos.drop_duplicates(inplace=True)
                print('Continuamos, se han eliminado los duplicados')
            else:
                print('Continuamos, con los duplicados ')
        return True