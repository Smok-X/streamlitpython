import streamlit as st
import pandas as pd

st.set_page_config(page_title='Estatísticas Brasileirão')

with st.container():
    st.subheader('Campeonato Brasileiro de Futebol')
    st.title('Tabela em Estatística do Brasileirão Betano 2025')
    st.write('Informações sobre a quantidade de gols marcados neste Brasileirão Betano 2025')
    st.write('Quer saber mais sobre Brasileirão? [Clique aqui](https://ge.globo.com/futebol/brasileirao-serie-a/)')

@st.cache_data
def carregar_dados():
        tabela = pd.read_csv('resultados.csv')
        return tabela

with st.container():
    st.write('---')
    qtde_dias = st.selectbox('Selecione o período', ['7D', '10D', '15D'])
    num_dias = int(qtde_dias.replace('D', ''))
    dados = carregar_dados()
    dados = dados[-num_dias:]

    st.area_chart(dados,x='Data', y='Contratos')