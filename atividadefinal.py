import random

def jogardado():
    return random.randint(1, 6)

def criarjogador(nome):
    return {"nome": nome, "resultados": [], "vitorias": 0}

def main():
    numrodadas = int(input("Quantas rodadas você deseja jogar? "))
    numjogadores = int(input("Quantos jogadores vão participar do jogo? "))

    jogadores = []
    
    for i in range(numjogadores):
        nome = input(f"Nome do jogador {i + 1}: ")
        jogadores.append(criarjogador(nome))

    for rodada in range(numrodadas):
        print(f"\nRodada {rodada + 1}:")

        resultadosrodada = [jogardado() for _ in range(numjogadores)]
        maxresultado = max(resultadosrodada)

        for i, jogador in enumerate(jogadores):
            jogador["resultados"].append(resultadosrodada[i])
            print(f"{jogador['nome']} tirou {resultadosrodada[i]}")

            if resultadosrodada[i] == maxresultado:
                jogador["vitorias"] += 1

    print("\nResultados finais:\n")
    for jogador in jogadores:
        print(f"{jogador['nome']} obteve {jogador['vitorias']} vitória(s).")

    jogadores.sort(key=lambda x: x['vitorias'], reverse=True)

    empate = len(jogadores) > 1 and jogadores[0]['vitorias'] == jogadores[1]['vitorias']
    if empate:
        print("\nTeve um empate.")
    else:
        print(f"\nO campeão é {jogadores[0]['nome']}!")

if __name__ == "__main__":
    main()
