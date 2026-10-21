# Unidades, chaves e junções

A chave que separa as escolas é o código INEP (co_entidade); as respostas se ligam à escola e à turma.

| Tabela | Unidade de análise | Chave | Periodicidade | Origem |
|---|---|---|---|---|
| T1 escolas_censo | escola × ano do Censo (duas escolas) | co_entidade + nu_ano_censo | Anual | F1, F2, F3 |
| T2 resp_direcao | resposta de direção ou professor | id_resposta; co_entidade da escola | Única, 2026.2 | F7 |
| T3 resp_estudantes | estudante (anonimizado) | id_estudante (código aleatório, sem nome); co_entidade da escola | Única, 2026.2 (ou antes e depois da ação, se houver tempo) | F6 |
| T4 resp_voluntarios | voluntário (anonimizado) | id_voluntario (código aleatório, sem nome) | Única, 2026.2 | F8 |

## Junções

| Junção | Tabelas | Chave / método | Cardinalidade | Cuidados |
|---|---|---|---|---|
| J1 | T2 e T3 com T1 | co_entidade | n:1 (várias respostas por escola) | São só duas escolas, então a comparação é descritiva; usar o ano do Censo mais recente e lembrar que pode estar defasado em relação a 2026 |
| J2 | T3 com cadastro de turmas (F5) | co_entidade + serie + turma | n:1 (vários estudantes por turma) | Serve para calcular a taxa de resposta por turma; o cadastro de turmas vem da direção e não é versionado |
| J3 | T4 com T3 | Alocação do voluntário a escola e turma (fase de desenho) | n:n | Fica agregada (voluntários por escola e turma); nunca identificar voluntário nem estudante |
