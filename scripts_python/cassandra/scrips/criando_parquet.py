
from pyspark.sql import SparkSession

# abrindo conexão com o spark para ler no postgres
spark = SparkSession \
    .builder \
    .appName("parquet para postgres") \
    .config("spark.jars", r"gs://pasta-scripts/postgresql-42.3.2.jar") \
    .getOrCreate()

# lendo do postgres e criando um dataframe
df = spark.read \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://34.151.208.93:5432/operadora2") \
    .option("dbtable", "operadora") \
    .option("user", "postgres") \
    .option("password", "ROOT") \
    .option("driver", "org.postgresql.Driver") \
    .load()

#df.printSchema()



def lendo_transformando_parquet(nome_tabela, caminho_parquet):
    
    url = 'jdbc:postgresql://34.151.208.93:5432/operadora2'
    
    properties = {
    
    'user': 'postgres',
    'password': 'ROOT',
    'driver': 'org.postgresql.Driver'
    }

    df = spark.read.jdbc(url=url, table=nome_tabela, properties=properties)
    
    df.write.parquet(caminho_parquet)

    return f"Parquet add em {caminho_parquet}"

lendo_transformando_parquet('operadora', 'gs://pasta-scripts/parquetofic')