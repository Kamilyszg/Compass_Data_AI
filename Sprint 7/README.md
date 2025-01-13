# Informações

Na sexta sprint, pude aprender sobre Spark e Hadoop

# Resumo

**Spark** 

Apache Spark é uma poderosa ferramenta de processamento de dados, amplamente utilizada para análise e processamento em larga escala. Trata-se de uma plataforma projetada para executar tarefas de processamento distribuído em clusters, que são redes de computadores que operam juntos para atingir um mesmo objetivo. Um dos grandes diferenciais do Spark é a capacidade de realizar operações diretamente em memória, o que proporciona um desempenho muito superior em relação a outras soluções que dependem do acesso ao disco.

No Spark, os dados são particionados e distribuídos entre os nós do cluster. Essa abordagem permite que grandes volumes de informações sejam processados de forma paralela, melhorando a eficiência. Para garantir a tolerância a falhas, o Spark utiliza replicção e recuperação automática, assegurando que o processamento continue mesmo que algum componente do sistema falhe.

RDD (Resilient Distributed Datasets)

O RDD é a estrutura básica de dados de baixo nível no Spark. Ele representa um conjunto de dados distribuídos imutáveis que podem ser manipulados usando transformações e ações. A flexibilidade dos RDDs é uma das principais vantagens do Spark, permitindo o desenvolvimento de soluções personalizadas para diferentes tipos de processamento.

Uma característica importante do Spark é o conceito de Lazy Evaluation. Isso significa que as transformações aplicadas aos RDDs não são executadas imediatamente. Em vez disso, elas são registradas em um plano de execução que só será realizado quando uma ação é invocada, otimizando o uso dos recursos.

Dataset e DataFrame

Além dos RDDs, o Spark também oferece estruturas de dados de mais alto nível: Datasets e DataFrames. Ambos são utilizados para manipulação tabular de dados, facilitando o uso de consultas e operações títicas comuns em bancos de dados.

DataFrame: é uma abstração similar a uma tabela relacional, composta por linhas e colunas. Os dados em um DataFrame são imutáveis e podem ser de diversos tipos. As operações com DataFrames incluem agregar, ordenar e filtrar registros, oferecendo também otimizadores de consultas que geram planos de execução eficientes para as operações realizadas. Assim como os RDDs, DataFrames também utilizam Lazy Evaluation.

PySpark: é a interface do Apache Spark que permite que os desenvolvedores acostumados com a linguagem utilize-a para a realização de aplicações de análise e aprendizado de máquina.

**Comandos básicos**

1. Criação de um RDD
```Shell
    numeros = sc.parallelize([1,2,3,4,5,6,7,8,9,10])

    numeros.take(5) #visualização dos 5 primeiros
    numeros.top(5) #visualização dos 5 maiores
    numeros.collect() #visualização de todos os números
```

1. Concatenação de RDDs

```Shell
    numeros = sc.parallelize([1,2,3,4,5,6,7,8,9,10])
    numeros2 = sc.parallelize([6,7,8,9,10])

    uniao = numeros.union(numeros2) #1,2,3,4,5,6,7,8,9,10,6,7,8,9,10
```

3. Operações com conjuntos
```Shell
    interseccao = numeros.intersection(numeros2)
    #6,7,8,9,10

    subtracao = numeros.subtract(numeros2)
    #1,2,3,4,5

    cartesiano = numeros.cartesian(numeros2)
    #visualização de todas as combinações entre os conjuntos
```

4. Funções de agregação
   
```Shell
    numeros.count() #contagem
    numeros.mean() #média
    numeros.max() #maior número
    numeros.min() #menor número
    numeros.stdev() #desvio padrão
```

5. Utilização da função lambda

```Shell
    filtro = numeros.filter(lambda filtro: filtro > 2)

    mapa = numeros.map(lambda mapa: mapa *2)
```

6. Funções - manipulações  de RDDs

```Shell
    compras = sc.parallelize([(1, 200),(2,300),(3,400),(4,100),(5,70)])
    
    chaves = compras.keys()
    valores = compras.values()

    compras.countByKey() #contagem das chaves

    soma = compras.mapValues(lambda s: s +1)
    #aplica a função para cada valor na lista

    debitos = sc.parallelize([(1, 100),(2, 300)])
    resultado = compras.join(debitos)
    # [(1, (200, 100)),(2, (300,300))]

    semDebitos = compras.subtractByKey(debitos)
    #subtracao das chaves existem em debitos
    #[(3,400),(4,100),(5,70)]
```

