velocidade = float(input('Qual a velocidade do carro em kmh? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7.00
    print(f'Você foi multado em R${multa:.2f}')
else:
    print('Você está no limite de velocidade')
