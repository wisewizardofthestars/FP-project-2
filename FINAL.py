#Final project 2 
#Sara Pinheiro, ist1102507, sara.pinheiro@tecnico.ulisboa.pt
#projeto 2: simulação de um prado

#TAD posição 
#O TAD posicao é usado para representar uma posição (x, y) de um prado 
#arbitrariamente grande, sendo x e y dois valores inteiros não negativos.
#tipo básico será LISTAS, em que formato será [coluna,linha]

#construtores

def cria_posicao(x,y):
    '''
    cria_posicao(x,y) recebe os valores correspondentes às coordenadas de uma
posição e devolve a posição correspondente.
     int × int → posicao
    '''
    if type(x)!=int or type(y)!=int or x<0 or y<0:
        raise ValueError ('cria_posicao: argumentos invalidos')
    return [x,y]


def cria_copia_posicao(p):
    '''
    cria_copia posicao(p) recebe uma 
    posição e devolve uma cópia nova da posição.
    posicao → posicao
    '''
    return p.copy()

#seletores
def obter_pos_x(p):
    '''
    obter_pos_x(p) devolve a componente x da posição p.
    posicao → int
    '''
    return p[0]
def obter_pos_y(p):
    '''
    obter_pos_y(p) devolve a componente y da posição p.
    posicao → int
    '''
    return p[1]

#reconhecedores 
def eh_posicao(arg):
    '''
    eh_posicao(arg) devolve True caso o seu argumento seja um TAD posição e
False caso contrário
    universal → booleano
    '''
    if type(arg)!=list or len(arg)!=2:
        return False
    if type(obter_pos_x(arg))!=int or type(obter_pos_y(arg))!=int or \
       obter_pos_x(arg)<0 or obter_pos_y(arg)<0:
        return False
    return True
#teste
def posicoes_iguais(p1,p2):
    '''
    posicoes_iguais(p1, p2) devolve True apenas se p1 e p2 são posições e 
    são iguais.
     posicao × posicao → booleano
    '''
    def pos_iguais_aux(p1,p2,elemento):
        return elemento(p1)==elemento(p2)
    if not eh_posicao(p1) or not eh_posicao(p2):
        return False
    return pos_iguais_aux(p1,p2,obter_pos_x) and \
           pos_iguais_aux(p1,p2,obter_pos_y)


#transformador
def posicao_para_str(p):
    '''
    posicao_para_str(p) devolve a cadeia de caracteres '(x, y)' que representa o
seu argumento, sendo os valores x e y as coordenadas de p.
    posicao → str
    '''
    return str((obter_pos_x(p), obter_pos_y(p)))
#funções de alto nível
def obter_posicoes_adjacentes(p):
    '''
    obter_posicoes_adjacentes(p) devolve um tuplo com as posições adjacentes 
    à posição p, começando pela posição acima de p e seguindo no 
    sentido horário.
    posicao → tuplo
    '''
    def pos_y_cima(p): 
        return cria_posicao(obter_pos_x(p),obter_pos_y(p)-1)
    def pos_x_direita(p):
        return cria_posicao(obter_pos_x(p)+1,obter_pos_y(p))
    def pos_y_baixo(p):   
        return cria_posicao(obter_pos_x(p),obter_pos_y(p)+1)
    def pos_x_esq(p):
        return cria_posicao(obter_pos_x(p)-1,obter_pos_y(p))
    
    if obter_pos_x(p)==0 and obter_pos_y(p)!=0: 
        return(pos_y_cima(p),pos_x_direita(p),pos_y_baixo(p))
    #se a posição for a coluna 0 então não existe adjacente para a esquerda
    
    if obter_pos_x(p)!=0 and obter_pos_y(p)==0:
        return (pos_x_direita(p),pos_y_baixo(p),pos_x_esq(p))
    #se for linha 0 então não pode haver posição para cima
    
    if obter_pos_x(p)==0 and obter_pos_y(p)==0:
        return (pos_x_direita(p),pos_y_baixo(p))
    #se a posição for coluna 0 e linha 0 então não pode haver posição 
    #para a esquerda nem para cima
    else:
        return (pos_y_cima(p),pos_x_direita(p),pos_y_baixo(p),pos_x_esq(p))
    #se a posição não tiver estas restrições
    
