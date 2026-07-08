import os
import shutil

from cartas_31 import gerar_cartas, validar


LOGO_ORIGEM = "/Users/gabrielacarvalho/Library/Mobile Documents/com~apple~CloudDocs/Matemagincana-Arquivos-Soltos/Matemagincana-Jogamat.png"
LOGO_ARQUIVO = "Matemagincana-Jogamat.png"

CORES_MATEMAGINCANA = [
    ("RosaV", "#FF1E79"),
    ("Turquesa", "#11C5D9"),
    ("AzulM", "#4D9DE0"),
    ("Amarelo", "#F9D94E"),
    ("Branco", "#FFFFFF"),
    ("LilasV", "#B57DFF"),
    ("LavandaS", "#DCC6FF"),
    ("Verde Menta", "#7CE8B5"),
    ("Coral Alegre", "#FF7B72"),
]

FORMAS = [
    "circulo",
    "quadrado",
    "triangulo",
    "losango",
    "pentagono",
    "hexagono",
    "losango",
    "trapezio",
    "esfera",
    "cone",
    "cilindro",
    "piramide_base_quadrada",
    "cubo",
    "paralelepipedo",
    "tetraedro",
    "prisma_triangular",
    "prisma_hexagonal",
]


def sombra(cor, gradiente_id):
    return f'<linearGradient id="{gradiente_id}" x1="18" y1="12" x2="78" y2="84"><stop offset="0" stop-color="#ffffff" stop-opacity=".72"/><stop offset=".18" stop-color="{cor}"/><stop offset="1" stop-color="#4b5563" stop-opacity=".24"/></linearGradient>'


