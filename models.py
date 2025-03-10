from sqlalchemy import Column, Integer, String, BigInteger, Float, Date, Boolean, Time
from sqlalchemy.orm import declarative_base
import pymysql

Base = declarative_base()


class Pdt621(Base):
    __tablename__ = '_9'
    __table_args__ = {'schema': 'acc'}


    id = Column(BigInteger, primary_key=True, autoincrement=True)
    ruc = Column(BigInteger, nullable=True)
    subdiario = Column(Integer, nullable=True)
    periodo_tributario = Column(Integer, nullable=True)
    numero_orden = Column(BigInteger, nullable=True)
    fecha_presentacion = Column(Date, nullable=True)
    _100 = Column(Integer, nullable=True)
    _101 = Column(Integer, nullable=True)
    _102 = Column(Integer, nullable=True)
    _103 = Column(Integer, nullable=True)
    _160 = Column(Integer, nullable=True)
    _161 = Column(Integer, nullable=True)
    _162 = Column(Integer, nullable=True)
    _163 = Column(Integer, nullable=True)
    _106 = Column(Integer, nullable=True)
    _127 = Column(Integer, nullable=True)
    _105 = Column(Integer, nullable=True)
    _109 = Column(Integer, nullable=True)
    _112 = Column(Integer, nullable=True)
    _107 = Column(Integer, nullable=True)
    _108 = Column(Integer, nullable=True)
    _110 = Column(Integer, nullable=True)
    _111 = Column(Integer, nullable=True)
    _113 = Column(Integer, nullable=True)
    _114 = Column(Integer, nullable=True)
    _115 = Column(Integer, nullable=True)
    _116 = Column(Integer, nullable=True)
    _117 = Column(Integer, nullable=True)
    _119 = Column(Integer, nullable=True)
    _120 = Column(Integer, nullable=True)
    _122 = Column(Integer, nullable=True)
    _172 = Column(Integer, nullable=True)
    _169 = Column(Integer, nullable=True)
    _173 = Column(Float, nullable=True)
    _340 = Column(Integer, nullable=True)
    _341 = Column(Integer, nullable=True)
    _182 = Column(Integer, nullable=True)
    _301 = Column(Integer, nullable=True)
    _312 = Column(Integer, nullable=True)
    _380 = Column(Float, nullable=True)
    _315 = Column(Float, nullable=True)
    _140 = Column(Integer, nullable=True)
    _145 = Column(Integer, nullable=True)
    _184 = Column(Integer, nullable=True)
    _171 = Column(Integer, nullable=True)
    _168 = Column(Integer, nullable=True)
    _164 = Column(Integer, nullable=True)
    _179 = Column(Integer, nullable=True)
    _176 = Column(Integer, nullable=True)
    _165 = Column(Integer, nullable=True)
    _681 = Column(Integer, nullable=True)
    _185 = Column(Integer, nullable=True)
    _187 = Column(Integer, nullable=True)
    _188 = Column(Integer, nullable=True)
    _353 = Column(Integer, nullable=True)
    _351 = Column(Integer, nullable=True)
    _352 = Column(Integer, nullable=True)
    _347 = Column(Integer, nullable=True)
    _342 = Column(Integer, nullable=True)
    _343 = Column(Integer, nullable=True)
    _344 = Column(Integer, nullable=True)
    _302 = Column(Integer, nullable=True)
    _303 = Column(Integer, nullable=True)
    _304 = Column(Integer, nullable=True)
    _326 = Column(Integer, nullable=True)
    _327 = Column(Integer, nullable=True)
    _305 = Column(Integer, nullable=True)
    _328 = Column(Integer, nullable=True)
    _682 = Column(Integer, nullable=True)
    _317 = Column(Integer, nullable=True)
    _319 = Column(Integer, nullable=True)
    _324 = Column(Integer, nullable=True)
    observaciones = Column(String(255), nullable=True)
    _683 = Column(Integer, nullable=True)
    notas = Column(String(255), nullable=True)


