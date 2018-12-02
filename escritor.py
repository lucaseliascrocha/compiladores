from utils import util_sem

file = open('out.c', 'w+')

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
        text = 'printf(' + ARG['lexema'] + ');\n'
    else:
        text = 'printf("' + ARG['lexema'] + '");\n'
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
        file.write(Tx + ' = ' + OPRD1 + ' == ' + OPRD2 + '\n')
    elif OPR == '<>':
        file.write(Tx + ' = ' + OPRD1 + ' != ' + OPRD2 + '\n')
    else:
        file.write(Tx + ' = ' + OPRD1 + ' ' + OPR + ' ' + OPRD2 + '\n')
