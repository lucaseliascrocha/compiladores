file = open('fonte.txt', 'r')
fonte = file.readlines()
n_linha = 0
n_coluna = 0

while(True):

    try:
        linha = fonte[n_linha]
        if not linha[n_coluna] == '\n':
            print(linha[n_coluna])
            n_coluna = n_coluna + 1
        else:
            n_linha = n_linha + 1
            n_coluna = 0
    except:
        print("EOF")
        break;
