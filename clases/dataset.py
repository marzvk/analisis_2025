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
        pass

    def validar_datos(self):
        