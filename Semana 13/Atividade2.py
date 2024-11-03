def calcular_idades(homem1, homem2, mulher1, mulher2):
    # Verifica se as idades são números inteiros positivos
    if not all(isinstance(idade, int) and idade > 0 for idade in [homem1, homem2, mulher1, mulher2]):
        return "Erro: Todos devem ser números inteiros"

    # Identificar o homem mais velho e o mais novo
    homem_mais_velho = max(homem1, homem2)
    homem_mais_novo = min(homem1, homem2)
    
    # Identificar a mulher mais velha e a mais nova
    mulher_mais_velha = max(mulher1, mulher2)
    mulher_mais_nova = min(mulher1, mulher2)
    
    # Calcular a soma do homem mais velho com a mulher mais nova
    soma_idades = homem_mais_velho + mulher_mais_nova
    
    # Calcular o produto do homem mais novo com a mulher mais velha
    produto_idades = homem_mais_novo * mulher_mais_velha
    
    return soma_idades, produto_idades

# Exemplo de uso com idades válidas
homem1 = 30
homem2 = 25
mulher1 = 22
mulher2 = 28

resultado = calcular_idades(homem1, homem2, mulher1, mulher2)
if isinstance(resultado, str):
    print(resultado)  # Exibe mensagem de erro se houver
else:
    soma, produto = resultado
    print("Soma das idades do homem mais velho com a mulher mais nova:", soma)
    print("Produto das idades do homem mais novo com a mulher mais velha:", produto)

# Exemplo de uso com idades inválidas
homem1 = 30
homem2 = -25  # Idade inválida
mulher1 = 22
mulher2 = "vinte e oito"  # Idade inválida

resultado = calcular_idades(homem1, homem2, mulher1, mulher2)
if isinstance(resultado, str):
    print(resultado)  # Exibe mensagem de erro se houver
else:
    soma, produto = resultado
    print("Soma das idades do homem mais velho com a mulher mais nova:", soma)
    print("Produto das idades do homem mais novo com a mulher mais velha:", produto)

