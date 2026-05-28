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

df = vendas.merge(clientes, on="id_cliente", how="left")
df = df.merge(produtos, on="id_produto", how="left")

df["valor_total"] = df["quantidade"] * df["preco_unitario"]
df["mes"] = df["data_venda"].dt.month
df["ano"] = df["data_venda"].dt.year
df["dia_semana"] = df["data_venda"].dt.day_name()

df["faixa_etaria"] = pd.cut(
    df["idade"],
    bins=[17, 25, 35, 45, 60, 100],
    labels=["18-25", "26-35", "36-45", "46-60", "60+"]
)

faturamento_total = df["valor_total"].sum()
ticket_medio = df["valor_total"].mean()
total_vendas = df["id_venda"].nunique()
total_clientes = df["id_cliente"].nunique()

print("--- RESUMO GERAL ---")
print(f"Faturamento total: R$ {faturamento_total:,.2f}")
print(f"Ticket médio: R$ {ticket_medio:,.2f}")
print(f"Total de vendas: {total_vendas}")
print(f"Clientes únicos: {total_clientes}")

vendas_por_estado = (
    df.groupby("estado")
    .agg(
        faturamento=("valor_total", "sum"),
        quantidade_vendida=("quantidade", "sum"),
        clientes_unicos=("id_cliente", "nunique")
    )
    .sort_values("faturamento", ascending=False)
)

vendas_por_categoria = (
    df.groupby("categoria")
    .agg(
        faturamento=("valor_total", "sum"),
        quantidade=("quantidade", "sum"),
        ticket_medio=("valor_total", "mean")
    )
    .sort_values("faturamento", ascending=False)
)

top_produtos = (
    df.groupby("produto")
    .agg(
        faturamento=("valor_total", "sum"),
        unidades_vendidas=("quantidade", "sum")
    )
    .sort_values("faturamento", ascending=False)
    .head(5)
)
