with open('estudantes.csv', 'r', encoding='utf-8') as arquivo:
    conteudo_arquivo = arquivo.readlines()

def processar_conteudo(linha):
    dados = linha.strip().split(',')
    estudante_nome = dados[0]
    lista_notas = list(map(int, dados[1:]))
    notas_selecionadas = sorted(lista_notas, reverse=True)[:3]
    media_calculada = round(sum(notas_selecionadas) / 3, 2)
    return (estudante_nome, f"Nome: {estudante_nome} Notas: {notas_selecionadas} Média: {media_calculada}")

relatorio_final = sorted(map(processar_conteudo, conteudo_arquivo), key=lambda x: x[0])

for _, relatorio in relatorio_final:
    print(relatorio)