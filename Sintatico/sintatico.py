import ../Lexico/lexico


pilha = []
def main():
    global pilha

    a = lexico.analisador()
    pilha.append(0)
    while (True):
        s = pilha[-1]
        action = t_analise[s][a['token']]

        if action[0] == 'S':
            pilha.append(int(action[1]))
            a = lexico.analisador()

        elif action[0] == 'R':
            A = gramatica[int(action[1]-1)]['A']
            B = gramatica[int(action[1])-1]['B']
            modulo_B = len(B.split())

            for i in [0:modulo_B]:
                pilha.pop(-1)

            t = pilha[-1]
            pilha.append(t_analise[t][A])

            print(A + ' -> ' + B)

        elif action[0] == 'acc':
            break

        else:
            erro()
