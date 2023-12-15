class Factor:
    def __init__(self, fatoracao:int) -> int:
        self.__fatoracao = fatoracao

    @property
    def fatoracao(self):
        return self.__fatoracao
    
    @fatoracao.setter
    def fatoracao(self, fatoracao:int):
        self.__fatoracao = fatoracao

    def fatorar(self):
        j = 1
        fact = self.fatoracao
        for i in range (fact, 0, -1):
                j*=i
        return j