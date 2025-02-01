import streamlit_authenticator as stauth
import streamlit as st
import yaml
from yaml.loader import SafeLoader

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

st.set_page_config(page_title="Login", page_icon=":material/edit:", layout="wide")

hide_streamlit_menu = """
    <style>
        #MainMenu {visibility: hidden;} /* Oculta el menú de Streamlit */
        footer {visibility: hidden;} /* Oculta el footer "Made with Streamlit" */
        header {visibility: hidden;} /* Opcional: Oculta la barra de encabezado completa */
    </style>
"""
st.html(hide_streamlit_menu)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

try:
    authenticator.login(captcha=True)
except Exception as e:
    st.error(e)


def mostrar_navbar():

    with open("added/navbar.html", "r") as html_file:
        navbar_html = html_file.read()

    st.html(navbar_html)


if 'authenticator' not in st.session_state:
    st.session_state['authenticator'] = authenticator

if st.session_state['authentication_status']:
    user_roles = config['credentials']['usernames'][st.session_state["username"]].get('roles', [])

    if 'admin' in user_roles:
        if 'gerencia_navbar' not in st.session_state:
            pass
            st.session_state['navbar'] = mostrar_navbar
    else:
        if 'other_navbar' not in st.session_state:
            pass
            st.session_state['navbar'] = mostrar_navbar
    st.switch_page("pages/1_dashboard.py")
elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')
