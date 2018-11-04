import lexico
from utils import util_sin

def erro():
    global pilha

    while(True):
        s = pilha.pop(-1)
        aux = False
        for A in util_sin.nao_terminal:
            if not util_sin.t_analise[s][A] == -1:
                aux = True
                break
        if aux:
            break

    while(True):
        s = pilha[-1]
        a = lexico.analisador()
        if a == False:
            return a
        action = util_sin.t_analise[s][a['token']]
        if action[0] == 'S' or action[0] == 'R':
            return a


pilha = []
def main():
    global pilha

    a = lexico.analisador()

    pilha.append(0)
    regra = util_sin.gramatica[0]

    while (True):
        if a == False:
            break
        s = pilha[-1]
        action = util_sin.t_analise[s][a['token']]

        if action[0] == 'S':
            pilha.append(int(action[1]))
            a = lexico.analisador()

        elif action[0] == 'R':
            regra = util_sin.gramatica[int(action[1])-1]
            A = regra['A']
            B = regra['B']
            modulo_B = len(B.split())

            for i in range(modulo_B):
                pilha.pop(-1)

            t = pilha[-1]
            pilha.append(t_analise[t][A])

            print(A + ' -> ' + B)

        elif action[0] == 'acc':
            break

        else:
            linha, coluna = lexico.get_l_c()
            print("Erro Sintatico(" + linha + ',' + coluna + ').')
            a = erro(regra)
