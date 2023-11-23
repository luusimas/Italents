# Taxas de câmbio (23/11/2023)

taxadolar = 4.91
taxadolarcanadense = 3.59
taxaeuro = 5.35
taxalibra = 6.13
taxapesoargentino = 0.014
taxapesochileno = 0.0056

valorreais = float(input("Digite o valor desejado em reais (R$): "))

valordolar = valorreais / taxadolar
valordolarcanadense = valorreais / taxadolarcanadense
valoreuro = valorreais / taxaeuro
valorlibra = valorreais / taxalibra
valorpesoargentino = valorreais / taxapesoargentino
valorpesochileno = valorreais / taxapesochileno

print(f"USD {valordolar:.2f}")
print(f"C$ {valordolarcanadense:.2f}")
print(f"EUR {valoreuro:.2f}")
print(f"GBP {valorlibra:.2f}")
print(f"ARS {valorpesoargentino:.2f}")
print(f"CLP {valorpesochileno:.2f}")