def simbolo_svg(numero, tamanho=96, mostrar_numero=False, contexto_id=""):
    nome_cor, cor = CORES_MATEMAGINCANA[(numero - 1) % len(CORES_MATEMAGINCANA)]
    forma = FORMAS[(numero - 1) % len(FORMAS)]
    rotacao = ((numero - 1) * 17) % 360
    traco = "#111827"
    largura_traco = 4
    centro = tamanho / 2
    defs = ""
    gradiente_id = f"grad_{numero}_{contexto_id}" if contexto_id else f"grad_{numero}"

    if forma == "circulo":
        desenho = f'<circle cx="{centro}" cy="{centro}" r="30" fill="{cor}" stroke="{traco}" stroke-width="{largura_traco}"/>'
    elif forma == "quadrado":
        desenho = f'<rect x="22" y="22" width="52" height="52" fill="{cor}" stroke="{traco}" stroke-width="{largura_traco}"/>'
    elif forma == "triangulo":
        desenho = f'<polygon points="48,14 82,78 14,78" fill="{cor}" stroke="{traco}" stroke-width="{largura_traco}"/>'
    elif forma == "losango":
        desenho = f'<polygon points="48,10 86,48 48,86 10,48" fill="{cor}" stroke="{traco}" stroke-width="{largura_traco}"/>'
    elif forma == "pentagono":
        desenho = f'<polygon points="48,10 84,38 70,82 26,82 12,38" fill="{cor}" stroke="{traco}" stroke-width="{largura_traco}"/>'
    elif forma == "hexagono":
        desenho = f'<polygon points="28,14 68,14 88,48 68,82 28,82 8,48" fill="{cor}" stroke="{traco}" stroke-width="{largura_traco}"/>'
    elif forma == "trapezio":
        desenho = f'<polygon points="30,20 66,20 84,78 12,78" fill="{cor}" stroke="{traco}" stroke-width="{largura_traco}" stroke-linejoin="round"/>'
    elif forma == "esfera":
        defs = sombra(cor, gradiente_id)
        desenho = (
            f'<circle cx="48" cy="48" r="32" fill="url(#{gradiente_id})" stroke="{traco}" stroke-width="{largura_traco}"/>'
            f'<ellipse cx="37" cy="33" rx="11" ry="7" fill="#ffffff" opacity=".78"/>'
        )
    elif forma == "cone":
        defs = sombra(cor, gradiente_id)
        desenho = (
            f'<path d="M48 10 L80 72 Q48 88 16 72 Z" fill="url(#{gradiente_id})" stroke="{traco}" stroke-width="{largura_traco}" stroke-linejoin="round"/>'
            f'<ellipse cx="48" cy="72" rx="32" ry="12" fill="{cor}" opacity=".86" stroke="{traco}" stroke-width="{largura_traco}"/>'
        )
    elif forma == "cilindro":
        defs = sombra(cor, gradiente_id)
        desenho = (
            f'<path d="M20 28 V70 Q20 84 48 84 Q76 84 76 70 V28" fill="url(#{gradiente_id})" stroke="{traco}" stroke-width="{largura_traco}"/>'
            f'<ellipse cx="48" cy="28" rx="28" ry="13" fill="{cor}" stroke="{traco}" stroke-width="{largura_traco}"/>'
        )
    elif forma == "piramide_base_quadrada":
        desenho = (
            f'<polygon points="48,12 20,68 48,84" fill="{cor}" stroke="{traco}" stroke-width="{largura_traco}" stroke-linejoin="round"/>'
            f'<polygon points="48,12 76,68 48,84" fill="{cor}" opacity=".70" stroke="{traco}" stroke-width="{largura_traco}" stroke-linejoin="round"/>'
            f'<polygon points="20,68 48,56 76,68 48,84" fill="{cor}" opacity=".50" stroke="{traco}" stroke-width="{largura_traco}" stroke-linejoin="round"/>'
            f'<polygon points="48,12 20,68 48,56" fill="#ffffff" opacity=".20" stroke="{traco}" stroke-width="{largura_traco}" stroke-linejoin="round"/>'
            f'<polygon points="48,12 76,68 48,56" fill="#ffffff" opacity=".10" stroke="{traco}" stroke-width="{largura_traco}" stroke-linejoin="round"/>'
        )
    elif forma == "cubo":
        desenho = (
            f'<polygon points="28,32 50,18 72,32 50,46" fill="#ffffff" opacity=".42" stroke="{traco}" stroke-width="{largura_traco}" stroke-linejoin="round"/>'
            f'<polygon points="28,32 50,46 50,76 28,62" fill="{cor}" stroke="{traco}" stroke-width="{largura_traco}" stroke-linejoin="round"/>'
            f'<polygon points="50,46 72,32 72,62 50,76" fill="{cor}" opacity=".74" stroke="{traco}" stroke-width="{largura_traco}" stroke-linejoin="round"/>'
        )
    elif forma == "paralelepipedo":
        desenho = (
            f'<polygon points="18,38 48,22 82,34 52,50" fill="#ffffff" opacity=".42" stroke="{traco}" stroke-width="{largura_traco}" stroke-linejoin="round"/>'
            f'<polygon points="18,38 52,50 52,78 18,66" fill="{cor}" stroke="{traco}" stroke-width="{largura_traco}" stroke-linejoin="round"/>'
            f'<polygon points="52,50 82,34 82,62 52,78" fill="{cor}" opacity=".72" stroke="{traco}" stroke-width="{largura_traco}" stroke-linejoin="round"/>'
        )
    elif forma == "tetraedro":
        desenho = (
            f'<polygon points="48,12 14,76 48,58" fill="{cor}" stroke="{traco}" stroke-width="{largura_traco}" stroke-linejoin="round"/>'
            f'<polygon points="48,12 82,76 48,58" fill="{cor}" opacity=".66" stroke="{traco}" stroke-width="{largura_traco}" stroke-linejoin="round"/>'
            f'<polygon points="14,76 82,76 48,58" fill="#ffffff" opacity=".30" stroke="{traco}" stroke-width="{largura_traco}" stroke-linejoin="round"/>'
        )
    elif forma == "prisma_triangular":
        desenho = (
            f'<polygon points="18,34 42,18 42,66" fill="{cor}" stroke="{traco}" stroke-width="{largura_traco}" stroke-linejoin="round"/>'
            f'<polygon points="42,18 76,30 76,78 42,66" fill="{cor}" opacity=".70" stroke="{traco}" stroke-width="{largura_traco}" stroke-linejoin="round"/>'
            f'<polygon points="18,34 42,18 76,30 52,46" fill="#ffffff" opacity=".30" stroke="{traco}" stroke-width="{largura_traco}" stroke-linejoin="round"/>'
            f'<polygon points="18,34 42,66 76,78 52,46" fill="{cor}" opacity=".52" stroke="{traco}" stroke-width="{largura_traco}" stroke-linejoin="round"/>'
        )
    else:
        desenho = (
            f'<polygon points="24,28 42,18 64,20 78,34 72,56 54,66 32,64 18,50" fill="{cor}" opacity=".92" stroke="{traco}" stroke-width="{largura_traco}" stroke-linejoin="round"/>'
            f'<polygon points="32,64 54,66 72,56 78,70 60,82 36,78 18,62 18,50" fill="{cor}" opacity=".58" stroke="{traco}" stroke-width="{largura_traco}" stroke-linejoin="round"/>'
            f'<polygon points="24,28 42,18 64,20 78,34 78,70 72,56 54,66 32,64 18,50" fill="#ffffff" opacity=".18" stroke="{traco}" stroke-width="{largura_traco}" stroke-linejoin="round"/>'
        )

    numero_html = ""
    if mostrar_numero:
        numero_html = (
            f'<rect x="33" y="34" width="30" height="24" rx="7" fill="#ffffff" stroke="#111827" stroke-width="3"/>'
            f'<text x="48" y="52" text-anchor="middle" font-size="18" font-family="Arial" font-weight="900" fill="#111827">{numero}</text>'
        )

    return f"""
    <svg viewBox="0 0 96 96" aria-label="Simbolo {numero}: {forma}, {nome_cor}">
      <defs>{defs}</defs>
      <g transform="rotate({rotacao} 48 48)">
        {desenho}
      </g>
      {numero_html}
    </svg>
    """


