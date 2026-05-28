import pandas as pd
import numpy as np

np.random.seed(1)


clientes = pd.DataFrame({
    "id_cliente": range(1, 101),
    "nome": [f"Cliente_{i}" for i in range(1, 101)],
    "estado": np.random.choice(["SP", "RJ", "MG", "BA", "PR", "SC"], 100),
    "idade": np.random.randint(18, 70, 100),
    "genero": np.random.choice(["M", "F"], 100)
})

produtos = pd.DataFrame({
    "id_produto": range(1, 21),
    "produto": [f"Produto_{i}" for i in range(1, 21)],
    "categoria": np.random.choice(["Eletrônicos", "Roupas", "Casa", "Esporte"], 20),
    "preco_unitario": np.random.uniform(25, 1500, 20).round(2)
})

vendas = pd.DataFrame({
    "id_venda": range(1, 1001),
    "id_cliente": np.random.randint(1, 101, 1000),
    "id_produto": np.random.randint(1, 21, 1000),
    "quantidade": np.random.randint(1, 6, 1000),
    "data_venda": pd.date_range("2024-01-01", periods=1000, freq="d")
})