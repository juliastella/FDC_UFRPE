monica, id1, id2 = (int(input()) for _ in range(3))

def filho_velho(idade1, idade2, idade3):
    cal_idade = idade1 - idade2 - idade3

    mais_velho = idade2

    if idade3 > mais_velho:
        mais_velho = idade3

    if cal_idade > mais_velho:
        mais_velho = cal_idade
    
    return mais_velho

print(filho_velho(monica, id1, id2))
