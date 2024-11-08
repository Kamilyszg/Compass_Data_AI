# Informações

Na segunda sprint, pude aprender sobre banco de dados **SQL**, desde seu planejamento a fim de suprir a necessidade do negócio, até seu desenvolvimento e otimização que visa o fornecimento de informações claras e precisas que garantem uma boa tomada de decisão. Além disso, com o curso da **AWS** pude aprender <!--continuar-->

# Resumo

**SQL:** Por meio de vídeo aulas, exercícios e a leitura de materiais, pude aprender os comandos utilizados para a manipulação de tabelas e seus dados contidos com base nas formas de normalização buscando manter o banco de dados livre de redundâncias e inconsistências. Pode-se então dividir os conceitos nos seguintes tópicos:

## 1. Comandos SQL

<details>
<summary>Comandos Básicos;</summary>

```SQL
    SELECT coluna1, coluna2 -- Seleciona colunas de uma tabela

    SELECT DISTINCT coluna1 -- Seleciona valores distintos de uma coluna

    SELECT * -- Seleciona todas as colunas da tabela

    FROM tabela1 -- Define a(s) tabelas a ser(em) explorada(s)
    
    WHERE condicao = true -- Define condição para a seleção

    HAVING condicao_calculada = true -- Como o where, define uma condição para a seleção, diferenciando-se por aceitar condições que são calculadas por meio de funções.
    
    GROUP BY coluna1, coluna2 -- Agrupa os ítens semelhantes - evitando a repetição de linhas (o mesmo ocorre em GROUP BY 1,2)

    ORDER BY 1,2 -- Ordena a exibição de maneira crescente, onde 1 representa a "tabela1" e 2, a "tabela2"
    -- Caso for necessário ordenar de maineira decrescente, acrescentar "DESC" ao comando, ex. ORDER BY 1 DESC

    LIMIT N -- Limita a exibição ao número (N) de linhas definido
```
</details>

<details>
<summary>Operadores Aritméticos;</summary>

```SQL
    +  -- Soma de valores entre colunas ou constantes
    -- Exemplo (soma das colunas "salario" e "bonus" - resultado será exibido em uma nova coluna "total"):
    SELECT salario + bonus AS total FROM funcionarios;
    
    -  -- Subtração de valores
    -- Exemplo (subtração das colunas "preco" e "desconto" - resultado será exibido em uma nova coluna "preco_final") 
    SELECT preco - desconto AS preco_final FROM produtos;
    
    *  -- Multiplicação de valores
    -- Exemplo (multiplicação das colunas "quantidade" e "preco_unitario - resultado será exibido em uma nova coluna "pedidos")
    SELECT quantidade * preco_unitario AS total FROM pedidos;
    
    /  -- Divisão de valores, onde o divisor não pode ser zero
    -- Exemplo (divisão da coluna "total_vendas" por 12 - resultado será exibido em uma nova coluna "media_mensal")
    SELECT total_vendas / 12 AS media_mensal FROM vendas;
   
    %  -- Resto da divisão entre valores (módulo)
    -- Exemplo (divisão da coluna id por 2 e exibição de seu resto)
    SELECT id % 2 AS resto FROM usuarios;

    ^ -- Potenciação de valores
    -- Exemplo (2³ - retorno na nova coluna "resultado")
    SELECT 2 ^ 3 AS resultado;  

    || --Concatenação de strings
    -- Exemplo (junção das colunas "nome" e "sobrenome" na nova coluna "nome_completo")
    SELECT nome || ' ' || sobrenome AS nome_completo
    FROM usuarios;
```
</details>

<details>
<summary>Funções de agregação;</summary>

```SQL
    COUNT(*) -- Contagem de linhas ou valores não nulos de uma coluna

    SUM(coluna_x) --Calcula a soma de valores em uma coluna numérica.

    MIN(coluna_y) -- Filtra o menor valor entre as linhas

    MAX(coluna_z) -- Filtra o maior valor entre as linhas

    AVG(coluna_k) -- Calcula a média entre os valores
```
</details>

<details>
<summary> Join; </summary>

```SQL
    INNER JOIN  -- Retorna apenas as linhas que têm correspondência em ambas as tabelas
    -- Exemplo:
    SELECT A.nome, B.departamento
    FROM funcionarios A
    INNER JOIN departamentos B ON A.departamento_id = B.id;

    LEFT JOIN  -- Retorna todas as linhas da tabela à esquerda e as correspondências da tabela à direita; onde não há correspondência, retorna NULL
    -- Exemplo:
    SELECT A.nome, B.departamento
    FROM funcionarios A
    LEFT JOIN departamentos B ON A.departamento_id = B.id;

    RIGHT JOIN  -- Retorna todas as linhas da tabela à direita e as correspondências da tabela à esquerda; onde não há correspondência, retorna NULL
    -- Exemplo:
    SELECT A.nome, B.departamento
    FROM funcionarios A
    RIGHT JOIN departamentos B ON A.departamento_id = B.id;

    FULL JOIN  -- Retorna todas as linhas quando há correspondência em pelo menos uma das tabelas, e NULL onde não há correspondência
    -- Exemplo:
    SELECT A.nome, B.departamento
    FROM funcionarios A
    FULL JOIN departamentos B ON A.departamento_id = B.id;

```
</details>

