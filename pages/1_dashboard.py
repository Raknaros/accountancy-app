from time import sleep

import streamlit as st
from streamlit_navigation_bar import st_navbar

st.set_page_config(page_title="Dashboard", page_icon=":material/edit:", layout="wide")
st.session_state.sidebar()

if st.session_state.get("authentication_status"):

    #st.session_state['authenticator'].logout(location='navbar', button_name='Cerrar Sesion')
    st.title('Bienvenido')

else:
    st.error("Por favor inicia sesion para continuar...")
    sleep(2)
    st.switch_page("app.py")


