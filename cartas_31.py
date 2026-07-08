import csv
from itertools import combinations


def gerar_cartas(q=5):
    """
    Gera q^2 + q + 1 cartas do plano projetivo finito de ordem q.

    Para q=5:
    - 31 cartas
    - 31 numeros diferentes
    - 6 numeros por carta
    - qualquer par de cartas tem exatamente 1 numero em comum
    """
    if q != 5:
        raise ValueError("Este exemplo usa aritmetica modulo 5. Use q=5.")

    pontos = {}
    numero = 1

    # 25 pontos comuns: pares (x, y), com x e y em {0, 1, 2, 3, 4}
    for x in range(q):
        for y in range(q):
            pontos[("ponto", x, y)] = numero
            numero += 1

    # 5 pontos no infinito, um para cada inclinacao m
    for m in range(q):
        pontos[("infinito_inclinacao", m)] = numero
        numero += 1

    # 1 ponto no infinito das retas verticais
    pontos[("infinito_vertical",)] = numero

    cartas = []

    # Retas y = m*x + b (mod 5)
    for m in range(q):
        for b in range(q):
            carta = [
                pontos[("ponto", x, (m * x + b) % q)]
                for x in range(q)
            ]
            carta.append(pontos[("infinito_inclinacao", m)])
            cartas.append(sorted(carta))

    # Retas verticais x = a
    for a in range(q):
        carta = [
            pontos[("ponto", a, y)]
            for y in range(q)
        ]
        carta.append(pontos[("infinito_vertical",)])
        cartas.append(sorted(carta))

    # Reta do infinito
    carta_infinito = [
        pontos[("infinito_inclinacao", m)]
        for m in range(q)
    ]
    carta_infinito.append(pontos[("infinito_vertical",)])
    cartas.append(sorted(carta_infinito))

    return cartas


def validar(cartas):
    if len(cartas) != 31:
        raise AssertionError(f"Esperava 31 cartas, mas foram geradas {len(cartas)}.")

    for i, carta in enumerate(cartas, start=1):
        if len(carta) != 6:
            raise AssertionError(f"Carta {i} tem {len(carta)} numeros, nao 6.")

    for (i, carta_a), (j, carta_b) in combinations(enumerate(cartas, start=1), 2):
        comum = set(carta_a) & set(carta_b)
        if len(comum) != 1:
            raise AssertionError(
                f"Cartas {i} e {j} compartilham {len(comum)} numeros: {sorted(comum)}"
            )


def salvar_csv(cartas, caminho="cartas_31.csv"):
    with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Carta", "Numero 1", "Numero 2", "Numero 3", "Numero 4", "Numero 5", "Numero 6"])
        for indice, carta in enumerate(cartas, start=1):
            escritor.writerow([indice, *carta])


if __name__ == "__main__":
    cartas = gerar_cartas()
    validar(cartas)

    for indice, carta in enumerate(cartas, start=1):
        print(f"Carta {indice:02d}: {carta}")

    salvar_csv(cartas)
    print("\nOK: 31 cartas geradas e validadas.")
    print("CSV salvo como cartas_31.csv")
