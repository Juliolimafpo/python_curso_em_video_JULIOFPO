from random import randint

numero_aleatorio = randint(0, 5)
print(10 * '=')
print('Adivinhação')
print(10 * '=')

numero_usuario = int(input('Digite um numero inteiro: '))

if numero_usuario == numero_aleatorio:
    print('Parabens Voce acertou!!')
else:
    print('Voce errou :(')
