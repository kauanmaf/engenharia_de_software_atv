import pandas as pd
from adapters import CSVAdapter, APIAdapter, ObjectAdapter
from dataiterator import DataIterator

csv_path = "data/teste.csv"
json_path = "data/teste.json"
outsource_data = (
    "id=100, nome=Ana Souza, cargo=Analista de Dados, salario=6500;"
    "id=101, nome=Bruno Lima, cargo=Engenheiro de Dados, salario=8500;"
    "id=102, nome=Carla Menezes, cargo=Cientista de Dados, salario=9000;"
    "id=103, nome=Daniel Rocha, cargo=Gerente de Projetos, salario=12000;"
    "id=104, nome=Eduarda Silva, cargo=Engenheira de Software, salario=9500;"
    "id=105, nome=Fábio Martins, cargo=Coordenador de TI, salario=11000"
)

csv_adap = CSVAdapter(csv_path)
json_adap = APIAdapter(json_path)
string_data = ObjectAdapter(outsource_data)

x = DataIterator(csv_adap,json_adap, string_data)

for element in range(15):
    print(next(x))