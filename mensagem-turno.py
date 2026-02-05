# em busca da casa automatica parte 100000000000

'''

criar um menu interativo de mensagem de cumprimento.

acesso com letra M = manhã
acesso com letra T = tarde
acesso com letra N = noite


'''

nome = input("qual seu nome ")
noite = "Boa noite "
manha = "bom dia "
tarde = "boa tarde "
periodo = input("digite o periodo ")

print("Bem vindo")

match periodo:
    case "m" | "manhã":
        print(manha, nome)
    case "n" | "noite":
        print(noite, nome)
    case "t" | "tarde":
        print(tarde, nome)
    case _:
        print("lamento ainda não trabalhamos com periodos marcianos")
