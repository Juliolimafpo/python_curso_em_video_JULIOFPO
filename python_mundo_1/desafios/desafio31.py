distancia = float(input('Qual a distância em kmh? '))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f'Voce vai pagar R${preco:.2f}')
