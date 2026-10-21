# Educação financeira no ensino médio de João Pessoa: piloto voluntário em duas escolas

Projeto aplicado de extensão da disciplina **PSAE00320 – Técnicas de Pesquisa e Análise Econômica II (TPAE II)**, Turma 01, 2026.2, Curso de Ciências Econômicas da UFPB.

## Equipe

- Ana Beatriz Laurentino
- Arthur Almeida
- Gabriel Pinheiro

**Orientador:** Prof. Alessio

## Demandante

**CORECON-PB** (Conselho Regional de Economia da Paraíba), em parceria com estudantes de Ciências Econômicas da UFPB.

## Problema

Estudantes do ensino médio chegam à vida adulta sem educação financeira, que não faz parte do currículo obrigatório das escolas. A ideia é uma iniciativa voluntária em que estudantes de Economia da UFPB, em parceria com o CORECON-PB, ensinem educação financeira no ensino médio. O foco do projeto é um **piloto em duas escolas de João Pessoa**: a Interactivo (particular) e uma escola pública, ainda a definir. Com duas escolas, a comparação é descritiva e não permite generalizar para a cidade.

## Escolas do piloto

- **Escola A (particular):** Interactivo Sistema de Ensino, código INEP 25092901, rua dos Milagres, 1989, Cristo Redentor, João Pessoa. Código e endereço a confirmar no Catálogo de Escolas do INEP.
- **Escola B (pública):** a definir pelos critérios de [`docs/escolha_escola_publica.md`](docs/escolha_escola_publica.md).

## Pergunta (Entrega 3, a ajustar ao novo foco)

Que perfil de escolas, conteúdos e capacidade de voluntários deve orientar uma iniciativa de educação financeira conduzida por estudantes de Economia da UFPB, em parceria com o CORECON-PB? O plano original está em `docs/E03_equipe01_plano.pdf` e descreve um diagnóstico de várias escolas; o alinhamento com o novo foco deve ser combinado com o professor.

## Fontes

Inventário completo em [`docs/inventario_fontes.md`](docs/inventario_fontes.md). Resumo:

| ID | Fonte | Uso |
|---|---|---|
| F1 | Censo Escolar (INEP) | Matrículas e rede das duas escolas |
| F2 | Catálogo de Escolas (INEP) | Cadastro, código INEP e escolha da escola pública |
| F3 | Ideb por escola (INEP) | Contexto de aprendizagem da escola pública |
| F4 | PISA 2022 (OCDE) | Referência nacional de letramento financeiro |
| F5 | Autorizações das escolas e da secretaria da rede pública | Acesso e calendário |
| F6 a F8 | Questionários próprios (estudantes, direção/professores, voluntários) | Oferta, temas, conhecimento e capacidade voluntária |
| F9 | CORECON-PB | Apoio institucional e materiais |

Unidades, chaves e junções: [`docs/unidades_chaves.md`](docs/unidades_chaves.md). Dicionário: [`docs/dicionario_preliminar.md`](docs/dicionario_preliminar.md). Aquisição: [`docs/plano_aquisicao.md`](docs/plano_aquisicao.md). Tarefas: [`docs/tarefas.md`](docs/tarefas.md).

## Estrutura de pastas

```
.
├── README.md
├── .gitignore
├── data/
│   ├── raw/          # dados originais permitidos (grandes ficam fora do Git)
│   └── processed/    # dados tratados e anonimizados
├── notebooks/        # aquisição, tratamento e análise
├── docs/             # planos, inventário, dicionário e instrumentos
└── outputs/          # tabelas, gráficos e produtos
```

## Como reproduzir

1. Leia `docs/plano_aquisicao.md` e baixe os arquivos indicados (os brutos não são versionados).
2. Registre a data de acesso de cada fonte em `docs/inventario_fontes.md`.
3. Rode `python notebooks/01_aquisicao_censo_escolar.py CAMINHO_DO_ZIP ANO [CODIGO_ESCOLA_PUBLICA]` para gerar `data/processed/escolas_piloto_ANO.csv`. Requer `pandas`.

## Segurança

Nunca versionar senhas, tokens, chaves, dados pessoais, documentos internos ou bases restritas. Respostas de questionários só entram anonimizadas, e estudantes menores de idade só respondem com autorização da escola e dos responsáveis.

## Situação atual

- **Entrega 3 (01/10/2026):** definição do problema e plano de pesquisa.
- **Entrega 4 (20/10/2026):** repositório e plano de dados.
- Próximos passos: escolher a escola pública, falar com as direções, enviar ofício à secretaria, elaborar os instrumentos.
- **Entrega final:** 15/12/2026.

## Contato acadêmico

Prof. Alessio · Curso de Ciências Econômicas, UFPB. Contato central da equipe: Ana Beatriz (laurentino.anabia@gmail.com).
