print("\nSeja bem-vindo ao jogo da forca!\n")

palavra_secreta = 'flamengo'
letras_acertadas = ['_', '_', '_', '_', '_', '_', '_', '_']

acertou = False
enforcou = False
erros = 0

while not acertou and not enforcou:
    chute = input('Qual letra? \n')
    if chute in palavra_secreta:
        posicao = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                letras_acertadas[posicao] = letra
            posicao += 1
        print(letras_acertadas)
    else:
        erros += 1
        print(f"Você errou! Tentativa {erros} de 6.")

    enforcou = erros == 6
    acertou = '_' not in letras_acertadas

if acertou:
    print('\nParabéns, você venceu!\n')
else:
    print('\nVocê foi enforcado!\n')
