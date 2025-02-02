import pandas as pd
from sqlalchemy import create_engine
import toml
import streamlit as st
import psycopg2
from sqlalchemy.orm import sessionmaker

salessystem_user = st.secrets['DB_USERNAME_SS']
salessystem_token = st.secrets['DB_TOKEN_SS']
salessystem_database = st.secrets['DB_DATABASE_SS']
salessystem_source = st.secrets['DB_SOURCE_SS']
warehouse_user = st.secrets['DB_USERNAME_WH']
warehouse_token = st.secrets['DB_TOKEN_WH']
warehouse_database = st.secrets['DB_DATABASE_WH']
warehouse_source = st.secrets['DB_SOURCE_WH']

salessystem_url = f'mysql+pymysql://{salessystem_user}:{salessystem_token}@{salessystem_source}:3306/{salessystem_database}'
warehouse_url = f'postgresql://{warehouse_user}:{warehouse_token}@{warehouse_source}:5432/{warehouse_database}'

salessystem = create_engine(salessystem_url, connect_args={"connect_timeout": 10})

warehouse = create_engine(warehouse_url, connect_args={"connect_timeout": 10})

Session = sessionmaker(bind=warehouse)

def ejecutar_consulta(query, conexion, parse_dates=None):
    result = None
    while result is None:
        try:
            result = pd.read_sql(query, con=conexion, parse_dates=parse_dates)
        except Exception as e:
            st.warning(f"Error en la consulta: {e}. Reintentando...")
    return result


# Consultas específicas
def pdt621():
    query = "SELECT * FROM acc._9"
    return ejecutar_consulta(query, warehouse)

def ventas():
    query = "SELECT * FROM acc._9"
    return ejecutar_consulta(query, warehouse)

def compras():
    query = "SELECT * FROM acc._9"
    return ejecutar_consulta(query, warehouse)

def pagos_sunat():
    query = "SELECT * FROM acc._9"
    return ejecutar_consulta(query, warehouse)

def entidades():
    query = "SELECT * FROM priv.entities"
    return ejecutar_consulta(query, warehouse)

def usuarios():
    query = "SELECT * FROM priv.users"
    return ejecutar_consulta(query, warehouse)

def buzon_sunat():
    query = "SELECT * FROM priv.buzon_sunat"
    return ejecutar_consulta(query, warehouse)

def ficha_ruc():
    query = "SELECT * FROM acc._9"
    return ejecutar_consulta(query, warehouse)

def ide():
    query = "SELECT * FROM acc._9"
    return ejecutar_consulta(query, warehouse)

def tra():
    query = "SELECT * FROM acc._9"
    return ejecutar_consulta(query, warehouse)


def inicializar_datos():
    if 'pdt621' not in st.session_state:
        st.session_state.pdt621 = pdt621()
    if 'ventas' not in st.session_state:
        st.session_state.ventas = ventas()
    if 'compras' not in st.session_state:
        st.session_state.compras = compras()
    if 'pagos_sunat' not in st.session_state:
        st.session_state.pagos_sunat = pagos_sunat()
    if 'entidades' not in st.session_state:
        st.session_state.entidades = entidades()
    if 'usuarios' not in st.session_state:
        st.session_state.usuarios = usuarios()
    if 'buzon_sunat' not in st.session_state:
        st.session_state.buzon_sunat = buzon_sunat()
    if 'ficha_ruc' not in st.session_state:
        st.session_state.ficha_ruc = ficha_ruc()
    if 'tregistro_ide' not in st.session_state:
        st.session_state.tregistro_ide = ide()
    if 'tregistro_tra' not in st.session_state:
        st.session_state.tregistro_tra = tra()


def actualizar_datos():
    st.session_state.pdt621 = pdt621()
    st.session_state.ventas = ventas()
    st.session_state.compras = compras()
    st.session_state.pagos_sunat = pagos_sunat()
    st.session_state.entidades = entidades()
    st.session_state.usuarios = usuarios()
    st.session_state.buzon_sunat = buzon_sunat()
    st.session_state.ficha_ruc = ficha_ruc()
    st.session_state.tregistro_ide = ide()
    st.session_state.tregistro_tra = tra()