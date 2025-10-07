import pandas as pd
import json
from abc import ABC, abstractmethod

class Adapter(ABC):
    @abstractmethod
    def get_data():
        pass

class CSVAdapter(Adapter):
    def __init__(self, path_csv):
        self.data = pd.read_csv(path_csv)
    
    def get_data(self):
        return self.data.to_dict(orient="records")

class APIAdapter(Adapter):
    def __init__(self, path_json):

        with open(path_json, "r", encoding="utf-8") as f:
            raw = json.load(f)

        self.data = pd.DataFrame(raw["funcionarios"])
    
    def get_data(self):
        return self.data.to_dict(orient="records")

class ObjectAdapter(Adapter):
    def __init__(self, string_data):
        self.data_string = self.parse_string(string_data)
    
    def parse_string(self, string_data):
        # Divide cada registro usando ';'
        registros = [r.strip() for r in string_data.split(";") if r.strip()]
        lista_dados = []

        for reg in registros:
            pairs = [item.split("=") for item in reg.split(",")]
            data_dict = {k.strip(): v.strip() for pair in pairs if len(pair) == 2 for k, v in [pair]}
            lista_dados.append(data_dict)
        
        return lista_dados
    
    def get_data(self):
        return self.data_string

        
