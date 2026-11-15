n = input('Digite algo: ')

print(n)
print('O tipo primitivo é: ',type(n))
print('É alfanumerico? ', n.isalnum())
print('So letra? ', n.isalpha())
print('Está so em maiusculo? ', n.isupper())
print('Está so em minusculo? ', n.islower())
print('É numerico? ', n.isnumeric())
print('So tem espaços? ', n.isspace())
print('É capitalizado? ', n.istitle())
if False:
    print('Oi')
else:
    print('CU')