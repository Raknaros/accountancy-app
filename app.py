import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(page_title="Home", page_icon=":material/edit:", layout="wide")

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Pre-hashing all plain text passwords once
# stauth.Hasher.hash_passwords(config['credentials'])

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

if 'authenticator' not in st.session_state:
    st.session_state['authenticator'] = authenticator

if st.session_state['authentication_status']:
    authenticator.logout()
    user_roles = config['credentials']['usernames'][st.session_state["username"]].get('roles', [])
    st.write(f"Roles de {st.session_state["name"]}: {user_roles}")
    # Luego, puedes usar los roles para condicionar accesos:
    if 'admin' in user_roles:
        st.write("Bienvenido, administrador.")
    elif 'editor' in user_roles:
        st.write("Bienvenido, editor.")
    elif 'viewer' in user_roles:
        st.write("Bienvenido, visor.")
elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')
