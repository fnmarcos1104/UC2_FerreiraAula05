# pip install pandas sqlalchemy pymysql openpyxl
from sqlalchemy import create_engine
import pandas as pd

host = 'localhost'
user = 'root'
password = 'root'
database = 'bd_vendas'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# Carregar dados da tabela 'tb_clientes' do Banco Exemplo3 MySQL
query_clientes = "SELECT id_cliente, nome, email FROM tb_clientes"
df_clientes = pd.read_sql(query_clientes, engine)

# Carregar dados da tabela 'pedidos' do arquivo Excel
df_pedidos = pd.read_excel('tb_pedidos.xlsx')


print(df_clientes)
print(df_pedidos)