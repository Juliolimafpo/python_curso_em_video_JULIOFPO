from math import pow, sqrt

cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))

cateto_oposto = pow(cateto_oposto, 2)
cateto_adjacente = pow(cateto_adjacente, 2)

hipotenusa = sqrt(cateto_oposto + cateto_adjacente)

print(f'A hipotenusa é {hipotenusa}')
