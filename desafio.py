# Desafio passado em aula

print("==ESCOLHA UM DOS SERVIÇOS ABAIXO BASTA DIGITAR SEU NUMERO==")
print("==Digite 1 para falar com um de nosssos atendentes==")
print("==Digite 2 para verificar a segundqa via do boleto==")
print("==Digite 3 para cancelar os nosssos serviços==")
print("==Digite 4 para receber mais informaçõessobre nossos planos==" )
print("==Digite 5 caso deseja sair==")

atendente = "==Estamos te encaminhando para um de nossos atendentes, porfavor aguarde na linha...=="
boleto = "==a seguir nos confirme as seguintes informações...=="
cancelar_servico = "==Se você deseja cancelar os nossos serviços, aguarde nos voltaremos com uma promoção imperdivel pra você, esperamos que mude de ideia=="
informacoes = "veja abaixo as informações sobre o seu plano"
sair = "Adeus"

escolha = input("digite o numero do serviço que deseja usar: ")

match escolha:
    case "1":
        print(atendente)
    case "2":
        print(boleto)
    case "3":
        print(cancelar_servico)
    case "4":
        print(informacoes)
        print("senhor Joelson seu plano atual é de 1mb pela bagatela de R$200,00 por mês")
    case "5":
        print(sair)
    case _:
        print("==parece que vc digitou errado, porfavor preste mais atenção==")

        