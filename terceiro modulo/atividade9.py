dadosfuncionario = {}

dadosfuncionario["nome"] = input("Nome do funcionário: ")
dadosfuncionario["anonascimento"] = int(input("Ano de nascimento: "))
dadosfuncionario["ctps"] = int(input("Número da CTPS (0 se não tiver): "))

if dadosfuncionario["ctps"] != 0:
    dadosfuncionario["anocontratacao"] = int(input("Ano de contratação: "))
    dadosfuncionario["salario"] = float(input("Salário: "))
    
    anoscontribuicao = 35
    idadeaposentadoria = dadosfuncionario["anocontratacao"] + anoscontribuicao - dadosfuncionario["anonascimento"]
    
    dadosfuncionario["idadeaposentadoria"] = idadeaposentadoria

print("\nInformações:")
for chave, valor in dadosfuncionario.items():
    print(f"{chave.capitalize()}: {valor}")