CREATE VIEW dim_Cliente AS
	SELECT 
		cli.idCliente,
		cli.nomeCliente,
		e.nomeEstado AS estadoCliente,
		c.nomeCidade AS cidadeCliente,
		p.nomePais AS paisCliente
	FROM Cliente cli
	LEFT JOIN Estado e 
		ON cli.idEstado = e.idEstado
	LEFT JOIN Cidade c 
		ON cli.idCidade = c.idCidade 
	LEFT JOIN Pais p 
		ON cli.idPais = p.idPais
	GROUP BY cli.idCliente
	
CREATE VIEW dim_Carro AS
	SELECT
		car.idCarro,
		MAX(car.kmCarro) AS kmCarro,
		car.classiCarro,
		car.modeloCarro,
		car.anoCarro,
		com.idCombustivel,
		com.tipoCombustivel,
		m.marcaCarro
	FROM Carro car 
	LEFT JOIN Combustivel com 
		ON car.idCombustivel = com.idCombustivel 
	LEFT JOIN Marca m 
		ON car.idMarca = m.idMarca
	GROUP BY car.idCarro
	
CREATE VIEW dim_Vendedor AS
	SELECT
		v.idVendedor,
		v.nomeVendedor,
		v.sexoVendedor,
		e.nomeEstado AS estadoVendedor
	FROM Vendedor v 
	LEFT JOIN Estado e 
		ON v.idEstado = e.idEstado
	GROUP BY v.idVendedor 

CREATE VIEW fato_Locacao AS
	SELECT
		l.idLocacao,
		l.dataLocacao,
		l.horaLocacao,
		l.qtdDiaria,
		l.vlrDiaria,
		l.dataEntrega,
		l.horaEntrega,
		cli.idCliente,
		v.idVendedor,
		car.idCarro	
	FROM Locacao l 
	LEFT JOIN Cliente cli
		ON l.idCliente = cli.idCliente 
	LEFT JOIN Carro car 
		ON l.idCarro = car.idCarro 
	LEFT JOIN Vendedor v 
		ON v.idVendedor = l.idVendedor
	GROUP BY l.idLocacao
	
	
-- Consultas 
	
SELECT * FROM dim_Cliente

SELECT * FROM dim_Carro

SELECT * FROM dim_Vendedor

SELECT * FROM fato_Locacao
	