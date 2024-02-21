class No:
    def __init__(self, dado):
        self.dado = dado
        self.prox = None

class Pilha:
    def __init__(self):
        self.inicio = None

    def inserir(self, dado):
        novo_no = No(dado)
        novo_no.prox = self.inicio
        self.inicio = novo_no

    def isVazia(self):
        return self.inicio is None

    def remover(self):
        if self.isVazia():
            None
        ponteiro = self.inicio
        self.inicio = self.inicio.prox
        return ponteiro        


s = "julia"
pilha = Pilha()

for i in s:
    pilha.inserir(i)

while not pilha.isVazia(): #falta terminar
