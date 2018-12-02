import lexico
from utils import util_sin
import escritor
from utils import util_sem

def erro(a):
    global pilha
    global id

    #Indicando erro
    finais = 'simbolos esperados: '
    s = pilha[-1]
    for terminal in util_sin.terminal:
        action = util_sin.t_analise[s][terminal]
        if not action == 'erro':
            finais+= terminal + '   '

    print(finais)

    # Tratando o erro
    while(True):
        s = pilha.pop(-1)
        aux = False
        for A in util_sin.nao_terminal:
            if not util_sin.t_analise[s][A] == '-1':
                aux = True
                break
        if aux:
            break

    while(True):
        s = pilha[-1]
        if a == False:
            return a

        action = util_sin.t_analise[s][a['token']]
        if action[0] == 's' or action[0] == 'r':
            if a['token'] == 'id':
                id = a
            return a
        elif a['token'] == '$':
            print('Erro sintatico invalida toda analise sintatica.')
            import sys
            sys.exit()
        a = lexico.analisador()


pilha = []
pilha_sem = []
def main():
    global pilha
    global pilha_sem

    a = lexico.analisador()

    pilha.append(0)

    while (True):
        if a == False:
            break

        s = pilha[-1]
        action = util_sin.t_analise[s][a['token']]

        if action[0] == 's':
            pilha.append(int(action[1:]))
            pilha_sem.append(a)
            a = lexico.analisador()

        elif action[0] == 'r':
            regra = util_sin.gramatica[int(action[1:])-1]
            A = regra['A']
            B = regra['B']
            modulo_B = len(B.split())

            for i in range(modulo_B):
                pilha.pop(-1)

            t = pilha[-1]
            pilha.append(int(util_sin.t_analise[t][A]))

            print(A + ' -> ' + B)
            semantico(int(action[1:]), A, modulo_B)

        elif action == 'acc':
            break

        else:
            linha = lexico.get_l()
            print("Erro Sintatico(linha: " + str(linha) + ')')
            a = erro(a)


#------------------------------------------------------------------------------------#

Tx_18 = 0
Tx_25 = 0
def semantico(regra, A, modulo_B):
    global pilha_sem

    regra_sem = util_sem.regras_sem[regra-1]
    print ('Regra Semântica: '+ regra_sem + '\n')

    simbolos = {}
    if regra == 18 or regra == 25: #(18) LD -> OPRD opm OPRD | (25) EXP_R -> OPRD opr OPRD
        aux = pilha_sem.pop(-1)
        simbolos['OPRD2'] = aux
        aux = pilha_sem.pop(-1)
        simbolos[aux['token']] = aux
        aux = pilha_sem.pop(-1)
        simbolos['OPRD1'] = aux

    else:
        for i in range(modulo_B):
            aux = pilha_sem.pop(-1)
            simbolos[aux['token']] = aux

    print('Simbolos D.: ' + str(simbolos))
    S = {'token': A}

    if regra == 5:
        escritor.varfim()

    elif regra == 6:
        id = simbolos['id']
        TIPO = simbolos['TIPO']
        lexico.atribuicao_tipo(id['lexema'], TIPO['tipo'])
        escritor.Tipo(TIPO['tipo'], id['lexema'])

    elif regra == 7:
        S['tipo'] = 'int'

    elif regra == 8:
        S['tipo'] = 'real'

    elif regra == 9:
        S['tipo'] = 'lit'

    elif regra == 11:
        id = simbolos['id']
        if lexico.id_declarado(id['lexema']):
            if id['tipo'] == 'lit':
                escritor.scanf('s', id['lexema'])
            elif id['tipo'] == 'int':
                escritor.scanf('d', id['lexema'])
            elif id['tipo'] == 'real':
                escritor.scanf('lf', id['lexema'])
        else:
            print('\nErro: Variável não declarada.\n')

    elif regra == 12:
        ARG = simbolos['ARG']
        escritor.escreva(ARG)

    elif regra == 13:
        literal = simbolos['literal']
        S['lexema'] = literal['lexema']
        S['tipo'] = 'lit'
    elif regra == 14:
        num = simbolos['num']
        S['lexema'] = num['lexema']
        S['tipo'] = 'num'
    elif regra == 15:
        id = simbolos['id']
        if lexico.id_declarado(id['lexema']):
            id = simbolos['id']
            S['lexema'] = id['lexema']
            S['tipo'] = id['tipo']
        else:
            print('\nErro: Variável não declarada.\n')

    elif regra == 17:
        id = simbolos['id']
        if lexico.id_declarado(id['lexema']):
            LD = simbolos['LD']
            if (id['tipo'] == LD['tipo']) or (id['tipo'] == 'real' and (LD['tipo'] == 'num' or LD['tipo'] == 'int')):
                rcb = simbolos['rcb']
                rcb['tipo'] = '='
                escritor.rcb(id['lexema'],rcb['tipo'],LD['lexema'])
            else:
                print('\nErro: Tipos diferentes para atribuição.\n')
        else:
            print('\nErro: Variável não declarada.\n')

    elif regra == 18:
        global Tx_18

        OPRD1 = simbolos['OPRD1']
        OPRD2 = simbolos['OPRD2']
        tipos_equivalentes = ['num', 'int', 'real']
        if OPRD1['tipo'] in tipos_equivalentes and OPRD2['tipo'] in tipos_equivalentes:
            Tx = 'T' + str(Tx_18)
            S['lexema'] = Tx
            S['tipo'] = 'int'
            Tx_18 += 1

            opm = simbolos['opm']
            escritor.opm(Tx, OPRD1['lexema'], opm['lexema'], OPRD2['lexema'])
        else:
            print('\nErro: Operandos com tipos incompatíveis.\n')

    elif regra == 19:
        OPRD = simbolos['OPRD']
        S['lexema'] = OPRD['lexema']
        S['tipo'] = OPRD['tipo']

    elif regra == 20:
        id = simbolos['id']
        if lexico.id_declarado(id['lexema']):
            S['lexema'] = id['lexema']
            S['tipo'] = id['tipo']
        else:
            print('\nErro: Variável não declarada.\n')

    elif regra == 21:
        num = simbolos['num']
        S['lexema'] = num['lexema']
        S['tipo'] = num['token']

    elif regra == 23:
        escritor.fim_cond()

    elif regra == 24:
        EXP_R = simbolos['EXP_R']
        escritor.ini_cond(EXP_R['lexema'])

    elif regra == 25:
        global Tx_25

        OPRD1 = simbolos['OPRD1']
        OPRD2 = simbolos['OPRD2']
        tipos_equivalentes = ['num', 'int', 'real']
        if (OPRD1['tipo'] == OPRD2['tipo']) or (OPRD1['tipo'] in tipos_equivalentes and OPRD2['tipo'] in tipos_equivalentes):
            Tx = 'T' + str(Tx_25)
            S['lexema'] = Tx
            S['tipo'] = 'boolean'
            Tx_18 += 1

            opr = simbolos['opr']
            escritor.opr(Tx, OPRD1['lexema'], opr['lexema'], OPRD2['lexema'])

        else:
            print('\nErro: Operandos com tipos incompatíveis.\n')

    pilha_sem.append(S)


main()
