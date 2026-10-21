# Dicionário preliminar

Conferir os nomes originais das colunas do Censo Escolar e do Ideb nos dicionários do ano baixado.

| Variável | Descrição | Tipo | Unidade | Fonte / cobertura |
|---|---|---|---|---|
| nu_ano_censo | Ano de referência do Censo Escolar | inteiro | ano | F1; anual |
| co_entidade | Código INEP da escola (25092901 = Interactivo; a escola pública entra quando for escolhida) | texto (8 dígitos) | código | F1, F2 |
| tp_dependencia | Rede: 2 estadual, 3 municipal, 4 privada | categórica | código | F1 |
| qt_mat_med | Matrículas no ensino médio | inteiro | estudantes | F1 |
| qt_mat_fund_af | Matrículas nos anos finais do fundamental | inteiro | estudantes | F1 |
| qt_mat_bas | Matrículas totais na educação básica | inteiro | estudantes | F1; denominador de porte |
| ideb | Ideb da escola (nota) e ano de referência | numérica | pontos (0 a 10) | F3; esperado só para a escola pública |
| id_resposta | Identificador da resposta de direção ou professor | texto | código | F7; sem dado pessoal |
| tem_atividade_ef | A escola já realiza atividade de educação financeira (0 não, 1 sim) | binária | 0/1 | F7 |
| tema_prioritario | Temas priorizados (orçamento, consumo, endividamento, poupança, crédito, investimento, outro); uma linha por tema | categórica | categoria | F7 |
| id_estudante | Código aleatório do estudante (sem nome nem matrícula) | texto | código | F6 |
| serie | Série do ensino médio (1, 2 ou 3) | inteiro | série | F6 |
| turma | Turma do estudante | texto | código | F6 |
| faixa_etaria | Faixa de idade (ex.: até 15, 16 a 17, 18 ou mais) | categórica | categoria | F6; evita idade exata |
| acertos_tema | Percentual de acertos no questionário diagnóstico, por tema | numérica | % | F6 |
| id_voluntario | Código aleatório do voluntário (sem nome nem matrícula) | texto | código | F8 |
| semestre_curso | Semestre cursado em Economia | inteiro | semestre | F8 |
| horas_semanais | Horas semanais que o voluntário pode dedicar | numérica | horas/semana | F8 |
| pisa_pct_baixo_desempenho | Estudantes brasileiros abaixo do nível 2 em letramento financeiro (45,1%) | numérica | % | F4; Brasil, 2022; só referência |
