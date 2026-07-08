# GeoPar – Matemagincana

O **GeoPar** é um jogo educativo desenvolvido pelo projeto de extensão **Matemagincana (UERJ/FAT Resende)** com o objetivo de tornar o ensino de Geometria mais dinâmico e interativo.

Este repositório contém o código responsável pela geração automática das cartas do jogo, permitindo criar diferentes versões com cores personalizadas e identidade visual do projeto.

## Objetivo

O GeoPar foi criado para auxiliar estudantes na aprendizagem de conceitos geométricos por meio da associação entre figuras, propriedades e características, promovendo o raciocínio lógico e o aprendizado de forma lúdica.

## Funcionalidades

- Geração automática das cartas do jogo;
- Validação da estrutura das cartas;
- Personalização das cores;
- Inserção da identidade visual do Matemagincana;
- Organização dos arquivos gerados.

## Estrutura do projeto

```
.
├── cartas-geometricas.py      # Script principal
├── Matemagincana-Jogamat.png  # Logo utilizada nas cartas
└── README.md
```

## Requisitos

- Python 3.10 ou superior

Dependências utilizadas:

- os
- shutil

Além do módulo responsável pela geração das cartas (`cartas_31.py`).

## Como executar

1. Clone este repositório.

2. Certifique-se de que todos os arquivos necessários estejam na mesma pasta.

3. Execute:

```bash
python cartas-geometricas.py
```

As cartas serão geradas automaticamente conforme as configurações definidas no script.

## Sobre o Matemagincana

O **Matemagincana** é um projeto de extensão da **Universidade do Estado do Rio de Janeiro (UERJ/FAT Resende)** que desenvolve jogos e atividades lúdicas para auxiliar o ensino da Matemática em escolas e eventos científicos, buscando aproximar os estudantes da disciplina de forma divertida e significativa.
