#!/bin/bash
cd /home/kamily/ecommerce

data=$(date +"%Y/%m/%d")
relatorio_final="/home/kamily/ecommerce/relatorio_final.txt"

touch "$relatorio_final"

echo "Relatório Final - $data" >> "$relatorio_final"

cd vendas/backup/
cat relatorio* >> "../../relatorio_final.txt"
