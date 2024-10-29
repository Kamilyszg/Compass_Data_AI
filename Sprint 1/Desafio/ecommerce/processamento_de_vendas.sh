#!/bin/bash
cd /home/kamily/ecommerce

#se não existe a pasta vendas
if [ ! -d "./vendas/" ];
then #então
  mkdir vendas/ #criar vendas
  mkdir vendas/backup/ #criar sub backup
fi #término do if

#copiar o arquivo csv de ecommerce/ para vendas/
cp dados_de_vendas.csv vendas/dados_de_vendas.csv

#definindo variáveis origem e destino
origem="vendas/dados_de_vendas.csv"
destino="vendas/backup/"

data=$(date +%Y%m%d)

#copiando com a formatação no nome do arquivo
cp "$origem" "$destino/dados-$data.csv"

nome_antigo="$destino/dados-$data.csv"
novo_nome="$destino/backup-dados-$data.csv"
#renomeando arquivo
mv "$nome_antigo" "$novo_nome"

#criando o relatório individual
touch "vendas/backup/relatorio-$data.txt"

data_formatada=$(date +"%Y/%m/%d")
hora_formatada=$(date +"%H:%M")

#imprimindo a data e a hora do SO
echo -e "$data_formatada $hora_formatada" >> "vendas/backup/relatorio-$data.txt"

#imprimindo a data da primeira venda
#delimito a coluna, ignoro a primeira linha, separo a coluna 5, defino o nome da variável que armazenará os valores e / como delimitador
#armazeno na variável formatacao a data entre ífens e gero o dado de entrada para sort e head
echo "Primeira venda: $(sort -k5 -t"," dados_de_vendas.csv | head -n1 | cut -d"," -f5)" >> "vendas/backup/relatorio-$data.txt"

#data da última venda: ordena-se de maneira reversa, e seleciona a primeira linha somente para a impressão
echo "Última venda: $(sed '1d' dados_de_vendas.csv | sort -k5 -t"," | tail -n1 | cut -d"," -f5)" >> "vendas/backup/relatorio-$data.txt"

#imprimindo quantidade de itens diferentes entre os dados: deleto a primeira linha,ordeno por nome delimitado, verifico se é único e conto
echo "Quantidade de ítens (distintos) vendidos: $(sed '1d' dados_de_vendas.csv|sort -k2 -t","|uniq -u|wc -l)" >> "vendas/backup/relatorio-$data.txt"

#enviando as 10 primeiras vendas ao relatório
cat $novo_nome|sed '1d'|head >> "vendas/backup/relatorio-$data.txt"

#zipando o backup do dia
zip $novo_nome.zip "vendas/backup/relatorio-$data.txt"

#removendo arquivos
rm $novo_nome $origem
