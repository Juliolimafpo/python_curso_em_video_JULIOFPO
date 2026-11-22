nome = input('Qual é o seu nome? ')

print(f'Prazer em te conhecer, {nome:>20}!')
print(f'Prazer em te conhecer, {nome:<20}!')
print(f'Prazer em te conhecer, {nome:=^20}!')

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
mult = n1 * n2
div = n1 / n2
divin = n1 // n2
potenc = n1 ** n2

print(f' A soma vale {s}, \n Multiplicação {mult}, \n divisão {div:.2f}, ', end='>>> ')
print(f'divisão inteira {divin}, \n potenciação {potenc}')