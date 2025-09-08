import requests
import re
import json
import pandas as pd
import streamlit as st
import time

st.title("🛠️ Produtos Aerofolio - Jocar")

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def extrair_pagina(url):
    """Extrai produtos da página usando JSON embutido"""
    r = requests.get(url, headers=HEADERS, timeout=15)
    if r.status_code != 200:
        return []

    html = r.text

    # Expressão para capturar o JSON de produtos
    pattern = r"gtag\('event','view_item_list',(\{.*?\})\);"
    match = re.search(pattern, html, re.DOTALL)

    if not match:
        return []

    raw_json = match.group(1)
    raw_json = raw_json.replace("'", '"')

    try:
        data = json.loads(raw_json)
        return data.get("items", [])
    except:
        return []

# =======================================================
# Entrada do usuário
# =======================================================
categoria = st.text_input("Cole a URL da categoria:", 
    "https://www.jocar.com.br/acabamentos-externos/aerofolio/?PG=1"
)

if st.button("🔎 Extrair Produtos"):
    # Detectar URL base para paginação
    base_url = categoria.split("?PG=")[0] + "?PG={}"
    pagina = 1
    todos_produtos = []

    while True:
        url = base_url.format(pagina)
        st.write(f"📄 Extraindo página {pagina}...")
        items = extrair_pagina(url)

        if not items:
            break

        todos_produtos.extend(items)
        pagina += 1
        time.sleep(1)  # respeitar servidor

    if todos_produtos:
        df = pd.DataFrame(todos_produtos)

        # Renomear colunas principais
        df.rename(columns={
            "item_id": "ID",
            "item_name": "Produto",
            "price": "Preço",
            "currency": "Moeda"
        }, inplace=True)

        # Filtros interativos
        st.subheader("📊 Tabela Interativa")
        filtro_nome = st.text_input("Filtrar por nome do produto:")
        filtro_preco_min = st.number_input("Preço mínimo:", min_value=0.0, value=0.0)
        filtro_preco_max = st.number_input("Preço máximo:", min_value=0.0, value=float(df["Preço"].max()))

        df_filtrado = df.copy()

        if filtro_nome:
            df_filtrado = df_filtrado[df_filtrado["Produto"].str.contains(filtro_nome, case=False, na=False)]

        df_filtrado = df_filtrado[(df_filtrado["Preço"] >= filtro_preco_min) & (df_filtrado["Preço"] <= filtro_preco_max)]

        # Mostrar tabela interativa
        st.dataframe(df_filtrado, use_container_width=True)

        st.success(f"✅ {len(df_filtrado)} produtos encontrados após filtros.")
    else:
        st.warning("⚠️ Nenhum produto encontrado.")