def estilo_ocorrencia(indice_carta, posicao, numero):
    dados = dados_ocorrencia(indice_carta, posicao, numero)
    return (
        f"left: {dados['esquerda']:.1f}mm; "
        f"top: {dados['topo']:.1f}mm; "
        f"width: {dados['tamanho']:.1f}mm; "
        f"height: {dados['tamanho']:.1f}mm; "
        f"transform: rotate({dados['giro']}deg);"
    )


def dados_ocorrencia(indice_carta, posicao, numero):
    zonas = [
        (46, 12),
        (74, 32),
        (74, 60),
        (46, 80),
        (18, 60),
        (18, 32),
    ]
    zona_indice = (posicao + indice_carta) % len(zonas)
    zona = zonas[zona_indice]
    tamanho = 17 + ((numero * 7 + indice_carta * 5 + posicao * 3) % 6)
    deslocamento_x = ((numero * 11 + indice_carta * 3 + posicao) % 3) - 1
    deslocamento_y = ((numero * 5 + indice_carta * 7 + posicao * 2) % 3) - 1
    giro = ((numero * 13 + indice_carta * 19 + posicao * 29) % 50) - 25

    margem = tamanho / 2
    centro_x = min(92 - margem, max(margem, zona[0] + deslocamento_x))
    centro_y = min(92 - margem, max(margem, zona[1] + deslocamento_y))
    esquerda = centro_x - tamanho / 2
    topo = centro_y - tamanho / 2

    return {
        "zona": zona_indice,
        "esquerda": esquerda,
        "topo": topo,
        "tamanho": tamanho,
        "giro": giro,
    }


