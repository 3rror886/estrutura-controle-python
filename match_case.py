# se quiser sim mn, se quiser sim.

# Calculadora para calculos calculaveis.

'''
lógica de matemaquina

Entrada:
1. O usuario pre digitar dois numeros ou + (ou -)
2. o usuario deve dar a operação que deve ser feita para a calculadora

processamento:
Realizar as operações entregues

Saida:
Exibir o resultado da operação

'''

numero_um = float(input("Primeiro numero: "))
numero_dois = float(input("Segundo numero: "))
operar = input("Sinal: ")

'''
string = "Texto"
int = numeros inteiros
float = numeros que possuam casa decimal
boolean = true e false
'''

match operar:
    case "+":
        print("A sua conta deu: ", numero_um + numero_dois)
    case "-":
        print("A sua conta deu: ", numero_um - numero_dois)
    case "*":
        print("A sua conta deu: ", numero_um * numero_dois)
    case "/":
        if numero_dois == 0:
            print("mas tinha que ser o diferentão mesmo né, quebrando todas as regras, K K K K")
        else:
            print("nah", numero_um / numero_dois)
    case _:
        print("Nos só trabalhamos com sinais, Pfvr, tente novamente ")