numero = input("Digite um número inteiro: ")
i = 0
numeroAlterado = 0
soma = 0
while i <= len(numero):
    if i == 0:
        RestoDivisao = int(numero) % 10
        DivisaoInteira = int(numero) // 10
        numeroAlterado =  DivisaoInteira
        soma = soma + RestoDivisao
        i += 1
        pass
    else:
        RestoDivisao = numeroAlterado % 10
        DivisaoInteira = numeroAlterado // 10
        numeroAlterado =  DivisaoInteira
        soma = soma + RestoDivisao
        i += 1
        pass
print(soma)