def ordenar_posicoes(tup): 
    '''
    ordenar_posicoes(t) devolve um tuplo contendo as mesmas posições do tuplo 
    fornecido como argumento, ordenadas de acordo com a ordem de 
    leitura do prado.
    tuplo → tuplo
    '''
    return tuple(map(lambda x:x[::-1],sorted(tuple(map(lambda x:x[::-1],tup)))))
    
#------------------------------------------------------------------------------#   

#TAD animal

#O TAD animal é usado para representar os animais do simulador de ecossistemas 
#que habitam o prado, existindo de dois tipos: predadores e presas. Os 
#predadores são caracterizados pela espécie, idade, frequência de reprodução, 
#fome e frequência de alimentação. As presas são apenas caracterizadas pela 
#espécie, idade e frequência de reprodução.

#O tipo básico usado será um dicionário, terá como keys o nome da espécie do
#animal, a frequência de reprodução, frequência de alimentação, 0 no caso das
#presas, fome e idade.

#construtor
def cria_animal(s,r,a):
    '''
    cria_animal(s, r, a) recebe uma cadeia de caracteres s não vazia 
    correspondente à espécie do animal e dois valores inteiros correspondentes
    à frequência de reprodução r (maior do que 0) e à frequência de alimentação
    a (maior ou igual que 0); e devolve o animal. Animais com frequência 
    de alimentação maior que 0 são considerados predadores, caso contrário são 
    considerados presas.
    str × int × int → animal
    '''
    if type(s)!=str or s=='' or type(r)!=int or r<1 or type(a)!=int or a<0:
        raise ValueError('cria_animal: argumentos invalidos')
    return {'name':s,'repr':r,'ali':a,'fome':0,'idade':0}

def cria_copia_animal(a):
    '''
    cria copia animal(a) recebe um animal a (predador ou presa) e devolve uma
nova cópia do animal.
    animal → animal
    '''
    return a.copy()

#seletores
def obter_especie(a):
    '''
    animal → str
obter_especie(a) devolve a cadeia de caracteres correspondente à espécie do
animal.
    '''
    return a['name']
def obter_freq_reproducao(a):
    '''
    animal → int
obter_freq_reproducao(a) devolve a frequência de reprodução do animal a.
    '''
    return a['repr']
def obter_freq_alimentacao(a):
    '''
    animal → int
obter_freq_alimentacao(a) devolve a frequência de alimentação do animal a
(as presas devolvem sempre 0).
    '''
    return a['ali']
def obter_idade(a):
    '''
    animal → int
obter_idade(a) devolve a idade do animal a.
    '''
    return a['idade']
def obter_fome(a):
    '''
    animal → int
obter_fome(a) devolve a fome do animal a (as presas devolvem sempre 0).
    '''
    return a['fome']


#modificadores
def aumenta_idade(a):
    '''
    animal → animal
aumenta_idade(a) modifica destrutivamente o animal a incrementando o valor da 
sua idade numa unidade, e devolve o próprio animal.
    '''
    a['idade']+=1
    return a
def reset_idade(a):
    '''
    animal → animal
reset_idade(a) modifica destrutivamente o animal a definindo o valor da sua
idade igual a 0, e devolve o próprio animal.
    '''
    a['idade']=0
    return a
def aumenta_fome(a):
    '''
     animal → animal
aumenta_fome(a) modifica destrutivamente o animal predador a incrementando o 
valor da sua fome em uma unidade, e devolve o próprio animal. Esta
operação não modifica os animais presa.
    '''
    if a['ali']!=0:
        a['fome']+=1
    return a
def reset_fome(a):
    '''
    animal → animal
reset_fome(a) modifica destrutivamente o animal predador a definindo o valor
da sua fome igual a 0, e devolve o próprio animal. Esta operação não modifica
os animais presa.
    '''
    if a['ali']!=0:
        a['fome']=0
    return a
