from time import sleep

import streamlit as st

#st.set_page_config(page_title="Dashboard", page_icon=":material/edit:", layout="wide")

if st.session_state.get("authentication_status"):
    #st.session_state.sidebar()
    st.session_state['authenticator'].logout(location='sidebar', button_name='Cerrar Sesion')
    st.title('Bienvenido')

    # Using "with" notation
    with st.sidebar:
        add_radio = st.radio(
            "Choose a shipping method",
            ("Standard (5-15 days)", "Express (2-5 days)")
        )

else:
    st.error("Por favor inicia sesion para continuar...")
    sleep(2)
    st.switch_page("app.py")
