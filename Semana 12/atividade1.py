def verificar_semelhanca(triangulo1, triangulo2, criterio):
    if criterio == 'LAL':
        lado1_tri1, angulo_tri1, lado2_tri1 = triangulo1
        lado1_tri2, angulo_tri2, lado2_tri2 = triangulo2
        
        # Verifica se os lados são proporcionais e se o ângulo é congruente
        if lado1_tri1 / lado1_tri2 == lado2_tri1 / lado2_tri2 and angulo_tri1 == angulo_tri2:
            return "Os triângulos são semelhantes pelo critério LAL."
        else:
            return "Os triângulos NÃO são semelhantes pelo critério LAL."
    
    elif criterio == 'AA':
        angulo1_tri1, angulo2_tri1 = triangulo1
        angulo1_tri2, angulo2_tri2 = triangulo2
        
        # Verifica se dois ângulos são congruentes
        if angulo1_tri1 == angulo1_tri2 and angulo2_tri1 == angulo2_tri2:
            return "Os triângulos são semelhantes pelo critério AA."
        else:
            return "Os triângulos NÃO são semelhantes pelo critério AA."
    
    elif criterio == 'LLL':
        lado1_tri1, lado2_tri1, lado3_tri1 = triangulo1
        lado1_tri2, lado2_tri2, lado3_tri2 = triangulo2
        
        # Verifica se todos os lados são proporcionais
        if (lado1_tri1 / lado1_tri2 == lado2_tri1 / lado2_tri2 == lado3_tri1 / lado3_tri2):
            return "Os triângulos são semelhantes pelo critério LLL."
        else:
            return "Os triângulos NÃO são semelhantes pelo critério LLL."
    
    else:
        return "Critério inválido. Use 'LAL', 'AA' ou 'LLL'."


# Testes do Código
# Exemplo de uso
triangulo1_LAL = (3, 60, 4)  # Lados: 3 e 4, ângulo: 60°
triangulo2_LAL = (6, 60, 8)  # Lados: 6 e 8, ângulo: 60°
print(verificar_semelhanca(triangulo1_LAL, triangulo2_LAL, 'LAL'))

triangulo1_AA = (40, 50)  # Ângulos: 40° e 50°
triangulo2_AA = (40, 50)  # Ângulos: 40° e 50°
print(verificar_semelhanca(triangulo1_AA, triangulo2_AA, 'AA'))

triangulo1_LLL = (2, 3, 4)  # Lados: 2, 3 e 4
triangulo2_LLL = (4, 6, 8)  # Lados: 4, 6 e 8
print(verificar_semelhanca(triangulo1_LLL, triangulo2_LLL, 'LLL'))
