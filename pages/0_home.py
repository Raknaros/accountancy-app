from time import sleep

import streamlit as st
import json

from models import Pdt621
from querys import entidades, usuarios, buzon_sunat, pdt621, Session

    #st.set_page_config(page_title="Home", page_icon=":material/edit:", layout="wide")



#st.session_state.sidebar()
if 'datos' not in st.session_state:
    st.session_state.pdt621 = pdt621()

if st.session_state.get("authentication_status"):
    #st.session_state.sidebar()
    st.session_state['authenticator'].logout(location='sidebar', button_name='Cerrar Sesion')
    st.html("""<nav>
    <ul>
        <li><a href="#">Inicio</a></li>
        <li><a href="#">Productos</a></li>
        <li><a href="#">Contacto</a></li>
    </ul>
</nav>""")
    st.title('Bienvenido')


else:
    st.error("Por favor inicia sesion para continuar...")
    sleep(2)
    st.switch_page("app.py")
