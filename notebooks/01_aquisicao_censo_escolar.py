# -*- coding: utf-8 -*-
"""Aquisição do Censo Escolar (INEP) filtrado para as escolas do piloto.

Fonte: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-escolar
ANTES DE USAR: testado apenas com um ZIP sintético, nunca com o arquivo real do INEP. Baixe o ZIP do ano
pelo portal, confira os nomes das colunas no dicionário do ano e ajuste COLUNAS se necessário.

Uso:  python notebooks/01_aquisicao_censo_escolar.py CAMINHO_DO_ZIP ANO [CODIGO_ESCOLA_PUBLICA ...]
A Interactivo (25092901) já vem incluída; passe o código INEP da escola pública quando ela for escolhida.
"""
import sys, zipfile, io
import pandas as pd

ESCOLAS = ["25092901"]  # Interactivo (código INEP a confirmar no Catálogo de Escolas)
COLUNAS = ["NU_ANO_CENSO", "CO_ENTIDADE", "NO_ENTIDADE", "CO_MUNICIPIO", "TP_DEPENDENCIA",
           "TP_LOCALIZACAO", "TP_SITUACAO_FUNCIONAMENTO", "QT_MAT_BAS", "QT_MAT_FUND_AF", "QT_MAT_MED"]

def main(zip_path, ano, extras):
    codigos = ESCOLAS + list(extras)
    with zipfile.ZipFile(zip_path) as z:
        nome = next(n for n in z.namelist() if n.lower().endswith(".csv") and "microdados" in n.lower())
        with z.open(nome) as f:
            df = pd.read_csv(io.TextIOWrapper(f, encoding="latin-1"), sep=";", dtype=str, low_memory=False)
    faltando = [c for c in COLUNAS if c not in df.columns]
    if faltando:
        sys.exit("Colunas ausentes (confira o dicionário do ano): %s" % faltando)
    df = df[COLUNAS]
    df = df[df["CO_ENTIDADE"].isin(codigos)]
    achados = set(df["CO_ENTIDADE"])
    for c in codigos:
        if c not in achados:
            print("AVISO: código %s não encontrado no Censo %s" % (c, ano))
    for c in ["QT_MAT_BAS", "QT_MAT_FUND_AF", "QT_MAT_MED"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df.columns = [c.lower() for c in df.columns]
    saida = "data/processed/escolas_piloto_%s.csv" % ano
    df.to_csv(saida, index=False)
    print("Escolas encontradas:", len(df), "->", saida)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2], sys.argv[3:])
