import random
import os
import time


#cores do sistema
class cores:
    cyan = '\033[1;36m'
    white = '\033[1;97m'
    yellow = '\033[1;33m'
    end = '\033[0m'
    green = '\033[92m'
    red= '\033[91m'

#definindo as funcoes
def finalizar_programa():
    print(cores.red + 'Finalizando o jogo...' + cores.end)
    exit()

def limpar_terminal():
    os.system('cls' if os.name== 'nt' else 'clear')

def gerar_numero_aleatorio():
    print(cores.yellow + 'Gerando um valor entre 1 e 100...' + cores.end)
    numero_aleatorio = random.randrange(101)
    return numero_aleatorio


limpar_terminal()

#aperte para continuar
print('')
print('\033[42m-=-\033[m'*13)
print('|                                     |')
print(
    '|\033[32m             Bem-Vindo!              \033[m|\n|\033[1:32m                                     |'
)
print('|         Vamos jogar um jogo?        |')
print('|                                     |')
print('|                                     |')
print('|  consegue adivinhar qual numero     |\n| estou pensando? esta entre 1 e 100  |')
print('|                                     |')
print('\033[42m-=-\033[m'*13)
print('')

while True:
    comecar_jogar = input('Pressione ENTER para comecar o jogo.')
    if comecar_jogar == '':
        break
    else:
        finalizar_programa()


numero_gerado = gerar_numero_aleatorio()
quantidade_de_chutes = 0 
#logica do game
while True:
    try:
        quantidade_de_chutes += 1 
        resposta = int(input('Tente adivinhar o numero...'))
        if resposta == numero_gerado:
            time.sleep(1)
            print(cores.green + f'Acertooou!!! o numero era {resposta}.' + cores.end)
            print(cores.white + f'Voce tentou {quantidade_de_chutes} vezes ate acertar.' + cores.end)
            jogar_novamente = input('Deseja jogar novamente? (s/n) :')
            quantidade_de_chutes = 0
            if jogar_novamente.lower() == 'n' or jogar_novamente == 'nao':
                finalizar_programa()
            elif jogar_novamente.lower() == 's' or jogar_novamente =='sim':
                limpar_terminal()
                numero_gerado = gerar_numero_aleatorio()
                continue
            else:
                print(cores.yellow + 'Resposta Invalida!' + cores.end)
                finalizar_programa()
        elif resposta > numero_gerado:
            time.sleep(1)
            print ('tente um numero \033[1;36mMENOR\033[m')
        elif  resposta < numero_gerado:
            time.sleep(1)
            print ('tente um numero \033[1;36mMAIOR\033[m')
    except ValueError:
        print(cores.red +'Digite um numero inteiro, por favor!' + cores.end)