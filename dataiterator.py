import pandas as pd
from adapters import Adapter

class DataIterator():
    """
    Classe que serve para juntar dados de locais diferentes e devolver os dados com um nível de abstração.
    """
    def __init__(self, data):
        """
        *adapters = fontes diferentes as quais queremos juntar nesse exemplo
        """
        self.iterable = data
        self.atual = 0

    def __iter__(self):
        """
        função reponsável por
        """
        return self
    
    def __next__(self):
        if self.atual == len(self.iterable):
            raise StopIteration("não há mais dados no iterador")

        prox = self.iterable[self.atual]
        
        self.atual += 1
        return prox


# nome = {"aa": 22, "bb" : 45, "cc" : 96}
# a = DataIterator(nome)


# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())

