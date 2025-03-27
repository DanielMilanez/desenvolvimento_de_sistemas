-- comentário
-- SQL: Linguagem de programação de banco de dados

/*
	D - Dados
    T - Transação
    L - Linguagem
    
	DDL -> Cria, altera e destrói. - Definição
    DML -> Manipulação
    DQL -> Consultas
    DCL -> Controle
    DTL -> Dados, Transação, Linguagem.
*/

CREATE DATABASE barbearia; -- DDL

USE barbearia;

CREATE TABLE if not exists cliente(
	id int PRIMARY KEY auto_increment,
    nome VARCHAR(60) NOT NULL,
    whatsapp CHAR(13) NOT NULL,
    email VARCHAR(80)
)auto_increment=1;

DROP TABLE cliente;

show tables;

INSERT INTO cliente(nome, whatsapp, email)VALUES('joão', '61889987867', 'joao@gmail.com'); -- DML

SELECT * FROM cliente;

/*
	Exercício
    Considerando a nossa barbearia. o cliente pediu a elaboração de uma nova tabela de serviço
		- nome do serviço
        - valor do serviço
	Considerando nosso contexto, crie a tabela, pesquise na internet os melhores serviços de uma barbearia e insira no banco de dados (popular) - persisitr;
*/

CREATE TABLE if not exists servico(
	id integer PRIMARY KEY auto_increment,
    nome VARCHAR(65) NOT NULL,
    valor FLOAT NOT NULL
)auto_increment=1;

-- DROP TABLE servico;

INSERT INTO servico(nome, valor)VALUES('corte de cabelo', 30), ('massagem', 100), ('pintar unha', 25), ('unha postica', 50);

SELECT * FROM servico; -- DQL -> Q - Query

SELECT * FROM cliente WHERE id = 1;
SELECT nome FROM cliente WHERE id = 1;

/*
	Realize as seguintes consultas:
    - Pesquise todos os serviços cadastrados
    - Pesquise apenas o serviço de id = 3
    - Pesquise todos os serviços maiores que R$ 30.00
    - Pesquise todos os serviços, porém apenas a coluna nome
*/

SELECT * FROM servico;

SELECT * FROM servico WHERE id = 3;

SELECT * FROM servico WHERE valor > 30;

SELECT nome FROM servico;





