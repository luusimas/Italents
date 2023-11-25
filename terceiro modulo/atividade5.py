import random

quantidadejogos = int(input("Quantidade de jogos a serem gerados: "))

for _ in range(quantidadejogos):
    palpite = random.sample(range(1, 61), 6)
    print("Palpite:", sorted(palpite))