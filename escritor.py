from utils import util_sem

file = open('out_aux.c', 'w+')

def varfim():
    file.write('\n\n\n')

def Tipo(t, lexema):
    if t == 'lit':
        file.write('literal ' + lexema + ';\n')
    elif t == 'real':
        file.write('double ' + lexema + ';\n')
    else:
        file.write(t + ' ' + lexema + ';\n')

def scanf(t, lexema):
    file.write('scanf("%' + t + '", &' + lexema + ');\n')

def escreva(ARG):
    if ARG['tipo'] == 'lit':
        text = 'printf("%s",' + ARG['lexema'] + ');\n'
    elif ARG['tipo'] == 'real' or ARG['tipo'] == 'num':
        text = 'printf("%lf",' + ARG['lexema'] + ');\n'
    elif ARG['tipo'] == 'int':
        text = 'printf("%d",' + ARG['lexema'] + ');\n'
    else:
        text = 'printf(' + ARG['lexema'] + ');\n'
    file.write(text)

def rcb(id, rcb, LD):
    file.write(id + ' ' + rcb + ' ' + LD + ';\n')

def opm(Tx, OPRD1, OPM, OPRD2):
    file.write(Tx + ' = ' + OPRD1 + ' ' + OPM + ' ' + OPRD2 + ';\n')

def fim_cond():
    file.write('}\n')

def ini_cond(EXP_R):
    file.write('if (' + EXP_R + '){\n')

def opr(Tx, OPRD1, OPR, OPRD2):
    if OPR == '=':
        file.write(Tx + ' = ' + OPRD1 + ' == ' + OPRD2 + ';\n')
    elif OPR == '<>':
        file.write(Tx + ' = ' + OPRD1 + ' != ' + OPRD2 + ';\n')
    else:
        file.write(Tx + ' = ' + OPRD1 + ' ' + OPR + ' ' + OPRD2 + ';\n')

def close_file():
    global file
    file.close()

def cabecalho(Tx_18, Tx_25):
    out_aux = open('out_aux.c', 'r')
    traducao = out_aux.readlines()

    arq_final = open('out.c', 'w+')

    arq_final.write('#include<stdio.h>\n')
    arq_final.write('typedef char literal[256];\n')
    arq_final.write('void main(void){\n')

    arq_final.write('\n/*----Variaveis temporarias----*/\n')
    for i in range(0, Tx_18):
         arq_final.write('int T' + str(i) + ';\n')
    for i in range(Tx_18, Tx_25):
        arq_final.write('int T' + str(i) + ';\n')
    arq_final.write('/*------------------------------*/\n')

    for c in traducao:
        arq_final.write(c)

    arq_final.write('}')
