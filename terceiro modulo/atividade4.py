numeros = []

while True:
    valor = input("Um número (ou 'sair' para encerrar): ")
    
    if valor.lower() == 'sair':
        break
    
    valor = int(valor)
    numeros.append(valor)

pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]

print("Lista completa:", numeros)
print("Lista de pares:", pares)
print("Lista de ímpares:", impares)
