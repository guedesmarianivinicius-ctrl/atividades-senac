import pandas as pd

dados = pd.read_csv("academia.csv")
print(dados)
print(dados.head()) 
print(dados.tail())
print(dados.shape)

print(dados["Idade"].mean())
print(dados["Calorias"].mean()) 
print(dados["Peso"].max()) 
print(dados["Peso"].min())