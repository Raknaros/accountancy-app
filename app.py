import streamlit_authenticator as stauth
import streamlit as st
import yaml
from streamlit_navigation_bar import st_navbar
from yaml.loader import SafeLoader
from time import sleep

#from services.Querys import adquirientes, proveedores, catalogo

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

st.set_page_config(page_title="Login", page_icon=":material/edit:", layout="wide")

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


def other_navbar():
    st_navbar(["Home", "Resumen"])
    #st.sidebar.page_link('pages/2_cargar_pedidos.py', label='Pedidos')
    #st.sidebar.page_link('pages/3_cargar_cotizaciones.py', label='Cotizaciones')
    #st.sidebar.page_link('pages/4_cargar_bancarizaciones.py', label='Bancarizaciones', disabled=True)


def gerencia_navbar():
    st_navbar(["Home", "Resumen"])
    #st.sidebar.page_link('pages/2_cargar_pedidos.py', label='Pedidos')
    #st.sidebar.page_link('pages/3_cargar_cotizaciones.py', label='Cotizaciones')
    #st.sidebar.page_link('pages/4_cargar_bancarizaciones.py', label='Bancarizaciones', disabled=True)


if 'authenticator' not in st.session_state:
    st.session_state['authenticator'] = authenticator

if st.session_state['authentication_status']:
    user_roles = config['credentials']['usernames'][st.session_state["username"]].get('roles', [])
    if 'admin' in user_roles:
        if 'navbar' not in st.session_state:
            st.session_state.sidebar = gerencia_navbar
    else:
        if 'navbar' not in st.session_state:
            st.session_state.sidebar = other_navbar
    st.switch_page("pages/0_home.py")
elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')