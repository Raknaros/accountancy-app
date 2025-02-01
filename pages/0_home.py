from time import sleep

import streamlit as st
import json

from models import Pdt621
from querys import entidades, usuarios, buzon_sunat, pdt621, Session

st.set_page_config(page_title="Home", page_icon=":material/edit:", layout="wide")


if st.session_state.get("authentication_status"):

    #st.session_state['authenticator'].logout(location='sidebar', button_name='Cerrar Sesion')

    st.title('Bienvenido')


else:
    st.error("Por favor inicia sesion para continuar...")
    sleep(2)
    st.switch_page("app.py")
