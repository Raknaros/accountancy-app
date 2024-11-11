import streamlit as st


st.set_page_config(page_title="Dashboard", page_icon=":material/edit:")

if 'authenticator' not in st.session_state:
    st.error("Error: No se ha cargado el objeto de autenticación.")
else:
    authenticator = st.session_state['authenticator']

    # Puedes realizar la autenticación o cualquier otra operación
    if st.session_state.get("authentication_status"):
        st.write("Bienvenido a la página de carga de pedidos")
        st.header("this is the markdown")
        st.markdown("this is the header")
        st.subheader("this is the subheader")
        st.caption("this is the caption")
        st.code("x=2021")
        st.latex(r''' a+a r^1+a r^2+a r^3 ''')
        # Continúa con el contenido de la página
    else:
        st.error("No estás autenticado.")



#st.image("pages/media/testlogo.png",caption="testlogo")
#st.audio("Audio.mp3")
#st.video("video.mp4")




