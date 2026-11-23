# nome = input('Qual é o seu nome? ')
#
# if nome == 'Gustavo':
#     print('Que nome lindo voce tem!!')
# else:
#     print('Seu nome é tao normal')
# print(f'Bom dia {nome} !')

n1 = float(input('Digite a primeira Nota: '))
n2 = float(input('Digite a segunda Nota: '))
m = (n1 + n2) / 2

print(f'A sua media foi {m:.2f}')
print(f'Parabens' if m >= 6 else 'Sua media foi ruim')

# if m >= 6:
#     print('Sua media foi boa, Parabens!!')
# else:
#     print('Sua media foi ruim')
