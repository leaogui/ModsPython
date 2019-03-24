def checar(palavra):

     with open("Mods.txt") as datafile: 
        for line in datafile: 
            if palavra in line: 
                print("O mod está na lista.")
            

        return False


def main():

    lista = []

    flag = 0

    print("Bem vindo ao programa para fazer uma lista de mods")

    arq = open("Mods.txt", "a")

    while(True):

        print("Para adicionar algo, digite 1, para checar se um mod está na lista, digite 2, para checar a lista, digite 3, para informações do programa, digite 4, para sair digite outra coisa.\n")

        choice = input("Escolha: ")

        if(choice == '1'):

            while(True):

                mods = input ("Digite o mod para adicionar, para parar digite -9: ")

                if(mods == '-9'):             
                    break 

                lista.append(mods)

                arq.write("\n") 
                arq.write(lista[flag])
                flag = flag + 1
                

        elif(choice == '2'):

            checks = input ("\nDigite o nome do mod: ")
            checar(checks)
        

        elif(choice == '3'):

            print("Os mods atuais são: ")

        elif(choice == '4'):

            print("\n Programa feito para listar lista de mods para jogos.\n Palavras ambíguas como 'CRAFT' podem gerar problemas ao identificar, seja específico.\n Tudo é salvo no .txt na pasta do programa. \n\n")


        else:

            print("Obrigado por usar o programa!\n")

            arq.close

            break



main()