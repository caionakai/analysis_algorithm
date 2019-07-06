import math

x = 3400

empirico = x + (0.3*x) * ( (0.7*x) + (0.7*x * math.log2(x)) + (0.7*x) + (0.7*x))

print("Custo empirico: ", empirico)

assintotico = x**2 * math.log2(x)

print("Custo assintotico: ", assintotico)

proporcao = empirico/assintotico

print("Proporcao: ", proporcao)