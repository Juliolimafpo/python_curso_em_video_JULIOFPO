salario = float(input('Qual o Valor do seu Salario? '))

if salario > 1250:
    aumento = (10 / 100 * salario)
    novo_salario = salario + aumento
    print('Aumento de 10%')
else:
    aumento = (15 / 100 * salario)
    novo_salario = salario + aumento
    print('Aumento de 15%')

print(f'Seu novo Salario é de {novo_salario}')
