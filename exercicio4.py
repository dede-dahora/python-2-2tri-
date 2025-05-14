N = int(input("\nDigite um número inteiro N para calcular N!: "))
fatorial = 1
for i in range(1, N + 1):
    fatorial *= i
print(f"O fatorial de {N} é {fatorial}.")