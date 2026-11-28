n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
n3 = int(input('Terceiro Valor: '))
menor = n1
maior = n3

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

if n2 > n3 and n2 > n1:
    maior = n2

if n1 > n3 and n1 > n2:
    maior = n1

print(f'O menor valor digitado foi {menor} e o maior foi {maior}')
