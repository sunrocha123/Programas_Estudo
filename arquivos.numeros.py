def coletar_numeros():
    nome_do_arquivo = 'numeros.txt'
    numeros = [[1,4.5,9,12.9,1000], [-9,4.67,9.98,20,996]]

    escrever_numeros_no_arquivo(numeros, nome_do_arquivo)

def escrever_numeros_no_arquivo(numeros, nome_do_arquivo):
    with open(nome_do_arquivo,'w', encoding= 'utf-8') as escrever_arquivo:
        for i in range (len(numeros)):
            for j in range (len(numeros[0])):
                escrever_arquivo.write(str(numeros[i][j]) + "\t")
            escrever_arquivo.write("\n")
    ler_numeros_do_arquivo(nome_do_arquivo)

def ler_numeros_do_arquivo(nome_do_arquivo):
    with open(nome_do_arquivo,'r', encoding= 'utf-8') as ler_arquivo:
        for linha in ler_arquivo:
            print(linha.strip())

coletar_numeros()
