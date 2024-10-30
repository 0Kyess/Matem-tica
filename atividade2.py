def razao_bissetriz_interna(a, b, c):
    """
    Calcula a razão dividida pela bissetriz interna em um triângulo
    Dados os lados a = AB, b = AC e c = BC
    """
    # Tratamento de caso especial: verificar se a + b é zero para evitar divisão por zero
    if a + b == 0:
        return "Erro: a soma dos lados adjacentes não pode ser zero."
    
    # Cálculo da divisão pela bissetriz interna
    bd = (a * c) / (a + b)
    dc = c - bd
    razao = bd / dc
    return razao

def razao_bissetriz_externa(a, b, c):
    """
    Calcula a razão dividida pela bissetriz externa em um triângulo
    Dados os lados a = AB, b = AC e c = BC
    """
    # Tratamento de caso especial: verificar se a - b é zero para evitar divisão por zero
    if a == b:
        return "Erro: não é possível calcular a divisão para a bissetriz externa quando a = b."
    
    # Cálculo da divisão pela bissetriz externa usando os segmentos BF e FC
    bf = (a * c) / abs(a - b)
    fc = c + bf
    razao = bf / fc
    return razao

# Solicitar entrada do usuário para os valores dos lados do triângulo
try:
    a = float(input("Informe o valor do lado a (AB): "))
    b = float(input("Informe o valor do lado b (AC): "))
    c = float(input("Informe o valor do lado c (BC): "))

    # Cálculo da razão pela bissetriz interna
    razao_interna = razao_bissetriz_interna(a, b, c)
    print(f"A razão BD/DC pela bissetriz interna é: {razao_interna}")

    # Cálculo da razão pela bissetriz externa
    razao_externa = razao_bissetriz_externa(a, b, c)
    print(f"A razão BF/FC pela bissetriz externa é: {razao_externa}")

except ValueError:
    print("Erro: Certifique-se de que todos os valores informados são números válidos.")
