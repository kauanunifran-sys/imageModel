def calcular_media(notas):
    soma = 0
    for nota in notas:  # Itera sobre cada nota para somar todas
        soma += nota
    media = soma / len(notas)  # Calcula a média aritmética dividindo a soma pelo número de notas
    return media

notas_aluno = [7, 8, 9, 10]  # Lista com as notas do aluno

resultado = calcular_media(notas_aluno)  # Calcula a média das notas usando a função

print("A média do aluno é:", resultado)

