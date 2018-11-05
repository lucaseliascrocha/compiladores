from utils import util_sin

for i in range(0,59):
    finais = str(i) + ': '
    for a in util_sin.terminal:
        action = util_sin.t_analise[i][a]
        if not action == 'erro':
            finais+= a + ':' + action + '   '

    for a in util_sin.nao_terminal:
        action = util_sin.t_analise[i][a]
        if not action == '-1':
            finais+= a + ':' + action + '   '

    print(finais)
