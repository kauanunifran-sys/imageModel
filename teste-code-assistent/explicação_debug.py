# Erro de sintaxe identificado: Falta o parêntese de fechamento na linha do print.
# Causa: Erro de digitação, esquecimento de fechar os parênteses.
# Correção proposta: Adicionar ) ao final da linha print.

def calcular_media(notas):
    soma = 0
    for nota in notas:
        soma += nota
    media = soma / len(notas)
    return media

notas_aluno = [7, 8, 9, 10]

resultado = calcular_media(notas_aluno)

print("A média do aluno é:", resultado)