"""
class ListaFacturas(Base):
    __tablename__ = 'lista_facturas'
    #__table_args__ = {'extend_existing': True}
    alias = Column(String(12), nullable=True)
    cui = Column(String(35), primary_key=True)
    guia = Column(String(8), nullable=True)
    numero = Column(String(8), nullable=True)
    ruc = Column(BigInteger, nullable=True)
    emision = Column(Date, nullable=True)
    descripcion = Column(String(50), primary_key=True)
    unidad_medida = Column(String(5), nullable=True)
    cantidad = Column(Float, nullable=True)
    p_unit = Column(Float, nullable=True)
    sub_total = Column(Float, nullable=True)
    igv = Column(Float, nullable=True)
    total = Column(Float, nullable=True)
    vencimiento = Column(Date, nullable=True)
    moneda = Column(String(4), nullable=True)


class ListaGuias(Base):
    __tablename__ = 'lista_guias'
    alias = Column(String(35), nullable=True)
    cui = Column(String(35), primary_key=True)
    traslado = Column(Date, primary_key=True)
    partida = Column(String(50), nullable=True)
    llegada = Column(String(50), nullable=True)
    placa = Column(String(8), nullable=True)
    conductor = Column(String(10), nullable=True)
    datos_adicionales = Column(String(35), nullable=True)
    observaciones = Column(String(35), nullable=True)


class Pedidos(Base):
    __tablename__ = 'pedidos'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    cod_pedido = Column(String(10), nullable=True)
    fecha_pedido = Column(Date, nullable=True)
    periodo = Column(Integer, nullable=True)
    adquiriente = Column(BigInteger, nullable=True)
    importe_total = Column(Float, nullable=True)
    rubro = Column(String(35), nullable=True)
    promedio_factura = Column(Integer, nullable=True)
    contado_credito = Column(String(30), nullable=True)
    bancariza = Column(Boolean, nullable=True)
    notas = Column(String(50), nullable=True)
    estado = Column(String(20), nullable=True)
    punto_entrega = Column(String(50), nullable=True)


class Bancarizaciones(Base):
    __tablename__ = 'v_bcp'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    dato_referencial = Column(String(35), nullable=True)
    fecha_operacion = Column(Date, nullable=True)
    hora_operacion = Column(Time, nullable=True)
    numero_operacion = Column(Integer, nullable=True)
    importe = Column(Float, nullable=True)
    adquiriente = Column(String(35), nullable=True)
    proveedor = Column(String(35), nullable=True)
    documento_relacionado = Column(String(13), nullable=True)
    customer_id = Column(String(5), nullable=True)
    observaciones = Column(String(50), nullable=True)
    cui = Column(String(30), nullable=True)


class Facturas(Base):
    __tablename__ = 'facturas'
    cod_pedido = Column(String(10), primary_key=True)
    cuo = Column(Integer, primary_key=True)
    alias = Column(String(12), nullable=True)
    guia = Column(String(13), nullable=True)
    serie = Column(String(4), nullable=True)
    numero = Column(BigInteger, nullable=True)
    emision = Column(Date, nullable=True)
    ruc = Column(BigInteger, nullable=True)
    nombre_razon = Column(String(35), nullable=True)
    moneda = Column(String(4), nullable=True)
    descripcion = Column(String(50), nullable=True)
    unid_medida = Column(String(5), nullable=True)
    cantidad = Column(Float, nullable=True)
    precio_unit = Column(Float, nullable=True)
    forma_pago = Column(String(35), nullable=True)
    estado = Column(String(20), nullable=True)
    observaciones = Column(String(50), nullable=True)
    vencimiento = Column(Date, nullable=True)
    cuota1 = Column(Float, nullable=True)
    vencimiento2 = Column(Date, nullable=True)
    cuota2 = Column(Float, nullable=True)
    vencimiento3 = Column(Date, nullable=True)
    cuota3 = Column(Float, nullable=True)
    vencimiento4 = Column(Date, nullable=True)
    cuota4 = Column(Float, nullable=True)
    detraccion = Column(Boolean, nullable=True)
    retencion = Column(Boolean, nullable=True)


class RemisionRemitente(Base):
    __tablename__ = 'remision_remitente'
    cod_pedido = Column(String(8), primary_key=True)
    cuo = Column(String(35), primary_key=True)
    alias = Column(String(20), nullable=True)
    factura = Column(String(13), nullable=True)
    serie = Column(String(4), nullable=True)
    numero = Column(String(8), nullable=True)
    traslado = Column(Date, nullable=True)
    partida = Column(String(50), nullable=True)
    llegada = Column(String(50), nullable=True)
    placa = Column(String(8), nullable=True)
    conductor = Column(String(10), nullable=True)
    datos_adicionales = Column(String(35), nullable=True)
    estado = Column(String(20), nullable=True)
    observaciones = Column(String(50), nullable=True)


class Customers(Base):
    __tablename__ = 'customers'
    adquiriente_id = Column(BigInteger, primary_key=True, autoincrement=True)
    ruc = Column(BigInteger, nullable=True)
    alias = Column(String(35), nullable=True)
    related_user = Column(String(35), nullable=True)
    observaciones = Column(String(50), nullable=True)
    nombre_razon = Column(String(100), nullable=True)


class Proveedores(Base):
    __tablename__ = 'proveedores'
    proveedor_id = Column(BigInteger, primary_key=True, autoincrement=True)
    tipo_proveedor = Column(String(35), nullable=True)
    numero_documento = Column(BigInteger, nullable=True)
    nombre_razon = Column(String(50), nullable=True)
    estado = Column(String(20), nullable=True)
    related_partner = Column(String(35), nullable=True)
    observaciones = Column(String(50), nullable=True)
    actividad_economica = Column(String(100), nullable=True)
    act_econ_sec_1 = Column(String(100), nullable=True)
    act_econ_sec_2 = Column(String(100), nullable=True)
    usuario_sol = Column(String(20), nullable=True)
    clave_sol = Column(String(10), nullable=True)
    alias = Column(String(20), nullable=True)
"""
