# 🛠️ Web Scraping de Autopeças

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![License](https://img.shields.io/badge/license-MIT-green)

Este projeto realiza **web scraping** da loja online [Jocar](https://www.jocar.com.br/), extraindo informações de produtos da categoria de **aerofólios** e exibindo os resultados em uma interface interativa com **Streamlit**.  

---

## 🚀 Funcionalidades
- 🔎 **Extração automática** de produtos de todas as páginas da categoria.  
- 📊 Conversão dos dados para **pandas DataFrame**.  
- 🏷️ Renomeação e organização de colunas principais (`ID`, `Produto`, `Preço`, `Moeda`).  
- 🎛️ Filtros interativos:
  - Busca por nome do produto.  
  - Faixa de preços mínima e máxima.  
- 🖥️ Exibição de tabela dinâmica diretamente na interface.  
- ⏳ Intervalo entre requisições para respeitar o servidor.  

---

## 🖼️ Demonstração
1. Informe a **URL da categoria** (exemplo: aerofólios).  
2. O app realiza a **paginação automática** e coleta os produtos.  
3. Os dados são exibidos em uma **tabela interativa** com filtros.   

---

## 🛠️ Tecnologias Utilizadas
- [Python](https://www.python.org/)  
- [Requests](https://pypi.org/project/requests/)  
- [Regex (re)](https://docs.python.org/3/library/re.html)  
- [JSON](https://docs.python.org/3/library/json.html)  
- [Pandas](https://pandas.pydata.org/)  
- [Streamlit](https://streamlit.io/)  

---

## ▶️ Como Executar

Clone o repositório:

git clone https://github.com/seu-usuario/nome-do-repo.git
cd nome-do-repo

python -m streamlit run

## ⚠️ Aviso

Este projeto é apenas para fins educacionais e de análise de dados.
Respeite os termos de uso do site alvo ao realizar scraping.
