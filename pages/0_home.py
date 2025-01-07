from time import sleep

import streamlit as st
import json

from querys import entidades, usuarios, buzon_sunat, pdt621

st.set_page_config(page_title="Home", page_icon=":material/edit:", layout="wide")

if 'datos' not in st.session_state:
    st.session_state.pdt621 = pdt621()

if st.session_state.get("authentication_status"):
    st.session_state.sidebar()
    st.session_state['authenticator'].logout(location='sidebar', button_name='Cerrar Sesion')
    st.title('Bienvenido')
    tab1, tab2, tab3 = st.tabs(["Entidades", "Usuarios", "Buzon Sunat"])
    with tab1:
        st.dataframe(entidades, height=300, hide_index=True,
                     column_order=['nombre_razon', 'alias', 'ruc', 'usuario_sol', 'clave_sol',
                                   'observaciones', 'activo', 'id', 'related_user', 'suscribed_until', 'suscription'],
                     column_config={
                         "nombre_razon": st.column_config.TextColumn(
                             label="Nombre o Razon Social",
                         ),
                         "alias": st.column_config.TextColumn(
                             label="Alias"
                         ),
                         "ruc": st.column_config.NumberColumn(
                             "RUC",
                             format='%d'
                         ),
                         "usuario_sol": st.column_config.TextColumn(
                             label="Usuario SOL",
                         ),
                         "clave_sol": st.column_config.TextColumn(
                             label="Clave SOL",
                         ),
                         "observaciones": st.column_config.TextColumn(
                             label="Observaciones",
                         ),
                         "activo": st.column_config.NumberColumn(
                             label="Activo",
                         ),
                         "id": st.column_config.NumberColumn(
                             label="ID",
                             format='%d'
                         ),
                         "related_user": st.column_config.NumberColumn(
                             label="Usuario relacionado",
                             format='%d'
                         ),
                         "suscribed_until": st.column_config.DateColumn(
                             label="Suscrito hasta",
                             format='DD/MM/YYYY'
                         ),
                         "suscription": st.column_config.NumberColumn(
                             label="Tipo de suscripcion",
                             format='%d'
                         ),
                     }
                     )
    with tab2:
        st.data_editor(st.session_state.pdt621, key='edit_pdt621', height=300, hide_index=True, num_rows='dynamic',
                       column_order=['ruc', 'periodo_tributario', 'numero_orden', 'fecha_presentacion',
                                     '_101', '_107', '_301', '_145'],
                       column_config={
                           "ruc": st.column_config.NumberColumn(
                               label="RUC",
                               format='%d',
                           ),
                           "periodo_tributario": st.column_config.NumberColumn(
                               label="Periodo",
                               format='%d',
                           ),
                           "numero_orden": st.column_config.NumberColumn(
                               "Numero de orden",
                               format='%d',
                           ),
                           "fecha_presentacion": st.column_config.DateColumn(
                               label="Fecha de presentacion",
                               format='DD/MM/YYYY'
                           ),
                           "_101": st.column_config.NumberColumn(
                               label="Ventas",
                               format='%d',
                           ),
                           "_107": st.column_config.NumberColumn(
                               label="Compras",
                               format='%d',
                           ),
                           "_301": st.column_config.NumberColumn(
                               label="Ingresos",
                               format='%d',
                           ),
                           "_145": st.column_config.NumberColumn(
                               label="Saldo a favor periodo anterior",
                               format='%d',
                           ),
                       }
                       )
    with tab3:
        st.dataframe(buzon_sunat, height=300, hide_index=True,
                     column_order=['ruc', 'id', 'fecha_recepcion', 'asunto', 'observaciones',
                                   'leido', ])




    def update_db():
        df = st.session_state.pdt621
        cambios = st.session_state["edit_pdt621"]
        #df.get_loc(0)
        #if cambios.get("edited_rows") is
        return st.write(cambios.get("added_rows"))
        #st.session_state.pdt621 = pdt621()


    st.button('Actualizar', type="primary", on_click=update_db)

else:
    st.error("Por favor inicia sesion para continuar...")
    sleep(2)
    st.switch_page("app.py")
