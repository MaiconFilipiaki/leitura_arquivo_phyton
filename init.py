arquivo = input('Digite o nome do arquivo: ')
with open(arquivo, 'r') as arquivo_existente, open('saida.txt',
                                                   'w') as novo_arquivo:
    for linha in arquivo_existente.readlines():
        novo_arquivo.write(linha)
