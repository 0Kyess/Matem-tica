def calcular_salario_final(salario_fixo, comissao_por_carro, total_carros_vendidos, total_vendas):
    # Define a porcentagem de comissão padrão sobre o total das vendas
    percentual_sobre_vendas = 5  # 5%
    # Define a porcentagem de bônus adicional se o vendedor vender mais de 10 carros
    percentual_bonus = 10  # 10%
    
    # Caso 1: Se o número de carros vendidos for zero, o vendedor recebe apenas o salário fixo
    if total_carros_vendidos == 0:
        salario_final = salario_fixo
    else:
        # Calcula a comissão por carros vendidos
        comissao_total_carros = comissao_por_carro * total_carros_vendidos
        
        # Calcula a comissão sobre o total das vendas
        comissao_sobre_vendas = (percentual_sobre_vendas / 100) * total_vendas
        
        # Salário padrão: salário fixo + comissão por carro + comissão sobre vendas
        salario_final = salario_fixo + comissao_total_carros + comissao_sobre_vendas
        
        # Caso 3: Bônus adicional de 10% sobre o total das vendas se o vendedor vender mais de 10 carros
        if total_carros_vendidos > 10:
            bonus_adicional = (percentual_bonus / 100) * total_vendas
            salario_final += bonus_adicional

    return salario_final

# Exemplo de uso:
salario_fixo = 2000  # Salário fixo
comissao_por_carro = 300  # Comissão por cada carro vendido
total_carros_vendidos = 12  # Quantidade de carros vendidos
total_vendas = 100000  # Valor total das vendas

salario_final = calcular_salario_final(salario_fixo, comissao_por_carro, total_carros_vendidos, total_vendas)
print("Salário final do vendedor:", salario_final)






