nota = float(input("Digite a nota do aluno (entre 0.0 e 10.0): "))

if 0.0 <= nota <= 10.0:
    if nota < 6.0:
        print("Nota F")
    elif 6.0 <= nota < 7.0:
        print("Nota D")
    elif 7.0 <= nota < 8.0:
        print("Nota C")
    elif 8.0 <= nota < 9.0:
        print("Nota B")
    else:
        print("Nota A")
else:
    print("Erro: A nota deve estar entre 0.0 e 10.0.")
