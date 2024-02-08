#PROGRAMA PARA CRIANCA PRATICAR MATEMATICA

import time
import random

Print("Olá ")

#VARIAVEIS PARA CONTROLAR O TEMPO GASTO EM CADA RESPOSTA

tempo_cada_questao = []

x = True
gabarito = []
resposta = []
n_questoes = 5  # Defina o número de questões aqui
n = n_questoes

while x:
    a = random.randint(1, 9)        #GERA PRIMEIRO NUMERO DA SOMA
    b = random.randint(1, 9)        #GERA SEGUND NUMERO DA SOMA
    gabarito.append(a+b)            #ADICIONA A RESPOSTA CORRETA AO GABARITO
    tempo_antes = int(time.time())       #VERIFICA O TEMPO NA HORA QUE EXIBE A QUESTAO
    print(f'{a}+{b}')               #EXIBE A CONT NA TELA
    c = int(input("RESPOSTA: "))    #CAPTURA  RESPOSTA
    tempo_depois = int(time.time())
    resposta.append(c)              #ADCIONA A RESPOSTA DO ALUNO A FOLHA RESPOSTA
    tempo_cada_questao.append(tempo_depois-tempo_antes) #adiciona o tempo gasto em cada questao EM SEGUNDOS
    if a+b == c:                    #VERIFICA SE A RESPOSTA EH IGUAL GABARITO
        print("CORRETO\n")          
        n -= 1         
    else:
        print("\033[1;31mERRADO\033[0m \n")
        n += 1
        print(f"Precisa ACERTAR {n_questoes-n} questoes")
        
    if n == 0:  # Se n for 0, o loop será interrompido
        x = False


print(gabarito)
print(resposta)
print(tempo_cada_questao)
