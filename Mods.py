from os import system, name 


def cls():

    if name == 'nt':
        system('cls')

    else:
        system('clear')

    return False

def existcheck(palavra):
    with open("Mods.txt") as arq: 
        for line in arq: 
            if palavra in line: 
                arq.close
                return True
        arq.close
        return False

def checar(palavra):

     with open("Mods.txt") as arq: 
        for line in arq: 
            if palavra in line:
                cls()
                print("\nO mod está na lista.\n")
                arq.close
                return True
        arq.close
        return False

def printar():

     with open("Mods.txt") as arq: 
        for line in arq:  
                print(line)
                arq.close


def deletar(delete):

    with open("Mods.txt", "r") as arq:
         lines = arq.readlines()
    with open("Mods.txt", "w") as arq:
        for line in lines:
            if line.strip("\n") != delete:
                arq.write(line)
                arq.truncate()
                arq.close

def main():

    lista = []

    flag = 0

    print("Bem vindo ao programa para fazer uma lista de mods, é altamente recomendado para o usuário ler as informações extras (opção 5).")


    while(True):


        print("Para adicionar algo, digite 1. Para checar se um mod está na lista, digite 2. Para checar a lista, digite 3. Para deletar algum mod, digite 4. para informações do programa, digite 5. Para sair digite outra coisa.\n")

        choice = input("Escolha: ")

        cls()

        if(choice == '1'):

            while(True):

                arq = open("Mods.txt", "a")

                print("Digite o mod para adicionar, para parar digite -9.")

                mods = input ("Escolha: ")

                if(mods == '-9'): 
                    cls()            
                    break 

                exist = existcheck(mods)


                if(exist == False):
                        lista.append(mods)

                        arq.write("\n") 
                        arq.write(lista[flag])
                        
                        flag = flag + 1
                        cls()
                        print("O mod foi adicionado.")
                else:
                    cls()
                    print("O mod já existe.")

                arq.close


                

        elif(choice == '2'):

            checks = input ("\nDigite o nome do mod: ")
            valid = checar(checks)
            
            if(valid == False):
                cls()
                print("\nO mod não está na lista.\n")

        elif(choice == '3'):

            print("Os mods atuais são: \n")
            printar()
            print("\n")
        
        elif(choice == '4'):

            print("Qual o mod que deseja deletar?")
            delete = input ("Escolha: ")
            cls()

            existdel=existcheck(delete)

            if(existdel == True):
                deletar(delete)
                print("\nO mod foi deletado.\n")
            else:
                print("\nO mod não existe na lista.\n")

        elif(choice == '5'):

            print("\n Programa feito para listar lista de mods para jogos.\n Palavras ambíguas como 'CRAFT' podem gerar problemas ao identificar, seja específico.\n O programa diferencia letras maiúsculas de minúsculas.\n Tudo é salvo no .txt na pasta do programa. \n\n")            

        else:

            print("Deseja mesmo fechar o programa?")
            
            exit = input("Escolha: ")

            cls()

            if(exit == 's' or exit == 'S' or exit == 'Sim' or exit == 'sim'):

                print("Obrigado por usar o programa!\n")
                input()
                break

  



main()