<details>
<summary>Union e Union All;</summary>

```SQL
    UNION  -- Combina os resultados de duas consultas e remove linhas duplicadas
    -- Exemplo:
    SELECT nome FROM clientes
    UNION
    SELECT nome FROM fornecedores;

    UNION ALL  -- Combina os resultados de duas consultas e mantém todas as linhas, incluindo duplicadas
    -- Exemplo:
    SELECT nome FROM clientes
    UNION ALL
    SELECT nome FROM fornecedores;
```
</details>

<details>
<summary>Subquery;</summary>

```SQL
    -- Realizam consultas e são executadas junto aos comandos:

    Subquery em WHERE -- Retorna um conjunto de valores que será usado como condição
    -- Exemplo:
    SELECT nome FROM funcionarios
    WHERE departamento_id IN (SELECT MIN(id) FROM departamentos);

    Subquery em SELECT -- Retorna um valor que será exibido como uma coluna
    -- Exemplo:
    SELECT nome, 
           (SELECT COUNT(*) FROM projetos) AS total_projetos
    FROM funcionarios;

    Subquery em FROM -- Executa uma subquery como uma tabela temporária - não recomendado
    -- Exemplo:
    SELECT sub.categoria, sub.quantidade_total
    FROM (
        SELECT categoria, SUM(quantidade) AS quantidade_total
        FROM produtos
        GROUP BY categoria
    ) AS sub
    WHERE sub.quantidade_total > 100;

    Subquery com WITH -- Realiza uma consulta prévia e esta pode ser implementada na query principal
    -- Exemplo:
    WITH total_por_categoria AS (
        SELECT categoria, SUM(quantidade) AS quantidade_total
        FROM produtos
        GROUP BY categoria
    )
    SELECT categoria, quantidade_total
    FROM total_por_categoria
    WHERE quantidade_total > 100;    
```
</details>

<details>
<summary>Tratamento de dados;</summary>

```SQL
    :: -- Conversão de unidade
    -- Exemplos:
    SELECT '2021-10-01'::DATE
    SELECT coluna1::TEXT | SELECT '100'::NUMERIC

    CASE WHEN -- Condicional (if-else)
    -- Exemplo:
    SELECT nome,
       CASE WHEN salario > 5000 THEN 'Alto'
            ELSE 'Baixo' END AS faixa_salarial
    FROM funcionarios;

    COALESCE() -- Verifica a partir do primeiro campo quais dados são nulos, se houver, retorna o segundo e assim sucessivamente 
    SELECT nome, COALESCE(email, 'email_não_fornecido') AS email
    FROM clientes;

    LOWER(nome) -- Converte texto para letras minúsculas

    UPPER(nome) -- Converte texto para letras maiúsculas

    TRIM() -- Remove espaços das extremidades de um texto
    -- Exemplo:
    SELECT TRIM(nome) AS nome_ajustado
    FROM clientes;

    REPLACE() -- Substitui uma substring por outra dentro de um texto
    -- Exemplo:
    SELECT REPLACE(nome, 'Maria', 'Ana') AS nome_ajustado
    FROM clientes;

    INTERVAL() -- Define intervalos de tempo para operações com datas
    -- Exemplo:
    SELECT NOW() + INTERVAL '7 days' AS data_proxima_semana;

    DATE_TRUNC -- Trunca uma data/hora para uma parte específica (como ano, mês, etc.)
    -- Exemplo: 
    SELECT DATE_TRUNC('month', NOW()) AS inicio_do_mes;

    EXTRACT — Extrai uma parte específica de uma data/hora (como dia, mês, ano).
    -- Exemplo:
    SELECT EXTRACT(year FROM data_nascimento) AS ano_nascimento
    FROM clientes;    
```
</details>

<!-- * **Manipulação de tabelas:**


## 2. Normalização de tabelas

___
**AWS** 

# Exercícios


1. ...
[Resposta Ex1.](exercicios/ex1.txt)


2. ...
[Resposta Ex2.](exercicios/ex2.txt)



# Evidências


Ao executar o código do exercício ... observei que ... conforme podemos ver na imagem a seguir:

![Evidencia 1]()


# Certificados


Certificado do Curso ABC

![Curso ABC](certificados/sample.png)

-->

