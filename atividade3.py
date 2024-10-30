# Função para representar a operação de implicação lógica
def implica(p, q):
    return not p or q

# Função para avaliar todas as combinações e construir a tabela verdade
def tabela_verdade():
    # Imprime o cabeçalho da tabela
    print("P\tQ\tM\tR\tP→Q\t(P∨Q)→R\t¬P→(M→R)")
    print("-" * 50)
    
    # Lista com todas as combinações de valores para P, Q e M
    combinacoes = [
        (True, True, True),
        (True, True, False),
        (True, False, True),
        (True, False, False),
        (False, True, True),
        (False, True, False),
        (False, False, True),
        (False, False, False),
    ]
    
    # Avaliação de cada combinação
    for P, Q, M in combinacoes:
        # Avaliando cada condição
        cond1 = implica(P, Q)  # Condição 1: Se Ana vai, então Bruno vai (P → Q)
        cond2 = implica(P or Q, True)  # Condição 2: Se Ana ou Bruno for, a festa é animada (P ∨ Q → R)
        cond3 = implica(not P, implica(M, True))  # Condição 3: Se Ana não for, a festa depende da música de Bruno (¬P → (M → R))
        
        # Para que R seja verdadeiro, todas as condições precisam ser verdadeiras
        R = cond1 and cond2 and cond3
        
        # Imprimindo cada linha da tabela verdade
        print(f"{P}\t{Q}\t{M}\t{R}\t{cond1}\t{cond2}\t{cond3}")

# Executa a tabela verdade
tabela_verdade()
