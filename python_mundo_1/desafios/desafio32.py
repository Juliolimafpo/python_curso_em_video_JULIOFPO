from datetime import date

ano = int(input('Digite um ano: Coloque 0 caso queira analisar ano atual: '))




if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} É bissexto.')
else:
    print(f'O ano {ano} NÃO é bissexto.')
