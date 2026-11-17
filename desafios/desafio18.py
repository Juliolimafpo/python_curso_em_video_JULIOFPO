import math

angulo = float(input('Digite o angulo: '))

angulo = math.radians(angulo)

seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print(f'O seno é {seno:.4f}, cosseno {cosseno:.4f} e tangente {tangente:.4f}')