#reconhecedor 
def eh_animal(arg):
    '''
    universal → booleano
eh_animal(arg) devolve True caso o seu argumento seja um TAD animal e
False caso contrário.
    '''
    if type(arg)!=dict or 'name' not in arg or 'repr' not in arg:
        return False
    if 'ali' not in arg or 'fome' not in arg or 'idade' not in arg:
        return False
    if type(arg['name'])!=str or arg['name']=='':
        return False
    if type(arg['repr'])!= int or arg['repr']<1 or type(arg['idade'])!=int:
        return False
    if type(arg['ali'])!=int or type(arg['fome'])!=int:
        return False
    if arg['ali']<0 or arg['fome']<0 or arg['idade']<0:
        return False
    return True
def eh_predador(arg):
    '''
    universal → booleano
eh_predador(arg) devolve True caso o seu argumento seja um TAD animal do
tipo predador e False caso contrário.
    '''
    if not eh_animal(arg):
        return False
    if obter_freq_alimentacao(arg)==0:
        return False
    return True
def eh_presa(arg):
    '''
    universal → booleano
eh_presa(arg) devolve True caso o seu argumento seja um TAD animal do
tipo presa e False caso contrário
    '''
    if not eh_animal(arg):
        return False
    if obter_freq_alimentacao(arg)!=0:
        return False
    return True

#teste 
def animais_iguais(a1,a2):
    '''
    animal × animal → booleano
animais_iguais(a1, a2) devolve True apenas se a1 e a2 são animais e são
iguais.
    '''
    if eh_animal(a1)==False or eh_animal(a2)==False:
        return False
    for car in a1:
        if a1[car]!=a2[car]:
            return False
    return True

#transformadores
def animal_para_char(a):
    '''
    animal → str
animal para char(a) devolve a cadeia de caracteres dum único elemento 
correspondente ao primeiro carácter da espécie do animal passada por 
argumento, em maiúscula para animais predadores e em minúscula para animais
presa.
    '''
    if a['ali']==0:
        return a['name'][0].lower()
    return a['name'][0].upper()
def animal_para_str(a):
    '''
    animal → str
animal_para_str(a) devolve a cadeia de caracteres que representa o animal.
    '''
    if a['ali']!=0:
        return a['name']+' '+'['+str(a['idade'])+'/'+str(a['repr'])+';'+\
               str(a['fome'])+'/'+str(a['ali'])+']'
    return a['name']+' '+'['+str(a['idade'])+'/'+str(a['repr'])+']'

#funções de alto nível
def eh_animal_fertil(a):
    '''
    animal → booleano
eh_animal_fertil(a) devolve True caso o animal a tenha atingido a 
idade de reprodução e False caso contrário.
    '''
    return obter_freq_reproducao(a)<=obter_idade(a)
def eh_animal_faminto(a):
    '''
    animal → booleano
eh_animal_faminto(a) devolve True caso o animal a tenha atingindo um valor de
fome igual ou superior à sua frequência de alimentação e False caso contrário. 
As presas devolvem sempre False.
    '''
    if obter_freq_alimentacao(a)==0:
        return False
    return obter_freq_alimentacao(a)<=obter_fome(a)

def reproduz_animal(a):
    '''
    animal → animal
reproduz_animal(a) recebe um animal a devolvendo um novo animal da mesma
espécie com idade e fome igual a 0, e modificando destrutivamente o animal 
passado como argumento a alterando a sua idade para 0.
    '''
    reset_idade(a)
    return reset_fome(reset_idade(cria_copia_animal(a)))
#---------------------------------------------------------------------------
#TAD prado
#O TAD prado é usado para representar o mapa do ecossistema e as animais que se
#encontram dentro. Neste caso o prado foi representado por uma lista de listas
#que contém na primeira posição um tuple de (linha,coluna); estas listas 
#são organizadas primeiro por linha e depois por coluna
#pode haver uma segunda posição em cada coluna; será 1 se nessa posição houver
#uma montanha ou rocha ou então será um animal(definido no TAD animal).
#não haver segunda posição significa que essa posição está livre.

