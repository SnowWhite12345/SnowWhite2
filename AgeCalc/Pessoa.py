from datetime import datetime as dt
class Pessoa:
    def __init__(self, datanasc:dt, nome: str)-> None:
        self.__nome = nome
        self.__datanasc = datanasc

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome:str):
        self.__nome = nome

    @property
    def datanasc(self):
        return self.__datanasc
    
    @datanasc.setter
    def datanasc(self, datanasc:dt):
        self.__datanasc = datanasc

    def idade(self):
        hoje = dt.today()
        return hoje.year - self.__datanasc.year
    