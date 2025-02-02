from time import sleep

import streamlit as st
import json

from models import Pdt621
from querys import entidades, usuarios, buzon_sunat, pdt621, Session

st.set_page_config(page_title="Home", page_icon=":material/edit:", layout="wide")

if st.session_state.get("authentication_status"):

    #st.session_state['authenticator'].logout(location='sidebar', button_name='Cerrar Sesion')

    st.title('Bienvenido')
    col1, col2 = st.columns([1, 6])
    #st.session_state['authenticator'].logout(location='sidebar', button_name='Cerrar Sesion')

    def info_resumen(alias=None):
        if alias == None:
            pass
        else:
            entidad = st.session_state.entidades.loc[st.session_state.entidades['alias'] == alias]
            st.write("**RUC:** " + str(entidad['ruc'].values[0]))
            st.write("**Usuario SOL:** " + str(entidad['usuario_sol'].values[0]))
            st.write("**Clave SOL:** " + str(entidad['clave_sol'].values[0]))


    with col1.container(height=800, border=False):
        search_query = st.text_input("Buscar entidad")
        entidades_filtradas = st.session_state.entidades.loc[
            st.session_state.entidades['alias'].str.contains(search_query, case=False) & (
                        st.session_state.entidades['activo'] == True)]
        for entidad in entidades_filtradas['alias'].tolist():
            if st.button(entidad, use_container_width=True, type="primary", key=entidad):
                st.session_state.entidad_seleccionada = entidad

    with col2:
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Resumen", "Ventas", "Compras", "Declaraciones", "Pagos"])
        with tab1:
            icol1, icol2, icol3, icol4, icol5, icol6, icol7, icol8 = st.columns(8)
            with icol1:
                if 'entidad_seleccionada' in st.session_state:
                    info_resumen(st.session_state.entidad_seleccionada)



else:
    st.error("Por favor inicia sesion para continuar...")
    sleep(2)
    st.switch_page("app.py")
