pessoas = []
idades = []

while True:
    pessoa = {}
    pessoa["nome"] = input("Nome da pessoa: ")
    pessoa["sexo"] = input("Sexo biológico (M/Fe): ").upper()
    pessoa["idade"] = int(input("Idade: "))
    
    if pessoa["sexo"] not in ['M', 'F']:
        print("Sexo biológico inválido. Digite 'M' para masculino ou 'F' para feminino.")
        continue
    
    pessoas.append(pessoa)
    idades.append(pessoa["idade"])
    
    continuar = input("Deseja cadastrar outra pessoa? (sim/não): ").lower()
    if continuar != "sim":
        break

totalpessoas = len(pessoas)
mediaidade = sum(idades) / totalpessoas

mulheres = [pessoa["nome"] for pessoa in pessoas if pessoa["sexo"] == 'F']
acimamediaidade = [pessoa["idade"] for pessoa in pessoas if pessoa["idade"] > mediaidade]

print(f"\nTotal de pessoas cadastradas: {totalpessoas}")
print(f"Média de idade das pessoas: {mediaidade:.2f}")
print(f"Mulheres cadastradas: {mulheres}")
print(f"Idades acima da média: {acimamediaidade}")