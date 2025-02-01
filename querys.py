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
    return ejecutar_consulta(query, salessystem)

def ventas():
    query = "SELECT * FROM acc._9"
    return ejecutar_consulta(query, salessystem)

def compras():
    query = "SELECT * FROM acc._9"
    return ejecutar_consulta(query, salessystem)

def pagos_sunat():
    query = "SELECT * FROM acc._9"
    return ejecutar_consulta(query, salessystem)

def entidades():
    query = "SELECT * FROM priv.entities"
    return ejecutar_consulta(query, salessystem)

def usuarios():
    query = "SELECT * FROM priv.users"
    return ejecutar_consulta(query, salessystem)

def buzon_sunat():
    query = "SELECT * FROM priv.buzon_sunat"
    return ejecutar_consulta(query, salessystem)

def ficha_ruc():
    query = "SELECT * FROM acc._9"
    return ejecutar_consulta(query, salessystem)

def ide():
    query = "SELECT * FROM acc._9"
    return ejecutar_consulta(query, salessystem)

def tra():
    query = "SELECT * FROM acc._9"
    return ejecutar_consulta(query, salessystem)


def inicializar_datos():
    if 'bancarizaciones' not in st.session_state:
        st.session_state.bancarizaciones = bancarizaciones()
    if 'adquirientes' not in st.session_state:
        st.session_state.adquirientes = adquirientes()
    if 'proveedores' not in st.session_state:
        st.session_state.proveedores = proveedores()
    if 'catalogo' not in st.session_state:
        st.session_state.catalogo = catalogo()
    if 'pre_detalle' not in st.session_state:
        st.session_state.pre_detalle = pre_detalle()
    if 'lista_facturas' not in st.session_state:
        st.session_state.lista_facturas = lista_facturas()
    if 'lista_guias' not in st.session_state:
        st.session_state.lista_guias = lista_guias()
    if 'pedidos' not in st.session_state:
        st.session_state.pedidos = pedidos()
    if 'cotizaciones' not in st.session_state:
        st.session_state.cotizaciones = cotizaciones()


def actualizar_datos():
    st.session_state.bancarizaciones = bancarizaciones()
    st.session_state.adquirientes = adquirientes()
    st.session_state.proveedores = proveedores()
    st.session_state.catalogo = catalogo()
    st.session_state.pre_detalle = pre_detalle()
    st.session_state.lista_facturas = lista_facturas()
    st.session_state.lista_guias = lista_guias()
    st.session_state.pedidos = pedidos()
    st.session_state.cotizaciones = cotizaciones()