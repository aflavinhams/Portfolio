# Ana Flávia Martins dos Santos
# O programa a seguir implementa um Jogo da Forca, onde você deve advinhar a palavra secreta

import random
# Vetor com as palavras que serão randomizadas
print('Bem-vindo ao Jogo da Forca!')
print('Tema: animais')
print('Tenha um bom jogo! :)')

palavras = ["camelo", "cavalo", "ovelha", "coelho", "girafa", "jacaré", "macaco"]

# Randomização da palavra secreta
indice = random.randint(0, 4)
palavra = palavras[indice]
#print(f'Palavra secreta: {palavra}')

# Criação dos vetores com as letras das palavras
camelo = ['c', 'a', 'm', 'e', 'l', 'o']
cavalo = ['c', 'a', 'v', 'a', 'l', 'o']
ovelha = ['o', 'v', 'e', 'l', 'h', 'a']
coelho = ['c', 'o', 'e', 'l', 'h', 'o']
girafa = ['g', 'i', 'r', 'a', 'f', 'a']
jacare = ['j', 'a', 'c', 'a', 'r', 'e']
macaco = ['m', 'a', 'c', 'a', 'c', 'o']

# Criação dos vetores da palavra secreta e da resposta
vetorPalavra = [0] * 6
vetorResposta = ['_'] * 6

# Inicializando a variável tentativas em 8
tentativas = 8

# Bloco while para que a pessoa continue jogando enquanto não esgotar as tentativas
while tentativas > 0 and vetorResposta != vetorPalavra:

    print(f'Palavra: {vetorResposta}')

    # Bloco if - elif para estabelecer o vetorPalavra
    if palavra == 'camelo':
        vetorPalavra = camelo
    elif palavra == 'cavalo':
        vetorPalavra = cavalo
    elif palavra == 'ovelha':
        vetorPalavra = ovelha
    elif palavra == 'coelho':
        vetorPalavra = coelho
    elif palavra == 'girafa':
        vetorPalavra = girafa
    elif palavra == 'jacaré':
        vetorPalavra = jacare
    elif palavra == 'macaco':
        vetorPalavra = macaco

    erros = 0
    print(f'Tentativas restantes: {tentativas}')
    letra = input("Digite uma letra: ")
    print(' ')

    # Bloco for para realizar a verificação das letras
    for i in range(len(vetorPalavra)):

        # Se a letra que o usuário escolheu existir no vetor da palavra original
        # ele armazena essa informação no vetor resposta
        if letra == vetorPalavra[i]:
            vetorResposta[i] = vetorPalavra[i]

        # Aqui ele soma em uma variável quando a letra não é identificada
        elif letra != vetorPalavra[i]:
            erros += 1

        # Caso isso ocorra 6 vezes, significa que a letra não está na palavra inicial
        # Então ele avisa que a letra não existe e diminuiu uma tentativa
        if erros == 6:
            print('A letra digitada não existe')
            print(' ')
            tentativas -= 1

        # Caso o vetor das resposta tenha todas as letras da palavra, a pessoa ganhou
        if vetorResposta == vetorPalavra:
            print('Parabéns! Você acertou a palavra secreta. ')

# Caso as tentativas se esgotem, a pessoa perde
if tentativas == 0:
    print('Suas tentativas acabaram! :(')

