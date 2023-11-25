respostaspositivas = 0

p1 = input("Você telefonou para a vítima? (s/n): ")
p2 = input("Esteve no local do crime? (s/n): ")
p3 = input("Mora perto da vítima? (s/n): ")
p4 = input("Devia para a vítima? (s/n): ")
p5 = input("Já trabalhou com a vítima? (s/n): ")

if p1.lower() == "s":
    respostaspositivas += 1
if p2.lower() == "s":
    respostaspositivas += 1
if p3.lower() == "s":
    respostaspositivas += 1
if p4.lower() == "s":
    respostaspositivas += 1
if p5.lower() == "s":
    respostaspositivas += 1

if respostaspositivas == 2:
    print("Suspeito")
elif 3 <= respostaspositivas <= 4:
    print("Cúmplice")
elif respostaspositivas == 5:
    print("Assassino")
else:
    print("Inocente")
