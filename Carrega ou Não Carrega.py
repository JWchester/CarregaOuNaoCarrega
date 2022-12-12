import sys

def divisao_sucessiva(recebe_Entrada):
    parada = recebe_Entrada
    Entrada2 = recebe_Entrada%2
    parada = parada//2
    
    vetor.append(Entrada2)
    if (parada!= 0):
        return divisao_sucessiva(parada) #uso inadequado da recursividade!!!!
    else:
        resultado = []
        for i in range(-1,-len(vetor)-1,-1):
            resultado.append(vetor[i])
        
        return resultado

def soma_32_bits(b1, b2):
    resultado = []
    for i in range(0,len(b2),1):
        if b1[i] + b2[i] == 2:
            resultado.append(0)
        else:
            resultado.append(b1[i] + b2[i])

    resultado2 = []
    for i in range(0,len(b2),1):
        resultado2.append(str(resultado[i]))
    resultado2 = "".join(resultado2)
    return int(resultado2,2)
            
def principal():
    while True:
        while True:
            Decimal = input("Digite dois numeros seguido de um espaço entre eles:  ").split(" ")

            try:

                Decimal1 = int(Decimal[0])
                Decimal2 = int(Decimal[1])
                break
            except:
                print("digite extamente como foi informado!")


        global vetor
        vetor = []
        Binario1 = divisao_sucessiva(Decimal1)
        vetor = []
        Binario2 = divisao_sucessiva(Decimal2)

        if len(Binario1) > len(Binario2):
            for i in range(0,len(Binario1) - len(Binario2), 1):
                Binario2.insert(0,0)

        elif len(Binario2) > len(Binario1):
            for i in range(0,len(Binario2) - len(Binario1), 1):
                Binario1.insert(0,0)
        
        print(soma_32_bits(Binario1,Binario2), ":)")
        Sair_do_Programa()

def Sair_do_Programa():
    while True:
        S = input("você deseja sair do programa? [y/n]").lower()
        if (S == "n" and S != "y") or (S != "n" and S == "y"):
            if S == "y":
                sys.exit()
            break
        elif S != "y" and S != "n":
            print("Digite y ou n para determinar seu destino")

principal()



