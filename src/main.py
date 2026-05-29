import pandas as pd
import numpy as np
pd.ExcelWriter("data/relatorio_vendas_pandas.xlsx")

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
clientes_vip = (
    df.groupby(["id_cliente", "nome"])
    .agg(
        total_gasto=("valor_total", "sum"),
        compras=("id_venda", "count"),
        ticket_medio=("valor_total", "mean")
    )
    .sort_values("total_gasto", ascending=False)
    .head(5)
)

faturamento_mensal = (
    df.groupby(["ano", "mes"])
    .agg(
        faturamento=("valor_total", "sum"),
        vendas=("id_venda", "count")
    )
    .reset_index()
)

faturamento_mensal["crescimento_%"] = (
    faturamento_mensal["faturamento"]
    .pct_change()
    .mul(100)
    .round(2)
)

def classificar_cliente(valor):
    if valor >= 20000:
        return "VIP"
    elif valor >= 10000:
        return "Premium"
    elif valor >= 5000:
        return "Regular"
    return "Novo"

gasto_clientes = (
    df.groupby("id_cliente")["valor_total"]
    .sum()
    .reset_index(name="total_gasto")
)

gasto_clientes["categoria_cliente"] = gasto_clientes["total_gasto"].apply(classificar_cliente)

df = df.merge(gasto_clientes[["id_cliente", "categoria_cliente"]], on="id_cliente", how="left")

pivot_estado_categoria = pd.pivot_table(
    df,
    values="valor_total",
    index="estado",
    columns="categoria",
    aggfunc="sum",
    fill_value=0
)

q1 = df["valor_total"].quantile(0.25)
q3 = df["valor_total"].quantile(0.75)
iqr = q3 - q1

limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

outliers = df[
    (df["valor_total"] < limite_inferior) |
    (df["valor_total"] > limite_superior)
]

with pd.ExcelWriter("relatorio_vendas_pandas.xlsx") as writer:
    df.to_excel(writer, sheet_name="Base Tratada", index=False)
    vendas_por_estado.to_excel(writer, sheet_name="Vendas por Estado")
    vendas_por_categoria.to_excel(writer, sheet_name="Vendas por Categoria")
    top_produtos.to_excel(writer, sheet_name="Top Produtos")
    clientes_vip.to_excel(writer, sheet_name="Clientes VIP")
    faturamento_mensal.to_excel(writer, sheet_name="Faturamento Mensal", index=False)
    pivot_estado_categoria.to_excel(writer, sheet_name="Pivot Estado Categoria")
    outliers.to_excel(writer, sheet_name="Outliers", index=False)

print("Relatório Excel gerado com sucesso!")

print("\n--- VENDAS POR ESTADO ---")
print(vendas_por_estado)

print("\n--- VENDAS POR CATEGORIA ---")
print(vendas_por_categoria)

print("\n--- TOP 10 PRODUTOS ---")
print(top_produtos)

print("\n--- CLIENTES VIP ---")
print(clientes_vip)

print("\n--- FATURAMENTO MENSAL ---")
print(faturamento_mensal)

print("\n--- OUTLIERS ENCONTRADOS ---")
print(outliers[["id_venda", "nome", "produto", "valor_total"]].head())