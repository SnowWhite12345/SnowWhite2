class Inverso:
    def __init__(self, invert:str) -> None:
        self.__invert = invert

    @property
    def invert(self):
        return self.__invert

    @invert.setter
    def invert(self, invert:list):
        self.__invert = invert

    def inverter(self):
        list(self.invert)
        lista_invertida = list(reversed(self.invert))
        return "".join(lista_invertida)