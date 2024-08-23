from collections import deque

def enche1(state):
    return [3, state[1]]

def enche2(state):
    return [state[0], 4]

def esvazia1(state):
    return [0, state[1]]

def esvazia2(state):
    return [state[0], 0]

def transfere1para2(state):
    X, Y = state
    transfer_amount = min(X, 4 - Y)
    return [X - transfer_amount, Y + transfer_amount]

def transfere2para1(state):
    X, Y = state
    transfer_amount = min(Y, 3 - X)
    return [X + transfer_amount, Y - transfer_amount]

def busca():
    estado_inicial = [0, 0]
    
    objetivo = 2
    
    fila = deque([(estado_inicial, [])])
    visitados = set()
    visitados.add(tuple(estado_inicial))
    
    while fila:
        estado_atual, caminho = fila.popleft() 
        
        if estado_atual[1] == objetivo:
            return caminho + [(estado_atual, "Objetivo alcançado!")]
        
        for operacao, funcao in [('encher-1', enche1), ('encher-2', enche2), 
                                 ('esvazia-1', esvazia1), ('esvazia-2', esvazia2), 
                                 ('transfere-1-para-2', transfere1para2), 
                                 ('transfere-2-para-1', transfere2para1)]:
            
            proximo_estado = funcao(estado_atual)
            if tuple(proximo_estado) not in visitados: 
                visitados.add(tuple(proximo_estado))
                fila.append((proximo_estado, caminho + [(estado_atual, operacao)]))
    
    return None

solucao = busca()
if solucao:
    print("Passos para alcançar a solução:")
    for passo, acao in solucao:
        print(f"Estado atual: Jarro X = {passo[0]}L, Jarro Y = {passo[1]}L -> Ação: {acao}")
else:
    print("Nenhuma solução encontrada.")
