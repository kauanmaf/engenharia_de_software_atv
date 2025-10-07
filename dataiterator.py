import pandas as pd
from adapters import Adapter

class DataIterator():
    def __init__(self, *adapters):
        self.iterable = self.get_data(adapters)
        self.atual = 0

    def get_data(self, adapters):
        total = []

        for adapter in adapters:
            if not isinstance(adapter, Adapter):
                raise TypeError(f"Existe um objeto do tipo {type(adapter)}. Esperamos apenas subclasses do tipo Adapter")
            df_dict = adapter.get_data()
            df = pd.DataFrame(df_dict)
            total.extend(df.to_dict(orient="records"))
        return total

    def __iter__(self):
        return self
    
    def __next__(self):
        # print(self.iterable)
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

