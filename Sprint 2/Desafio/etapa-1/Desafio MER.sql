CREATE TABLE Combustivel(
	idCombustivel INTEGER PRIMARY KEY,
	tipoCombustivel VARCHAR
)

INSERT INTO Combustivel (idCombustivel, tipoCombustivel)
SELECT
	DISTINCT idCombustivel,
	tipoCombustivel
FROM tb_locacao

CREATE TABLE Marca (
    idMarca INTEGER PRIMARY KEY,
    marcaCarro VARCHAR
)

INSERT INTO Marca (marcaCarro)
SELECT
	DISTINCT marcaCarro
FROM tb_locacao

CREATE TABLE Carro (
	idCarro INTEGER PRIMARY KEY,
	kmCarro INTEGER,
	classiCarro VARCHAR,
	modeloCarro VARCHAR,
	anoCarro INTEGER,
	idCombustivel INTEGER NOT NULL,
	idMarca INTEGER NOT NULL,
    FOREIGN KEY (idCombustivel) REFERENCES Combustivel(idCombustivel),
    FOREIGN KEY (idMarca) REFERENCES Marca(idMarca)
	)
	
INSERT INTO Carro (idCarro, kmCarro, classiCarro, modeloCarro, anoCarro, idCombustivel, idMarca)
SELECT
	DISTINCT idCarro,
	kmCarro,
	classiCarro,
	modeloCarro,
	anoCarro,
	idcombustivel,
	(SELECT idMarca FROM Marca WHERE Marca.marcaCarro = tl.marcaCarro)
FROM tb_locacao tl
WHERE (idCarro, kmCarro) IN 
        (SELECT idCarro, MAX(kmCarro) FROM tb_locacao GROUP BY idCarro) -- Seleciona apenas a última quilometragem (última locação)  
        
CREATE TABLE Estado (
	idEstado INTEGER PRIMARY KEY AUTOINCREMENT,
	nomeEstado VARCHAR
) 

INSERT INTO Estado (nomeEstado)
SELECT
	DISTINCT estadoCliente
FROM tb_locacao 

CREATE TABLE Cidade (
	idCidade INTEGER PRIMARY KEY AUTOINCREMENT,
	nomeCidade VARCHAR
) 

INSERT INTO Cidade (nomeCidade)
SELECT
	DISTINCT cidadeCliente
FROM tb_locacao 

CREATE TABLE Pais (
	idPais INTEGER PRIMARY KEY AUTOINCREMENT,
	nomePais VARCHAR
)

INSERT INTO Pais (nomePais)
SELECT
	DISTINCT paisCliente
FROM tb_locacao 

CREATE TABLE Cliente (
	idCliente INTEGER PRIMARY KEY,
	nomeCliente VARCHAR,
	idCidade INTEGER NOT NULL,
	idEstado INTEGER NOT NULL,
	idPais INTEGER NOT NULL,
	FOREIGN KEY(idCidade) REFERENCES Cidade(idCidade),
	FOREIGN KEY(idEstado) REFERENCES Estado(idEstado),
	FOREIGN KEY(idPais) REFERENCES Pais(idPais)
) 

INSERT INTO Cliente (idCliente,nomeCliente, idCidade, idEstado, idPais)
SELECT
	DISTINCT idCliente,
	nomeCliente,
	(SELECT idCidade FROM Cidade WHERE nomeCidade = cidadeCliente),
	(SELECT idEstado FROM Estado WHERE nomeEstado = estadoCliente),
	(SELECT idPais FROM Pais WHERE nomePais = paisCliente)
FROM tb_locacao 

CREATE TABLE Vendedor (
	idVendedor INTEGER PRIMARY KEY,
	nomeVendedor,
	sexoVendedor SMALLINT,
	idEstado INTEGER NOT NULL,
	FOREIGN KEY (idEstado) REFERENCES Estado(idEstado)
)

INSERT INTO Vendedor (idVendedor, nomeVendedor, sexoVendedor, idEstado)
SELECT 
	DISTINCT idVendedor,
	nomeVendedor,
	sexoVendedor,
	(SELECT idEstado FROM Estado WHERE nomeEstado = estadoVendedor)
FROM tb_locacao 

CREATE TABLE Locacao (
	idLocacao INTEGER PRIMARY KEY,
	dataLocacao DATE,
	horaLocacao TIME,
	qtdDiaria INTEGER,
	vlrDiaria DECIMAL,
	dataEntrega DATE,
	horaEntrega TIME,
	idCliente INTEGER NOT NULL,
	idVendedor INTEGER NOT NULL,
	idCarro INTEGER NOT NULL,
	FOREIGN KEY(idCliente) REFERENCES Cliente(idCliente),
	FOREIGN KEY(idVendedor) REFERENCES Vendedor(idVendedor),
	FOREIGN KEY(idCarro) REFERENCES Carro(idCarro)
)

INSERT INTO Locacao (idLocacao, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idCliente, idVendedor, idCarro)
SELECT
	DISTINCT idLocacao,
	dataLocacao,
	horaLocacao,
	qtdDiaria,
	vlrDiaria,
	dataEntrega,
	horaEntrega,
	(SELECT idCliente FROM Cliente WHERE Cliente.idCliente = tb_locacao.idCliente),
	(SELECT idVendedor FROM Vendedor WHERE Vendedor.idVendedor = tb_locacao.idVendedor),
	(SELECT idCarro FROM Carro WHERE Carro.idCarro = tb_locacao.idCarro)
FROM tb_locacao


SELECT * FROM tb_locacao tl 




