#construtor

def cria_prado(d,r,a,p):
    '''
    posicao × tuplo × tuplo × tuplo 7→ prado
cria_prado(d, r, a, p) recebe uma posição d correspondente à posição que
ocupa a montanha do canto inferior direito do prado, um tuplo r de 0 ou
mais posições correspondentes aos rochedos que não são as montanhas dos
limites exteriores do prado, um tuplo a de 1 ou mais animais, e um tuplo p da
mesma dimensão do tuplo a com as posições correspondentes ocupadas pelos
animais; e devolve o prado que representa internamente o mapa e os animais
presentes.
    '''
    def aux(arg,filtro,nr):
        if nr==0:
            for elemento in arg:
                if not filtro(elemento):
                    return False
                return True
        else:
            for elemento in arg:
                for ele in nr:
                    if filtro(elemento,nr):
                        return False
                return True     
#confirmações de argumento  
    nc,nl,prado=obter_pos_x(d)+1,obter_pos_y(d)+1,[]    
    if not eh_posicao(d) or type(r)!=tuple or type(a)!=tuple or type(p)!=tuple \
       or len(r)<0 or len(a)<1 or len(a)!=len(p):
        raise ValueError('cria_prado: argumentos invalidos')
    if obter_pos_x(d)<0 or obter_pos_y(d)<0:
        raise ValueError('cria_prado: argumentos invalidos')
    for pos in p:
        if obter_pos_x(pos)==0 or obter_pos_x(pos)==nc-1 or \
           obter_pos_y(pos)==0 or obter_pos_y(pos)==nl-1:
            raise ValueError('cria_prado: argumentos invalidos')     
    if r!=():
        if not aux(r,eh_posicao,0) or not \
           aux(a,eh_animal,0) or not aux(p,eh_posicao,0):
            raise ValueError('cria_prado: argumentos invalidos')
        if not aux(r,posicoes_iguais,p):
            raise ValueError('cria_prado: argumentos invalidos')   
        for pos in r:
            if obter_pos_x(pos)==0 or obter_pos_x(pos)==nc-1 or \
               obter_pos_y(pos)==0 or obter_pos_y(pos)==nl-1:
                raise ValueError('cria_prado: argumentos invalidos')         
    else:
        if not aux(a,eh_animal,0) or not aux(p,eh_posicao,0):
            raise ValueError('cria_prado: argumentos invalidos')
        for pos in r:
            if obter_pos_x(pos)==0 or obter_pos_x(pos)==nc-1 or \
               obter_pos_y(pos)==0 or obter_pos_y(pos)==nl-1:
                raise ValueError('cria_prado: argumentos invalidos')  
#acaba confirmação de argumento               
    for linha in range(0,nl):
        for coluna in range(0,nc):
            if linha==0 or linha==nl-1 or coluna==0 or coluna==nc-1:
                prado+=[[tuple(cria_posicao(linha,coluna)),1],]
            else:
                prado+=[[tuple(cria_posicao(linha,coluna))],]
    for montanha in r:
        prado[nc*obter_pos_y(montanha)+obter_pos_x(montanha)]+=[1]
    for i in range(0,len(a)):
        prado[nc*obter_pos_y(p[i])+obter_pos_x(p[i])]+=[a[i]]
    for linha in range(0,nl):
        for coluna in range(0,nc):
            if len(prado[nc*obter_pos_y(p[i])+obter_pos_x(p[i])])==1:
                prado[nc*obter_pos_y(p[i])+obter_pos_x(p[i])]+=[0]              
    prado=sorted(prado)
    return prado+[(nc,nl)] 

def cria_copia_prado (m):
    '''
    prado → prado
cria_copia_prado(m) recebe um prado e devolve uma nova cópia do prado.
    '''
    return list(m)

#seletores
def obter_tamanho_x(m):
    '''
     prado → int
obter_tamanho_x(m) devolve o valor inteiro que corresponde à dimensão Nx
do prado.
    '''
    return m[len(m)-1][0]
