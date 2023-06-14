jogo = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

contador = 0

print("---Jogo da velha---")

while contador == 0:

    jogadorxlinha = int(input("Digite a linha que gostaria jogar: "))
    jogadorxcoluna = int(input("Digite a coluna que gostaria jogar: \n"))

    jogo[jogadorxlinha - 1][jogadorxcoluna - 1] = 'x'

    for linha in range(3):
        print(" ".join(jogo[linha]))

    jogadorOlinha = int(input("Digite a linha que gostaria jogar: "))
    jogadorOcoluna = int(input("Digite a coluna que gostaria jogar: \n"))

    jogo[jogadorOlinha - 1][jogadorOcoluna - 1] = 'O'

    for linha in range(3):
        print(" ".join(jogo[linha]))

    # verifica se o jogador ganha pelas linhas
    for linha in range(3):
        if jogo[linha] == ['x', 'x', 'X']:
            print("Jogador X ganhou!")
            contador += 1
        elif jogo[linha] == ['o', 'o', 'o']:
            contador += 1
            print("Jogador O ganhou!")

    # verifica se o jogador ganha pelas colunas
    if jogo[0][0] == 'x' and jogo[1][0] == 'x' and jogo[2][0] == 'x':
        print('Jogador X ganhou!')
        contador += 1
    elif jogo[0][1] == 'x' and jogo[1][1] == 'x' and jogo[2][2] == 'x':
        print('Jogador X ganhou!')
        contador += 1
    elif jogo[0][2] == 'x' and jogo[1][2] == 'x' and jogo[2][2] == 'x':
        print('Jogador X ganhou!')
        contador += 1

    if jogo[0][0] == 'o' and jogo[1][0] == 'o' and jogo[2][0] == 'o':
        print('Jogador O ganhou!')
        contador += 1
    elif jogo[0][1] == 'o' and jogo[1][1] == 'o' and jogo[2][2] == 'o':
        print('Jogador O ganhou!')
        contador += 1
    elif jogo[0][2] == 'o' and jogo[1][2] == 'o' and jogo[2][2] == 'o':
        print('Jogador O ganhou!')
        contador += 1

    # verifica se o jogador ganha por diagonal
    if jogo[0][0] == 'x' and jogo[1][1] == 'x' and jogo[2][2] == 'x':
        print('Jogador X ganhou!')
        contador += 1
    elif jogo[2][0] == 'x' and jogo[1][1] == 'x' and jogo[0][2] == 'x':
        print('Jogador X ganhou!')
        contador += 1
    if jogo[0][0] == 'o' and jogo[1][1] == 'o' and jogo[2][2] == 'o':
        print('Jogador O ganhou!')
        contador += 1
    elif jogo[2][0] == 'o' and jogo[1][1] == 'o' and jogo[0][2] == 'o':
        print('Jogador O ganhou!')
        contador += 1