def retangulos_sobrepostos(a, b, folga=2):
    direita_a = a["esquerda"] + a["tamanho"]
    base_a = a["topo"] + a["tamanho"]
    direita_b = b["esquerda"] + b["tamanho"]
    base_b = b["topo"] + b["tamanho"]

    return not (
        direita_a + folga <= b["esquerda"]
        or direita_b + folga <= a["esquerda"]
        or base_a + folga <= b["topo"]
        or base_b + folga <= a["topo"]
    )


def dados_logo():
    tamanho = 26
    return {
        "zona": "logo",
        "esquerda": (92 - tamanho) / 2,
        "topo": (92 - tamanho) / 2,
        "tamanho": tamanho,
        "giro": 0,
    }


def identidade_numero(numero):
    nome_cor, cor = CORES_MATEMAGINCANA[(numero - 1) % len(CORES_MATEMAGINCANA)]
    forma = FORMAS[(numero - 1) % len(FORMAS)]
    return forma, nome_cor, cor


def nome_figura(forma):
    nomes = {
        "circulo": "círculo",
        "triangulo": "triângulo",
        "trapezio": "trapézio",
        "piramide_base_quadrada": "pirâmide de base quadrada",
        "paralelepipedo": "paralelepípedo",
        "prisma_triangular": "prisma triangular",
        "prisma_hexagonal": "prisma hexagonal",
    }
    return nomes.get(forma, forma)


def validar_variacoes_visuais(cartas):
    ocorrencias_por_numero = {numero: [] for numero in range(1, 32)}

    for indice_carta, carta in enumerate(cartas, start=1):
        zonas = []
        retangulos = [dados_logo()]
        for posicao, numero in enumerate(carta):
            dados = dados_ocorrencia(indice_carta, posicao, numero)
            zonas.append(dados["zona"])
            retangulos.append(dados)
            ocorrencias_por_numero[numero].append(
                (
                    identidade_numero(numero),
                    dados["esquerda"],
                    dados["topo"],
                    dados["tamanho"],
                    dados["giro"],
                )
            )

        if len(set(zonas)) != len(zonas):
            raise AssertionError(f"Carta {indice_carta} tem simbolos na mesma zona.")

        for indice_a, retangulo_a in enumerate(retangulos):
            for indice_b, retangulo_b in enumerate(retangulos[indice_a + 1:], start=indice_a + 2):
                if retangulos_sobrepostos(retangulo_a, retangulo_b):
                    raise AssertionError(
                        f"Carta {indice_carta} tem sobreposicao entre os simbolos "
                        f"{indice_a} e {indice_b - 1}."
                    )

    for numero, ocorrencias in ocorrencias_por_numero.items():
        identidades = {ocorrencia[0] for ocorrencia in ocorrencias}
        estilos = {ocorrencia[1:] for ocorrencia in ocorrencias}

        if len(identidades) != 1:
            raise AssertionError(f"Numero {numero} mudou de cor ou forma.")

        if len(estilos) <= 1:
            raise AssertionError(f"Numero {numero} nao variou tamanho, posicao ou rotacao.")


def preparar_logo():
    if os.path.exists(LOGO_ORIGEM):
        shutil.copyfile(LOGO_ORIGEM, LOGO_ARQUIVO)
        return True
    return os.path.exists(LOGO_ARQUIVO)


def logo_html():
    if not os.path.exists(LOGO_ARQUIVO):
        return ""
    return f'<img class="logo-carta" src="{LOGO_ARQUIVO}" alt="Logo Matemagincana">'


def gerar_html_cartas(cartas, mostrar_numeros=False):
    cards_html = []
    for indice, carta in enumerate(cartas, start=1):
        simbolos = []
        for posicao, numero in enumerate(carta):
            estilo = estilo_ocorrencia(indice, posicao, numero)
            simbolos.append(
                f'<div class="simbolo" style="{estilo}">'
                f'{simbolo_svg(numero, mostrar_numero=mostrar_numeros, contexto_id=f"c{indice}_n{numero}")}'
                f'</div>'
            )
        simbolos_html = "\n".join(simbolos)
        cards_html.append(
            f"""
            <section class="carta">
              <div class="grade">
                {logo_html()}
                {simbolos_html}
              </div>
            </section>
            """
        )

    return pagina_html("Cartas geometricas", "\n".join(cards_html), tipo="cartas")


