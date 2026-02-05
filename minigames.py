# pelo menos você tentou..... pelo visto você não conseguiu né.

pontos = int(input("== Insira sua pontuação: "))

noob = "Você atualmente esta no nivel iniciante, treine mais"
mid = "Você atualmente se encontra em um nivel intermediario, recomendamos que evolua mais"
pro = "Dentre todos os mundos seu nome ecoa, como um veterano, alguém acima da média"

if pontos < 100 :
    print(noob)
elif pontos <= 500 :
    print(mid)
else:
    print(pro)

print("Você escuta uma movimentação em um arbusto próximo, mas quando você foi verificar..... ")
escolha = input("Oh não criatura apareceu, oque fará Herói? \ndigite A para atacar \ndigite D para defender \ndigite M para lançar uma magia poderosa \ndigite F para gritar e fugir \n")

match escolha:
    case "A" | "a":
        print("Você ataca com sua espada, assim você Derrota o monstro")
    case "D" | "d": 
        print("Você defende incasavelmente, passam-se 3 dias e 3 noites, até que sua batalha de resistência termina, e a criatura desmaia de exaustão, espero que tenha valido apena Heroi")
    case "M" | "m":
        print("Você lança a sua mais nova magia com o seu cajado, uma bola de fogo desce do céu destruindo seu oponente..... e você, a floresta e a casa de um lenhador que morava por ali, descanse em paz Heroi")
    case "F" | "f":
        print("Você corre com se sua vida dependesse disso, e assim o conto do Heroi covarde se espalha por toda parte")
    case _:

        print("você comprou o jogo foi, o meu eo seu...")

