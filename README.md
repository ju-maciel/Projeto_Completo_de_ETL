# Projeto Completo de ETL

### <b>Projeto de extração, tratamento e carregamento de um dataset com 67.000 dados, utilizando PySpark e Google Cloud

### Etapas na máquina local:</b>

1°- Extração do aquivo csv.

2°- Tratamento dos dados com as bibliotecas Pandas e Numpy (criação do DataFrame, normalizar nomenclatura das colunas, exclusão de caracteres indevidos, 
análises, filtros no DataFrame, drop, exclusão de Nan). 

3°- Criação dos Bancos de Dados: Postgres e Cassandra. 

4°- Criação do código em Python para inserção dos dados no Postgres utilizando a biblioteca PSYCOPG2 para auxiliar o Python na conexão com o SGDB Postgres.

5°- Criação do Parquet utilizando o framework PySpark com o auxilio do conector JDBC.

6°- Migração dos dados inseridos no postgres já em Parquet para o banco de dados NoSQL Cassandra.

### <b>Após a realizão do Projeto feito na minha máquina local realizei o processo todo na Nuvem Google Cloud.

### Etapas Nuvem GCP:</b>

1° Criação do Cluster (Cluster é um nó - uma máquina virtual).

2° Criar instância do Cloud SQL.

3° Enviar todos os arquivos do projeto para o Bucket - Utilizando a ferramenta Cloud Storage.

4° Realizar o 1º JOB - Inserção dos dados no BD Postgres.

5° Realizar o 2º JOB - Ler do Postgres e criar Parquet.

6º Criar instância do SGBD Cassandra.

7° Uso da IDE Jupyter na Nuvem para ler o Parquet e inserir no Cassandra e fazer a interação com os dados para gerar análises. 
