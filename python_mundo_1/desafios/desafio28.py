from random import randint
from time import sleep

numero_aleatorio = randint(0, 5)
print(10 * '-=-')
print(8 * ' ', 'Adivinhação  ')
print(10 * '-=-')

numero_usuario = int(input('Digite um numero inteiro: '))

print('PROCESSANDO...')

sleep(1)

if numero_usuario == numero_aleatorio:
    print('Parabens Voce acertou!!')
else:
    print('Voce errou :(')
