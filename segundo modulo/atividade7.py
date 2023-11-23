salarioatual = float(input("Digite o salário atual: "))

if salarioatual <= 280.00:
    percentualaumento = 20
elif salarioatual <= 700.00:
    percentualaumento = 15
elif salarioatual <= 1500.00:
    percentualaumento = 10
else:
    percentualaumento = 5

valoraumento = (percentualaumento / 100) * salarioatual
novosalario = salarioatual + valoraumento

print(f"Salário antes do reajuste: R${salarioatual:.2f}")
print(f"Percentual de aumento aplicado: {percentualaumento}%")
print(f"Valor do aumento: R${valoraumento:.2f}")
print(f"Novo salário após o reajuste: R${novosalario:.2f}")
