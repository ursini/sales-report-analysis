📊 Sales Report Analysis
Projeto de análise de vendas desenvolvido em Python, utilizando dados simulados para gerar relatórios completos com insights sobre faturamento, clientes, produtos e categorias.

📝 Descrição
Este projeto gera e analisa um conjunto de dados simulados de vendas com 1.000 transações, 100 clientes e 20 produtos, aplicando técnicas de manipulação e análise de dados com pandas e numpy.
O pipeline completo inclui geração dos dados, transformações, análises agregadas, segmentação de clientes, detecção de outliers e exportação para Excel com múltiplas abas.

🗂️ Dados Simulados
Os dados são gerados automaticamente via numpy com seed fixo (np.random.seed(42)) para garantir reprodutibilidade. São três datasets principais:
DatasetRegistrosDescriçãoclientes100ID, nome, estado, idade e gêneroprodutos20ID, nome, categoria e preço unitáriovendas1.000ID, cliente, produto, quantidade e data
Os três datasets são integrados via merge e enriquecidos com colunas calculadas como valor_total, mes, ano, dia_semana e faixa_etaria.

🔍 Análises Realizadas
📌 Indicadores Gerais
Métricas consolidadas de todo o período:

Faturamento total
Ticket médio por venda
Total de vendas únicas
Total de clientes únicos

🗺️ Vendas por Estado
Agrupamento por estado com faturamento, quantidade vendida e clientes únicos.
🏷️ Vendas por Categoria
Faturamento, quantidade e ticket médio por categoria de produto (Eletrônicos, Roupas, Casa, Esporte).
🏆 Top 10 Produtos
Ranking dos produtos com maior faturamento e unidades vendidas.
👑 Clientes VIP
Top 10 clientes por valor total gasto, com número de compras e ticket médio individual.
📅 Faturamento Mensal
Evolução do faturamento mês a mês com variação percentual em relação ao mês anterior.
🎯 Segmentação de Clientes
Classificação automática de cada cliente com base no total gasto:
CategoriaValor Total GastoVIPAcima de R$ 20.000PremiumEntre R$ 10.000 e R$ 20.000RegularEntre R$ 5.000 e R$ 10.000NovoAbaixo de R$ 5.000
🔲 Pivot Table
Tabela cruzada de faturamento por estado × categoria, permitindo identificar quais categorias performam melhor em cada região.
📉 Detecção de Outliers
Identificação de vendas atípicas usando o método IQR (Interquartile Range):

Limite inferior: Q1 - 1.5 * IQR
Limite superior: Q3 + 1.5 * IQR


📊 Exemplo de Output no Terminal
--- RESUMO GERAL ---
Faturamento total: R$ 2,377,488.96
Ticket médio: R$ 2,377.49
Total de vendas: 1000
Clientes únicos: 100

--- VENDAS POR ESTADO ---
        faturamento  quantidade_vendida  clientes_unicos
estado
BA        625544.77                 814               25
RJ        432106.84                 535               19
PR        417596.49                 556               17
SC        414070.53                 506               17
MG        249073.89                 316               11
SP        239096.44                 322               11

--- VENDAS POR CATEGORIA ---
             faturamento  quantidade  ticket_medio
categoria
Roupas         749271.39         785   2892.94
Casa           726509.70         750   2941.33
Esporte        656248.98         950   2180.23
Eletrônicos    245458.89         564   1271.81

📁 Relatório Excel
O arquivo data/relatorio_vendas_pandas.xlsx é gerado automaticamente com as seguintes abas:
AbaConteúdoBase TratadaDataset completo após todas as transformaçõesVendas por EstadoFaturamento e quantidade por estadoVendas por CategoriaMétricas por categoria de produtoTop ProdutosTop 10 produtos por faturamentoClientes VIPTop 10 clientes por valor gastoFaturamento MensalEvolução mensal com variação %Pivot Estado CategoriaTabela cruzada estado × categoriaOutliersVendas fora do padrão identificadas pelo IQR

🛠️ Tecnologias

Python 3.x
Pandas
NumPy
OpenPyXL — geração do Excel


📁 Estrutura de Pastas
project/
├── data/
│   └── relatorio_vendas_pandas.xlsx  # Relatório gerado automaticamente
├── src/
│   └── main.py                       # Script principal
├── README.md
└── requirements.txt

▶️ Como Rodar

Clone o repositório:

bashgit clone https://github.com/ursini/sales-report-analysis.git
cd sales-report-analysis

Instale as dependências:

bashpip install -r requirements.txt

Execute o script:

bashpython src/main.py

O relatório Excel será gerado automaticamente em data/relatorio_vendas_pandas.xlsx.