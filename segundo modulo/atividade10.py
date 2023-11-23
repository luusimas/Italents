import random

numeroescolhido = random.randint(0, 10)

tentativa = int(input("Tente adivinhar o número entre 0 e 10: "))

if tentativa == numeroescolhido:
    print(f"Você acertou. O número era {numeroescolhido}.")
else:
    print(f"Você errou. O número correto era {numeroescolhido}.")
