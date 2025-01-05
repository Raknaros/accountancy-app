from time import sleep

import streamlit as st

from querys import entidades, usuarios, buzon_sunat

st.set_page_config(page_title="Home", page_icon=":material/edit:", layout="wide")

if st.session_state.get("authentication_status"):
    st.session_state.sidebar()
    st.session_state['authenticator'].logout(location='sidebar', button_name='Cerrar Sesion')
    st.title('Bienvenido')
    tab1, tab2, tab3 = st.tabs(["Entidades", "Usuarios", "Buzon Sunat"])
    with tab1:
        st.dataframe(entidades, height=300, hide_index=True,
                     column_order=['nombre_razon', 'alias', 'ruc', 'usuario_sol', 'clave_sol',
                                   'observaciones', 'activo', 'id', 'related_user', 'suscribed_until', 'suscription'])
    with tab2:
        st.dataframe(buzon_sunat, height=300, hide_index=True,
                     column_order=['ruc', 'id', 'fecha_recepcion', 'asunto', 'observaciones',
                                   'leido',])
    with tab3:
        st.dataframe(usuarios, height=300, hide_index=True,
                     column_order=['usuario', 'contrasena', 'contacto_nombre', 'contacto_correo', 'contacto_numero',
                                   'activo', 'ultimo_ingreso', 'creacion'])
else:
    st.error("Por favor inicia sesion para continuar...")
    sleep(2)
    st.switch_page("app.py")
