def merge(a, p, q, r):
    pilha_carta1 = q - (p + 1) # quantidade da pilha da esquerda em L 
    pilha_carta2 = r - q # quantindade de elementos da pilha da direita em R

    arranjo = c