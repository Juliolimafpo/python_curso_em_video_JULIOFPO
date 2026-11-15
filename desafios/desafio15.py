dias = int(input('Quantos dias foram de aluguel? '))
kms = float(input('Quantos kms rodados? '))

valor = (dias * 60) + (kms * 0.15)

print(f'O total que voce vai pagar é {valor:.2f}')