def obter_tamanho_y(m):
    '''
       prado → int
obter_tamanho_t(m) devolve o valor inteiro que corresponde à dimensão Ny
do prado.
    '''
    return m[len(m)-1][1]
#--------------------------------------------------------------------------
#função extra
def aux_contagem(m,function):
    '''
    Função auxiliar de contagem.
    prado x função--> int
    '''
    cont=0
    for posicao in m[:len(m)-1]:
        if len(posicao)==2 and function(posicao[1]):
            cont+=1
    return cont 
#----------------------------------------------------------------------------
#continuação de seletores

def obter_numero_predadores(m):
    '''
    prado → int
obter_numero_predadores(m) devolve o número de animais predadores no prado.
    '''
    return aux_contagem(m,eh_predador)

def obter_numero_presas(m):
    '''
     prado → int
obter_numero_presas(m) devolve o número de animais presa no prado.
    '''
    return aux_contagem(m,eh_presa)
def obter_posicao_animais(m):
    '''
    prado → tuplo posicoes
obter_posicao_animais(m) devolve um tuplo contendo as posições do prado
ocupadas por animais, ordenadas em ordem de leitura do prado.
    '''
    tuple_new=()
    for posicao in m[:len(m)-1]:
        if len(posicao)==2 and posicao[1]!=1:
            tuple_new+=(list(posicao[0][::-1]),)
    return tuple_new

def obter_animal(m,p):
    '''
    prado × posicao → animal
obter_animal(m, p) devolve o animal do prado que se encontra na posição p.
    '''
    if len(m[obter_valor_numerico(m,p)])==2:
        return m[(obter_valor_numerico(m,p))][1]
    return 

#modificadores
def eliminar_animal(m,p):
    '''
    prado × posicao → prado
eliminar animal(m, p) modifica destrutivamente o prado m eliminando o 
animal da posição p deixando-a livre. Devolve o próprio prado
    '''
    if eh_animal(obter_animal(m,p)):
        m[obter_valor_numerico(m,p)]=\
        [m[obter_valor_numerico(m,p)][0]]
        return m
    return m
def mover_animal(m,p1,p2):
    '''
    prado × posicao × posicao → prado
mover animal(m, p1, p2) modifica destrutivamente o prado m movimentando
o animal da posição p1 para a nova posição p2, deixando livre a posição onde
se encontrava. Devolve o próprio prado.
    '''
    if not posicoes_iguais(p1,p2):
        eliminar_animal(m,p2)
        m[obter_valor_numerico(m,p2)]=m[obter_valor_numerico(m,p2)]\
        +[obter_animal(m,p1)]
        eliminar_animal(m,p1)
        return m
    return m
def inserir_animal(m,a,p):
    '''
    prado × animal × posicao → prado
inserir animal(m, a, p) modifica destrutivamente o prado m acrescentando
na posição p do prado o animal a passado com argumento. Devolve o próprio
prado.
    '''
    m[obter_valor_numerico(m,p)]=m[obter_valor_numerico(m,p)]+[a]
    return m

#reconhecedores 
def eh_prado(arg):  
        '''
        universal → booleano
eh prado(arg) devolve True caso o seu argumento seja um TAD prado e False
caso contrário.
        '''
        len_arg=len(arg)
        last_pos=arg[len_arg-1]
        if type(arg)!=list or len_arg<2:
            return False
        if type(last_pos)!=tuple or len(last_pos)!=2:
            return False        
        nc,nl=obter_tamanho_x(arg) ,obter_tamanho_y(arg) 
        if type(nc)!=int or type(nl)!=int or nc<1 or nl<1:
            return False
        for posicao in arg[:len_arg-1]:
            len_posicao=len(posicao)
            if not eh_posicao(list(posicao[0])) or\
               (len_posicao!=1 and len_posicao!=2):
                return False
            if len_posicao==2: 
                if posicao[1]!=1 and not eh_animal(posicao[1]):
                    return False
        return True

