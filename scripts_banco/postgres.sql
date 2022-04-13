create table if not exists operadora (
	id_op serial constraint PK_operadoras primary key,
	Ano int not null,
    Mes varchar (100) not null,
    Acessos int not null,
    Servico varchar (400) not null,
    Cod_IBGE int not null,
    Municipio varchar (400) not null,
    UF varchar (100) not null,
    Regiao varchar (200) not null
    );