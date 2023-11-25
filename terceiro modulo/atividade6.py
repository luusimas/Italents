clientes = {"arthur": 18, "bianca": 16, "claudio": 20, "diego": 15, "ester": 22}
maiores = 0
menores = 0

for nome, idade in clientes.items():
    if idade >= 18:
        print(f"{nome} , maior de idade.")
        maiores += 1
    else:
        print(f"{nome} , menor de idade.")
        menores += 1

print(f"\nClientes maiores de idade: {maiores}")
print(f"Clientes menores de idade: {menores}")