def eh_posicao_animal(m,p):
    '''
    prado × posicao → booleano
eh posicao animal(m, p) devolve True apenas no caso da posição p do prado
estar ocupada por um animal
'''
    if len(m[obter_valor_numerico(m,p)])==2 and \
       eh_animal(m[obter_valor_numerico(m,p)][1]):
        return True
    return False

def eh_posicao_obstaculo(m,p):
    '''
    prado × posicao → booleano
eh posicao obstaculo(m, p) devolve True apenas no caso da posição p do prado
corresponder a uma montanha ou rochedo.
    '''
    if len(m[obter_valor_numerico(m,p)])==2 and \
        m[obter_valor_numerico(m,p)][1]==1:
        return True
    return False

def eh_posicao_livre(m,p):
    '''
     prado × posicao → booleano
eh posicao livre(m, p) devolve True apenas no caso da posição p do prado
corresponder a um espaço livre (sem animais, nem obstáculos).
    '''
    if len(m[obter_valor_numerico(m,p)])!=1:
        return False
    return True

#testes 
def prados_iguais(p1,p2):
    '''
    prado × prado → booleano
prados iguais(p1, p2) devolve True apenas se p1 e p2 forem prados e forem
iguais.
    '''
    if not eh_prado(p1) or not eh_prado(p2):
        return False
    for i in range(0,len(p1)):
        if p1[i]!=p2[i]:
            return False
    return True

#transformadores 
def prado_para_str(m):
        '''
        prado → str
prado para str(m) devolve uma cadeia de caracteres que representa o prado.
        '''
        nc,nl=obter_tamanho_x(m)-1,obter_tamanho_y(m)-1       
        def linha_str(linha,nc,nl):                        
            helper_str=''
            for posicao in linha: 
                x,y=posicao[0][1],posicao[0][0]
                if (x==0 and y==0) or (x==0 and y==nl) or (x==nc and y==0) \
                     or (y==nl and x==nc): 
                    helper_str+='+'
                elif x==0 or x==nc:
                    helper_str+='|'  
                elif y==0 or y==nl:
                    helper_str+= '-'
                elif len(posicao)==1:
                    helper_str+='.'
                else:
                    if posicao[1]==1:
                        helper_str+='@'
                    else:
                        helper_str+=\
                        animal_para_char(posicao[1])    
            return helper_str         
        result_str=''
        for i in range(nl+1):
            if i!=nl:
                result_str+=linha_str(m[(nc+1)*i:(nc+1)*(i+1)],nc,nl)+'\n'
            else:
                result_str+=linha_str(m[(nc+1)*i:len(m)-1],nc,nl)
        return result_str
    
#funções de alto nível
def obter_valor_numerico(m,p):
    '''
    prado × posicao 7→ int
obter valor numerico(m, p) devolve o valor numérico da posição p correspondente
à ordem de leitura no prado m.
    '''
    return obter_tamanho_x(m)*obter_pos_y(p)+obter_pos_x(p)
def obter_movimento(m,p):
    '''
    prado × posicao → posicao
obter movimento(m, p) devolve a posiçãoo seguinte do animal na posição p dentro
do prado m de acordo com as regras de movimento dos animais no prado.
    '''
    posicoes=list(obter_posicoes_adjacentes(p))
    animal=obter_animal(m,p)
    pos_presa=[]
    def rule(m,posicoes,p):
        pos=[]       
        for elemento in posicoes:
            if eh_posicao_livre(m,elemento):
                pos+=(elemento,)
                
        if len(pos)==0:
            return p
        return pos[obter_valor_numerico(m,p)%len(pos)]            
    
            
    if eh_predador(animal):
        for elemento in posicoes:
            if eh_posicao_animal(m,elemento) and eh_presa(obter_animal(m,elemento)):
                pos_presa+=(elemento,)        
        if len(pos_presa)>0:#se tiver de escolher presas
            return cria_posicao(pos_presa[0][0],pos_presa[0][1])

        else: #se so houverem livres ou de obstaculos
            return rule(m,posicoes,p)         
    else:
        return rule(m,posicoes,p)      
    
