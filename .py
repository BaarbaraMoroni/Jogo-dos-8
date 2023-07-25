def move(tab_original):
  
    # Checa possíveis movimentos (os nós) da árvore gerados a partir de um tabuleiro
   
    movimentos = []
    tab = eval(tab_original)
    i = 0
    j = 0
    while 0 not in tab[i]:
        i += 1
    j = tab[i].index(0)
    
    # Verifica se é possível mover o 0 para baixo
    if i < 2:
        tab[i][j], tab[i+1][j] = tab[i+1][j], tab[i][j] 
        movimentos.append(str(tab))
        tab[i][j], tab[i+1][j] = tab[i+1][j], tab[i][j]

    # Verifica se é possível mover o 0 para cima
    if i > 0:
        tab[i][j], tab[i-1][j] = tab[i-1][j], tab[i][j]  
        movimentos.append(str(tab))       
        tab[i][j], tab[i-1][j] = tab[i-1][j], tab[i][j]  

    # Verifica se é possível mover o 0 para a direita
    if j < 2:
        tab[i][j], tab[i][j+1] = tab[i][j+1], tab[i][j] 
        movimentos.append(str(tab))
        tab[i][j], tab[i][j+1] = tab[i][j+1], tab[i][j]
    
    # Verifica se é possível mover o 0 para a esquerda
    if j > 0:
        tab[i][j], tab[i][j-1] = tab[i][j-1], tab[i][j] 
        movimentos.append(str(tab))
        tab[i][j], tab[i][j-1] = tab[i][j-1], tab[i][j]

    return movimentos

def bfs(start, end):
    # Usa BFS
    explorado = set()
    banco = [[start]]
    while banco:
        caminho = banco.pop(0)
        final = caminho[-1]
        if final in explorado: 
            continue
        for movimento in move(final):
            if movimento in explorado:
                continue
            banco.append(caminho + [movimento])
        explorado.add(final)
        if final == end:
            return caminho
    return None

# Definindo o tabuleiro inicial
tabuleiro = str([
                [4, 3, 6],
                [8, 7, 1],
                [0, 5, 2]
            ])

# Definindo o tabuleiro objetivo
obj_final = str([
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 0]
            ])

print("Usando Busca em Largura:")

# Aplicando a busca em largura
caminho_bfs = bfs(tabuleiro, obj_final)

# Se houver um caminho encontrado, imprime-o
if caminho_bfs:
    print("Caminho para o objetivo:")
    for i in caminho_bfs:
        print(i, end="\n")
else:
    print("Não há solução usando Busca em Largura.")
