
create keyspace if not exists operadora2 with replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

CREATE TABLE IF NOT EXISTS "operadora2"."operadora" (
id_op int primary key,
Ano int,
Mes text,
Acessos int,
Servico text,
Cod_IBGE int,
Municipio text,
UF text,
Regiao text
);

select count(*) from operadora;

select * from operadora;