t_analise = [
{'inicio':,'varinicio':,'varfim':,'id':,'int':,'real':,'lit':,'leia':,'escreva':,'literal':,'num':,'se':,'(':,')':,'entao':,'opr':,'fimse':,'fim':,'P':,'V':,'LV':,'D':,'TIPO':,'A':,'ES':,'ARG':,'CMD':,'LD':,'OPRD':,'COND':,'CABECALHO':,'EXP_R':,'CORPO':},
{'inicio':,'varinicio':,'varfim':,'id':,'int':,'real':,'lit':,'leia':,'escreva':,'literal':,'num':,'se':,'(':,')':,'entao':,'opr':,'fimse':,'fim':,'P':,'V':,'LV':,'D':,'TIPO':,'A':,'ES':,'ARG':,'CMD':,'LD':,'OPRD':,'COND':,'CABECALHO':,'EXP_R':,'CORPO':},
{'inicio':,'varinicio':,'varfim':,'id':,'int':,'real':,'lit':,'leia':,'escreva':,'literal':,'num':,'se':,'(':,')':,'entao':,'opr':,'fimse':,'fim':,'P':,'V':,'LV':,'D':,'TIPO':,'A':,'ES':,'ARG':,'CMD':,'LD':,'OPRD':,'COND':,'CABECALHO':,'EXP_R':,'CORPO':},

]

gramatica = [
{'A':"P'",'B':'P'},
{'A':'P','B':'inicio V A'},
{'A':'V','B':'varinicio LV'},
{'A':'LV','B':'D LV'},
{'A':'LV','B':'varfim ;'},
{'A':'D','B':'id TIPO ;'},
{'A':'TIPO','B':'int'},
{'A':'TIPO','B':'real'},
{'A':'TIPO','B':'lit'},
{'A':'A','B':'ES A'},
{'A':'ES','B':'leia id ;'},
{'A':'ES','B':'escreva ARG ;'},
{'A':'ARG','B':'literal'},
{'A':'ARG','B':'num'},
{'A':'ARG','B':'id'},
{'A':'A','B':'CMD A'},
{'A':'CMD','B':'id rcb LD ;'},
{'A':'LD','B':'OPRD opm OPRD'},
{'A':'LD','B':'OPRD'},
{'A':'OPRD','B':'id'},
{'A':'OPRD','B':'num'},
{'A':'A','B':'COND A'},
{'A':'COND','B':'CABECALHO CORPO'},
{'A':'CABECALHO','B':'se ( EXP_R ) entao'},
{'A':'EXP_R','B':'OPRD opr OPRD'},
{'A':'CORPO','B':'ES CORPO'},
{'A':'CORPO','B':'CMD CORPO'},
{'A':'CORPO','B':'COND CORPO'},
{'A':'CORPO','B':'fimse'},
{'A':'A','B':'fim'}
]