#funções extra
def geracao(m):
        '''
        geracao: prado → prado
        geracao(m) é a função auxiliar que modifica o prado m fornecido como 
        argumento deacordo com a evolução correspondente a uma geração 
        completa, e devolve o próprio prado.
        '''
        def reproducao(m,animal,posicao,pos_nova):
            if eh_animal_fertil(animal):
                if pos_nova!=posicao:
                    reset_idade(animal)
                    return inserir_animal(m,reproduz_animal(animal),posicao) 
        def dead(dead_list,posicao):
            for elemento in dead_list:
                if posicoes_iguais(elemento,posicao):
                    return False
            return True
        
        p=obter_posicao_animais(m)
        dead_list=()
        for posicao in p:
            pos_nova=obter_movimento(m,posicao)
            animal=obter_animal(m,posicao)
            if eh_posicao_animal(m,posicao) and dead(dead_list,posicao):
                aumenta_idade(animal)                                
                aumenta_fome(animal)                 
                if pos_nova!=posicao and eh_posicao_animal(m,pos_nova):
                    dead_list+=(pos_nova,)
                    reset_fome(animal)
                mover_animal(m,posicao,pos_nova)
                reproducao(m,animal,posicao,pos_nova)            
                if eh_animal_faminto(animal):
                    eliminar_animal(m,pos_nova)
        return m
    
def simula_ecossistema(f,g,v):
    '''
    str × int × booleano → tuplo
    simula ecossitema(f, g, v) é a função principal que permite simular o 
    ecossistema de um prado. A função recebe uma cadeia de caracteres f, um 
    valor inteiro g e um valor booleano v e devolve o tuplo de dois elementos 
    correspondentes ao número de predadores e presas no prado no fim da 
    simulação. A cadeia de caracteres f passada por argumento corresponde ao 
    nome do ficheiro de configuração da simulação. O valor inteiro g 
    corresponde ao número de gerações a simular. O argumento booleano v ativa
    o modo verboso (True) ou o modo quiet (False). No modo quiet mostra-se pela
    saída standard o prado, o número de animais e o número de geração no início 
    da simulação e após a última geração. No modo verboso, após cada geração, 
    mostra-se também o prado, o número de animais e o número de geração,
    apenas se o número de animais predadores ou presas se tiver alterado.
    '''
    ff=open(f,'r')
    def catch_pos(ff):
        string=ff.readline()
        return eval(string)
    def pos(tup):
        return cria_posicao(tup[0],tup[1])
        
       
    dim=pos(catch_pos(ff))
    rochas=tuple(map(lambda x: pos(x), catch_pos(ff)))
    animal_full=ff.readlines()
    ff.close()
    
    animal_full=[eval(x) for x in animal_full]
    posicao,animal_list=(),()
    for animal in animal_full:
        posicao+=(pos(animal[3]),)
        animal_list+=((cria_animal(animal[0],animal[1],animal[2])),)
    prado=cria_prado(dim,rochas,animal_list,posicao)
    
    for generation in range(0,g+1):
        if generation==0:
            presas,predadores=obter_numero_presas(prado),\
                obter_numero_predadores(prado)                
            print ('Predadores:',predadores,'vs Presas:',presas,\
                   '(Gen. '+str(generation)+')')
            print (prado_para_str(prado))
        else:
            prado_new=geracao(cria_copia_prado(prado))
            presas_new,predadores_new=obter_numero_presas(prado_new),\
                obter_numero_predadores(prado_new)
            
            if v and (presas_new!=presas or predadores_new!=predadores):
                                 
                print ('Predadores:',predadores_new,'vs Presas:',\
                       presas_new,\
                       '(Gen. '+str(generation)+')')
                print (prado_para_str(prado_new)) 
            else:
                if generation==g:
                    print ('Predadores:',predadores_new,'vs Presas:',
                           presas_new,\
                           '(Gen. '+str(generation)+')')
                    print (prado_para_str(prado_new))  
            presas,predadores=presas_new,predadores_new                                                      
            prado=prado_new 

    return (predadores, presas)  