7. Criação de dataframe

```Shell
    df1 = spark.createDataFrame([("Pedro", 10),("Maria", 20),("José", 30)])

    df1.show() #apresentação do df - colunas serão nomeadas pelo spark
```

8. Criação do dataframe com colunas nomeadas

```Shell
    schema = "id INT, nome STRING"
    dados = [[1,"Pedro"], [2,"Maria"]]

    df2 = spark.createDataFrame(dados, schema)
    df2.show() #visualização do df completo
    df2.show(1) #visualoização apenas da primeira linha (1,Pedro)
```

9. Função soma

```Shell
    from pyspark.sql.functions import sum

    schema2 = "Produtos STRING, Vendas INT"
    vendas = [("Caneta", 10),("Lápis", 20),("Caneta", 20)]
    df3 = spark.createDataFrame(vendas, schema2)
    #visualização de todas as linhas - com repetição

    agrupado = df3.groupBy("Produtos").agg(sum("Vendas"))
    #exclusão de repetição - soma dos valores na col vendas
```

10. Select

```Shell
    df3.select("Produtos").show()
    #visualização da col Produtos apenas
    df3.select("Vendas", "Produtos").show() 
    #inversao das colunas

    #ou
    spark.sql("select Vendas, Produtos from df3").show()
```

11. Utilização de expressões em colunas

```Shell
    from pyspark.sql.functions import expr
    df3.select("Produtos", "Vendas", expr("Vendas * 2")).show()

    #será criada uma nova coluna para que a expressão seja aplicada a cada valor em vendas
```

12. Importação CSV

```Shell
    #forma 1
    from pyspark.sql.types import *
    arqschema = "id INT, nome STRING, status STRING, cidade STRING, vendas INT, data STRING"
    despachantes = spark.read.csv("caminho/absoluto/despachantes.csv", header = False, schema = arqschema)

    #forma 2 - a atribuição dos tipos das colunas será inferida pelo spark, as colunas terão nomes aleatórios
     desp_autoschema = spark.read.load("caminho/absoluto/despachantes.csv", header = False, format = "csv", sep = ",", inferSchema = True)
```

13. Consultas

```Shell
    from pyspark.sql import functions as Func
    despachantes.select("id", "nome", "vendas").where((Func.col("vendas")>20) & (Func.col("vendas")<40)).show()
```

14. Mudança do tipo da coluna e renomeação
    
```Shell
    #visualização dos atuais tipos
    despachantes2.schema

    #mudança do tipo
    despachantes2 = despachantes.withColumn("data2", to_timestamp(Func.col("data"), "yyyy-MM-dd"))

    #renomeação
    novodf = despachantes.withColumnRenamed("nome", "nomes")
```

15. Tranformações - Group by e Order by

```Shell
    #visualização dos anos distintos e a contagem de ocorrências
    despachantes2.select("data").groupBy(year("data")).count().show()
    #ou
    despachantes2.select(year("data")).distinct().show()

    #total de vendas por cidade
    despachantes.groupBy("cidade").agg(sum("vendas")).show()

    #visualização por ordem alfabética
    despachantes2.select("nome",year("data")).orderBy("nome").show()

    #de forma descrescente
    despachantes.orderBy(Func.col("vendas").desc()).show()

    #ordenar com base em mais de uma coluna
    despachantes.orderBy(Func.col("cidade").desc(), Func.col("vendas").desc()).show()
```

16. Filter

```Shell
    despachantes.filter(Func.col("nome") == "Deolinda Vilela").show()
```

17. Exportação de dados

```Shell
    despachantes.write.format("parquet").save("caminho/para/a/exportacao")
    #pode também ser salvo em formato json, orc e csv
```

18. Importação de dados
```Shell
    var = spark.read.format("parquet").load("caminho/absoluto/importacao")
```

**Hadoop**





# Exercícios e Evidências

Os exercícios consistem 

# Certificados
