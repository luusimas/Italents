estoque = {"produto1": 10, "produto2": 20, "produto3": 30}

produto = input("Nome do produto: ").lower()

if produto in estoque:
    quantidadesolicitada = int(input("Quantidade desejada: "))
    
    if quantidadesolicitada <= estoque[produto]:
        estoque[produto] -= quantidadesolicitada
        print(f"\nCompra realizada. Você comprou {quantidadesolicitada} unidades de {produto}.")
        print(f"Restante no estoque: {estoque}")
    else:
        print("Quantidade indisponível no estoque.")
else:
    print("Produto indisponível.")