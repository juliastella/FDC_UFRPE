def jogo_dos_convites():
    F = int(input())
    for _ in range(F):
        deck_na_mesa = list(map(int, input().split()))
        convidados = {}
        i = 1
        while True:
            deck = list(map(int, input().split()))
            if deck == [-1]:
                break
            convidados[i] = deck
            i += 1
        jogadores = sorted(convidados.keys(), reverse=True)
        rodada = 0
        while len(jogadores) > 1 and rodada < 1000:
            for jogador in jogadores:
                if not convidados[jogador]:
                    jogadores.remove(jogador)
                    print(jogador)
                    return
                carta_jogador = convidados[jogador].pop(0)
                if carta_jogador != deck_na_mesa[rodada % len(deck_na_mesa)]:
                    convidados[jogador].append(carta_jogador)
            rodada += 1
        print(0)

jogo_dos_convites()
