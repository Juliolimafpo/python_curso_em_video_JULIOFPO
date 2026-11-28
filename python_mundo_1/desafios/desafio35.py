print(15 * '=')
print('FORMA TRIANGULO?')
print(15 * '=')
lado1 = float(input('Primeiro lado de um triângulo: '))
lado2 = float(input('Segundo lado de um triângulo: '))
lado3 = float(input('Terceiro lado de um triângulo: '))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
    print('Pode formar um triangulo')
else:
    print('Nao pode formar um triangulo')