def gerar_html_legenda():
    itens = []
    for numero in range(1, 32):
        forma, nome_cor, _cor = identidade_numero(numero)
        itens.append(
            f"""
            <div class="item-legenda">
              <div class="simbolo pequeno">{simbolo_svg(numero, mostrar_numero=False)}</div>
              <strong>{numero}</strong>
              <span>{nome_figura(forma)}</span>
              <span>{nome_cor}</span>
            </div>
            """
        )
    return pagina_html("Legenda geometrica", f'<main class="legenda">{"".join(itens)}</main>', tipo="legenda")


def pagina_html(titulo, corpo, tipo):
    classe = "modo-legenda" if tipo == "legenda" else "modo-cartas"
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{titulo}</title>
  <style>
    * {{
      box-sizing: border-box;
    }}

    body {{
      margin: 0;
      background: #f3f4f6;
      color: #111827;
      font-family: Arial, Helvetica, sans-serif;
    }}

    .modo-cartas {{
      padding: 16px;
    }}

    .carta {{
      width: 112mm;
      height: 112mm;
      display: inline-flex;
      vertical-align: top;
      align-items: center;
      justify-content: center;
      margin: 6mm;
      background: white;
      border: 1.5mm solid #111827;
      border-radius: 50%;
      break-inside: avoid;
      page-break-inside: avoid;
    }}

    .grade {{
      position: relative;
      width: 92mm;
      height: 92mm;
    }}

    .simbolo {{
      position: absolute;
      width: 25mm;
      height: 25mm;
      display: grid;
      place-items: center;
    }}

    .simbolo svg {{
      width: 100%;
      height: 100%;
      display: block;
    }}

    .logo-carta {{
      position: absolute;
      left: 50%;
      top: 50%;
      width: 26mm;
      height: 26mm;
      object-fit: contain;
      transform: translate(-50%, -50%);
      z-index: 0;
    }}

    .simbolo {{
      z-index: 1;
    }}

    .legenda {{
      max-width: 980px;
      margin: 0 auto;
      padding: 24px;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
      gap: 12px;
    }}

    .item-legenda {{
      min-height: 116px;
      display: grid;
      place-items: center;
      gap: 6px;
      padding: 12px;
      background: white;
      border: 1px solid #d1d5db;
      border-radius: 8px;
    }}

    .pequeno {{
      position: static;
      width: 58px;
      height: 58px;
    }}

    @page {{
      size: A4;
      margin: 8mm;
    }}

    @media print {{
      body {{
        background: white;
      }}

      .modo-cartas {{
        padding: 0;
      }}

      .carta {{
        margin: 4mm;
      }}
    }}
  </style>
</head>
<body class="{classe}">
{corpo}
</body>
</html>
"""


if __name__ == "__main__":
    cartas = gerar_cartas()
    validar(cartas)
    validar_variacoes_visuais(cartas)
    preparar_logo()

    with open("cartas_geometricas.html", "w", encoding="utf-8") as arquivo:
        arquivo.write(gerar_html_cartas(cartas))

    with open("cartas_geometricas_com_numeros.html", "w", encoding="utf-8") as arquivo:
        arquivo.write(gerar_html_cartas(cartas, mostrar_numeros=False))

    with open("legenda_geometrica.html", "w", encoding="utf-8") as arquivo:
        arquivo.write(gerar_html_legenda())

    print("Arquivos gerados:")
    print("- cartas_geometricas.html")
    print("- cartas_geometricas_com_numeros.html")
    print("- legenda_geometrica.html")
