from time import sleep

import streamlit as st
import json

from models import Pdt621
from querys import entidades, usuarios, buzon_sunat, pdt621, Session

st.set_page_config(page_title="Home", page_icon=":material/edit:", layout="wide")#


if st.session_state.get("authentication_status"):
    st.title('Bienvenido')
    col1, col2 = st.columns([1, 7])
    #st.session_state['authenticator'].logout(location='sidebar', button_name='Cerrar Sesion')
    with col1:
        st.header("ENTIDADES")
        for entidad in ['IMPULSAMAS', 'ENFOCATE', 'INVERSIONES SONIC', 'JMV', 'PARJU']:
            if entidad[0] == 'I':
                st.button(entidad, icon="📨", use_container_width=True)#
            else:
                st.button(entidad, use_container_width=True)

        #st.selectbox("Elija una entidad", )
    with col2:
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["Resumen", "Ventas", "Compras", "Declaraciones", "Pagos"])
        with tab1:
            icol1, icol2, icol3, icol4, icol5, icol6, icol7, icol8 = st.columns(8)
            icol1.write("**20606285858**")
            icol1.write("**TONERTAT**")
            icol1.write("**rcavinsio**")
else:
    st.error("Por favor inicia sesion para continuar...")
    sleep(2)
    st.switch_page("app.py")
