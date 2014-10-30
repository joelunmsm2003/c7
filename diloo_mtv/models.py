# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Blaster010414(models.Model):
    id_registro = models.IntegerField(db_column='ID_Registro', blank=True, null=True) # Field name made lowercase.
    id_base = models.IntegerField(db_column='ID_Base', blank=True, null=True) # Field name made lowercase.
    id_proyecto = models.IntegerField(db_column='ID_Proyecto', blank=True, null=True) # Field name made lowercase.
    id_campana = models.IntegerField(db_column='ID_Campana', blank=True, null=True) # Field name made lowercase.
    id_gestion = models.IntegerField(db_column='ID_Gestion', blank=True, null=True) # Field name made lowercase.
    tsecuencia = models.IntegerField(db_column='tSecuencia', blank=True, null=True) # Field name made lowercase.
    tidcliente = models.IntegerField(db_column='tIdCliente', blank=True, null=True) # Field name made lowercase.
    tnrotarjeta = models.CharField(db_column='tNroTarjeta', max_length=45, blank=True) # Field name made lowercase.
    tnrocuenta = models.CharField(db_column='tNroCuenta', max_length=45, blank=True) # Field name made lowercase.
    tmarca = models.CharField(db_column='tMarca', max_length=25, blank=True) # Field name made lowercase.
    ttarjeta = models.CharField(db_column='tTarjeta', max_length=20, blank=True) # Field name made lowercase.
    tlinea = models.IntegerField(db_column='tLinea', blank=True, null=True) # Field name made lowercase.
    ttasa = models.FloatField(db_column='tTasa', blank=True, null=True) # Field name made lowercase.
    tplazo = models.IntegerField(db_column='tPlazo', blank=True, null=True) # Field name made lowercase.
    tproductoofrec = models.CharField(db_column='tProductoOfrec', max_length=45, blank=True) # Field name made lowercase.
    tnombre = models.CharField(db_column='tNombre', max_length=55, blank=True) # Field name made lowercase.
    tdni = models.IntegerField(db_column='tDni', blank=True, null=True) # Field name made lowercase.
    tdireccion = models.CharField(db_column='tDireccion', max_length=155, blank=True) # Field name made lowercase.
    tdistrito = models.CharField(db_column='tDistrito', max_length=65, blank=True) # Field name made lowercase.
    tprovincia = models.CharField(db_column='tProvincia', max_length=65, blank=True) # Field name made lowercase.
    tdepartamento = models.CharField(db_column='tDepartamento', max_length=65, blank=True) # Field name made lowercase.
    tresultado = models.IntegerField(db_column='tResultado', blank=True, null=True) # Field name made lowercase.
    tsubresultado = models.IntegerField(db_column='tSubresultado', blank=True, null=True) # Field name made lowercase.
    tssubresultado = models.IntegerField(db_column='tSsubresultado', blank=True, null=True) # Field name made lowercase.
    tusuario = models.CharField(db_column='tUsuario', max_length=15, blank=True) # Field name made lowercase.
    ffechagrabacion = models.DateTimeField(db_column='fFechaGrabacion', blank=True, null=True) # Field name made lowercase.
    lestado = models.CharField(db_column='lEstado', max_length=1, blank=True) # Field name made lowercase.
    tintentos = models.IntegerField(db_column='tIntentos', blank=True, null=True) # Field name made lowercase.
    contact_fono = models.IntegerField(db_column='Contact_Fono', blank=True, null=True) # Field name made lowercase.
    oc7_1 = models.IntegerField(db_column='OC7_1', blank=True, null=True) # Field name made lowercase.
    oc7_2 = models.IntegerField(db_column='OC7_2', blank=True, null=True) # Field name made lowercase.
    oc7_3 = models.CharField(db_column='OC7_3', max_length=10, blank=True) # Field name made lowercase.
    tduracion_ini = models.DateTimeField(db_column='tDuracion_ini', blank=True, null=True) # Field name made lowercase.
    tduracion_fin = models.DateTimeField(db_column='tDuracion_fin', blank=True, null=True) # Field name made lowercase.
    tduracion = models.IntegerField(db_column='tDuracion', blank=True, null=True) # Field name made lowercase.
    tregistro = models.CharField(db_column='tRegistro', max_length=45, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'blaster_010414'

class Blaster100414(models.Model):
    id_registro = models.IntegerField(db_column='ID_Registro', blank=True, null=True) # Field name made lowercase.
    id_base = models.IntegerField(db_column='ID_Base', blank=True, null=True) # Field name made lowercase.
    id_proyecto = models.IntegerField(db_column='ID_Proyecto', blank=True, null=True) # Field name made lowercase.
    id_campana = models.IntegerField(db_column='ID_Campana', blank=True, null=True) # Field name made lowercase.
    id_gestion = models.IntegerField(db_column='ID_Gestion', blank=True, null=True) # Field name made lowercase.
    tsecuencia = models.IntegerField(db_column='tSecuencia', blank=True, null=True) # Field name made lowercase.
    tidcliente = models.IntegerField(db_column='tIdCliente', blank=True, null=True) # Field name made lowercase.
    tnrotarjeta = models.CharField(db_column='tNroTarjeta', max_length=45, blank=True) # Field name made lowercase.
    tnrocuenta = models.CharField(db_column='tNroCuenta', max_length=45, blank=True) # Field name made lowercase.
    tmarca = models.CharField(db_column='tMarca', max_length=25, blank=True) # Field name made lowercase.
    ttarjeta = models.CharField(db_column='tTarjeta', max_length=20, blank=True) # Field name made lowercase.
    tlinea = models.IntegerField(db_column='tLinea', blank=True, null=True) # Field name made lowercase.
    ttasa = models.FloatField(db_column='tTasa', blank=True, null=True) # Field name made lowercase.
    tplazo = models.IntegerField(db_column='tPlazo', blank=True, null=True) # Field name made lowercase.
    tproductoofrec = models.CharField(db_column='tProductoOfrec', max_length=45, blank=True) # Field name made lowercase.
    tnombre = models.CharField(db_column='tNombre', max_length=55, blank=True) # Field name made lowercase.
    tdni = models.IntegerField(db_column='tDni', blank=True, null=True) # Field name made lowercase.
    tdireccion = models.CharField(db_column='tDireccion', max_length=155, blank=True) # Field name made lowercase.
    tdistrito = models.CharField(db_column='tDistrito', max_length=65, blank=True) # Field name made lowercase.
    tprovincia = models.CharField(db_column='tProvincia', max_length=65, blank=True) # Field name made lowercase.
    tdepartamento = models.CharField(db_column='tDepartamento', max_length=65, blank=True) # Field name made lowercase.
    tresultado = models.IntegerField(db_column='tResultado', blank=True, null=True) # Field name made lowercase.
    tsubresultado = models.IntegerField(db_column='tSubresultado', blank=True, null=True) # Field name made lowercase.
    tssubresultado = models.IntegerField(db_column='tSsubresultado', blank=True, null=True) # Field name made lowercase.
    tusuario = models.CharField(db_column='tUsuario', max_length=15, blank=True) # Field name made lowercase.
    ffechagrabacion = models.DateTimeField(db_column='fFechaGrabacion', blank=True, null=True) # Field name made lowercase.
    lestado = models.CharField(db_column='lEstado', max_length=1, blank=True) # Field name made lowercase.
    tintentos = models.IntegerField(db_column='tIntentos', blank=True, null=True) # Field name made lowercase.
    contact_fono = models.IntegerField(db_column='Contact_Fono', blank=True, null=True) # Field name made lowercase.
    oc7_1 = models.IntegerField(db_column='OC7_1', blank=True, null=True) # Field name made lowercase.
    oc7_2 = models.IntegerField(db_column='OC7_2', blank=True, null=True) # Field name made lowercase.
    oc7_3 = models.CharField(db_column='OC7_3', max_length=10, blank=True) # Field name made lowercase.
    tduracion_ini = models.DateTimeField(db_column='tDuracion_ini', blank=True, null=True) # Field name made lowercase.
    tduracion_fin = models.DateTimeField(db_column='tDuracion_fin', blank=True, null=True) # Field name made lowercase.
    tduracion = models.IntegerField(db_column='tDuracion', blank=True, null=True) # Field name made lowercase.
    tregistro = models.CharField(db_column='tRegistro', max_length=45, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'blaster_100414'

class Blaster270314(models.Model):
    id_registro = models.IntegerField(db_column='ID_Registro', blank=True, null=True) # Field name made lowercase.
    id_base = models.IntegerField(db_column='ID_Base', blank=True, null=True) # Field name made lowercase.
    id_proyecto = models.IntegerField(db_column='ID_Proyecto', blank=True, null=True) # Field name made lowercase.
    id_campana = models.IntegerField(db_column='ID_Campana', blank=True, null=True) # Field name made lowercase.
    id_gestion = models.IntegerField(db_column='ID_Gestion', blank=True, null=True) # Field name made lowercase.
    tsecuencia = models.IntegerField(db_column='tSecuencia', blank=True, null=True) # Field name made lowercase.
    tidcliente = models.IntegerField(db_column='tIdCliente', blank=True, null=True) # Field name made lowercase.
    tnrotarjeta = models.CharField(db_column='tNroTarjeta', max_length=45, blank=True) # Field name made lowercase.
    tnrocuenta = models.CharField(db_column='tNroCuenta', max_length=45, blank=True) # Field name made lowercase.
    tmarca = models.CharField(db_column='tMarca', max_length=25, blank=True) # Field name made lowercase.
    ttarjeta = models.CharField(db_column='tTarjeta', max_length=20, blank=True) # Field name made lowercase.
    tlinea = models.IntegerField(db_column='tLinea', blank=True, null=True) # Field name made lowercase.
    ttasa = models.FloatField(db_column='tTasa', blank=True, null=True) # Field name made lowercase.
    tplazo = models.IntegerField(db_column='tPlazo', blank=True, null=True) # Field name made lowercase.
    tproductoofrec = models.CharField(db_column='tProductoOfrec', max_length=45, blank=True) # Field name made lowercase.
    tnombre = models.CharField(db_column='tNombre', max_length=55, blank=True) # Field name made lowercase.
    tdni = models.IntegerField(db_column='tDni', blank=True, null=True) # Field name made lowercase.
    tdireccion = models.CharField(db_column='tDireccion', max_length=155, blank=True) # Field name made lowercase.
    tdistrito = models.CharField(db_column='tDistrito', max_length=65, blank=True) # Field name made lowercase.
    tprovincia = models.CharField(db_column='tProvincia', max_length=65, blank=True) # Field name made lowercase.
    tdepartamento = models.CharField(db_column='tDepartamento', max_length=65, blank=True) # Field name made lowercase.
    tresultado = models.IntegerField(db_column='tResultado', blank=True, null=True) # Field name made lowercase.
    tsubresultado = models.IntegerField(db_column='tSubresultado', blank=True, null=True) # Field name made lowercase.
    tssubresultado = models.IntegerField(db_column='tSsubresultado', blank=True, null=True) # Field name made lowercase.
    tusuario = models.CharField(db_column='tUsuario', max_length=15, blank=True) # Field name made lowercase.
    ffechagrabacion = models.DateTimeField(db_column='fFechaGrabacion', blank=True, null=True) # Field name made lowercase.
    lestado = models.CharField(db_column='lEstado', max_length=1, blank=True) # Field name made lowercase.
    tintentos = models.IntegerField(db_column='tIntentos', blank=True, null=True) # Field name made lowercase.
    contact_fono = models.IntegerField(db_column='Contact_Fono', blank=True, null=True) # Field name made lowercase.
    oc7_1 = models.IntegerField(db_column='OC7_1', blank=True, null=True) # Field name made lowercase.
    oc7_2 = models.IntegerField(db_column='OC7_2', blank=True, null=True) # Field name made lowercase.
    oc7_3 = models.CharField(db_column='OC7_3', max_length=10, blank=True) # Field name made lowercase.
    tduracion_ini = models.DateTimeField(db_column='tDuracion_ini', blank=True, null=True) # Field name made lowercase.
    tduracion_fin = models.DateTimeField(db_column='tDuracion_fin', blank=True, null=True) # Field name made lowercase.
    tduracion = models.IntegerField(db_column='tDuracion', blank=True, null=True) # Field name made lowercase.
    tregistro = models.CharField(db_column='tRegistro', max_length=45, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'blaster_270314'

class Chat(models.Model):
    id = models.IntegerField(primary_key=True)
    agente = models.IntegerField()
    supervisor = models.IntegerField()
    fecha = models.DateTimeField()
    cuerpo = models.CharField(max_length=1000)
    op = models.IntegerField()
    def __str__(self):
        return self.cuerpo
    class Meta:
        managed = False
        db_table = 'chat'

class Colas(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)
    id_ori_campana = models.IntegerField()
    tipo = models.IntegerField()
    did = models.IntegerField()
    acd = models.IntegerField()
    contestada = models.IntegerField()
    abandonada = models.IntegerField()
    estado = models.IntegerField()
    flag_mon = models.IntegerField()
    config = models.IntegerField()
    gestion = models.IntegerField()
    url = models.CharField(max_length=1000)
    parametros = models.CharField(max_length=300)
    popup = models.IntegerField()
    col_tel = models.IntegerField()
    base = models.IntegerField()
    precon = models.IntegerField()
    prencon = models.IntegerField()
    preerr = models.IntegerField()
    prepro = models.IntegerField()
    prepen = models.IntegerField()
    procon = models.IntegerField()
    proncon = models.IntegerField()
    proerr = models.IntegerField()
    propro = models.IntegerField()
    propen = models.IntegerField()
    def __str__(self):
        return self.nombre
    class Meta:
        managed = False
        db_table = 'colas'

class LogPhone(models.Model):
    id_log_phone = models.IntegerField(primary_key=True)
    id_ori_usuario = models.IntegerField(blank=True, null=True)
    id_ori_seg_cola = models.IntegerField(blank=True, null=True)
    id_ori_campana = models.IntegerField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    origen = models.CharField(max_length=30, blank=True)
    destino = models.CharField(max_length=30, blank=True)
    audio = models.CharField(max_length=100, blank=True)
    channel1 = models.CharField(max_length=50, blank=True)
    channel2 = models.CharField(max_length=50, blank=True)
    llam_estado = models.IntegerField(blank=True, null=True)
    age_nombre = models.CharField(max_length=50, blank=True)
    tie_ing = models.DateTimeField(blank=True, null=True)
    tie_acd = models.DateTimeField(blank=True, null=True)
    tie_tra = models.DateTimeField(blank=True, null=True)
    tie_con = models.DateTimeField(blank=True, null=True)
    tie_fin = models.DateTimeField(blank=True, null=True)
    tie_acw = models.DateTimeField(blank=True, null=True)
    flag = models.IntegerField(blank=True, null=True)
    uniqueid = models.CharField(max_length=30, blank=True)
    fin = models.IntegerField(blank=True, null=True)
    sql = models.IntegerField(blank=True, null=True)
    codhu = models.IntegerField(blank=True, null=True)
    bill = models.IntegerField(blank=True, null=True)
    asterisk = models.IntegerField(blank=True, null=True)
    valorllamada = models.CharField(max_length=200, blank=True)
    bk_id = models.IntegerField(blank=True, null=True)
    v_tring = models.IntegerField(blank=True, null=True)
    v_retry = models.IntegerField(blank=True, null=True)
    v_tipbusc = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    tregistro = models.CharField(max_length=11, blank=True)
    gestion_editid1 = models.CharField(max_length=20, blank=True)
    gestion_editid2 = models.CharField(max_length=20, blank=True)
    gestion_editid3 = models.CharField(max_length=20, blank=True)
    id_cliente = models.IntegerField(blank=True, null=True)
    coderr = models.IntegerField(db_column='codErr', blank=True, null=True) # Field name made lowercase.
    tipo_llamada = models.IntegerField()
    anexo = models.IntegerField()
    transferido = models.CharField(max_length=800)
    espera = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'log_phone'

class OriAcciones(models.Model):
    id = models.IntegerField(primary_key=True)
    accion = models.IntegerField()
    anx_sup = models.CharField(max_length=20)
    anx_age = models.CharField(max_length=20)
    canal = models.CharField(max_length=20)
    flag = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'ori_acciones'

class OriAcd(models.Model):
    id_ori_acd = models.IntegerField(primary_key=True)
    did_campana = models.CharField(db_column='DID_Campana', max_length=45) # Field name made lowercase.
    numero_llamado = models.CharField(db_column='Numero_Llamado', max_length=45) # Field name made lowercase.
    numero_entrante = models.CharField(db_column='Numero_Entrante', max_length=45) # Field name made lowercase.
    channel_entrante = models.CharField(db_column='Channel_Entrante', max_length=50) # Field name made lowercase.
    tiempo = models.CharField(db_column='Tiempo', max_length=15) # Field name made lowercase.
    flag = models.IntegerField()
    uniqueid = models.CharField(max_length=30)
    fin = models.IntegerField()
    age_nombre = models.CharField(max_length=100, blank=True)
    tie_ing = models.DateTimeField()
    tie_acd = models.DateTimeField()
    tie_tra = models.DateTimeField()
    tie_con = models.DateTimeField()
    tie_fin = models.DateTimeField()
    tie_acw = models.DateTimeField()
    id_ori_campana = models.IntegerField()
    sql = models.IntegerField()
    codhu = models.IntegerField(db_column='CodHU') # Field name made lowercase.
    bill = models.IntegerField()
    asterisk = models.IntegerField()
    audio = models.CharField(max_length=100)
    valorllamada = models.CharField(max_length=200)
    id_ori_usuario = models.IntegerField()
    llam_estado = models.IntegerField()
    anexo = models.IntegerField()
    duration = models.IntegerField()
    espera = models.IntegerField()
    def __str__(self):
        return self.uniqueid
    class Meta:
        managed = False
        db_table = 'ori_acd'

class OriAsignacion(models.Model):
    id_ori_asignacion = models.IntegerField(primary_key=True)
    id_ori_usuario = models.IntegerField()
    tipo_asig = models.IntegerField()
    id_ori_seg_cola = models.IntegerField()
    skill = models.IntegerField()
    in_orden = models.IntegerField()
    in_did = models.CharField(db_column='in_DID', max_length=20) # Field name made lowercase.
    db_orden = models.IntegerField(db_column='DB_orden') # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ori_asignacion'

class OriBlaster(models.Model):
    id_registro = models.IntegerField(db_column='ID_Registro', primary_key=True) # Field name made lowercase.
    id_base = models.IntegerField(db_column='ID_Base') # Field name made lowercase.
    id_proyecto = models.IntegerField(db_column='ID_Proyecto') # Field name made lowercase.
    id_campana = models.IntegerField(db_column='ID_Campana') # Field name made lowercase.
    id_gestion = models.IntegerField(db_column='ID_Gestion') # Field name made lowercase.
    tsecuencia = models.IntegerField(db_column='tSecuencia', blank=True, null=True) # Field name made lowercase.
    tidcliente = models.IntegerField(db_column='tIdCliente', blank=True, null=True) # Field name made lowercase.
    tnrotarjeta = models.CharField(db_column='tNroTarjeta', max_length=45, blank=True) # Field name made lowercase.
    tnrocuenta = models.CharField(db_column='tNroCuenta', max_length=45, blank=True) # Field name made lowercase.
    tmarca = models.CharField(db_column='tMarca', max_length=25, blank=True) # Field name made lowercase.
    ttarjeta = models.CharField(db_column='tTarjeta', max_length=20, blank=True) # Field name made lowercase.
    tlinea = models.IntegerField(db_column='tLinea', blank=True, null=True) # Field name made lowercase.
    ttasa = models.FloatField(db_column='tTasa', blank=True, null=True) # Field name made lowercase.
    tplazo = models.IntegerField(db_column='tPlazo', blank=True, null=True) # Field name made lowercase.
    tproductoofrec = models.CharField(db_column='tProductoOfrec', max_length=45, blank=True) # Field name made lowercase.
    tnombre = models.CharField(db_column='tNombre', max_length=55, blank=True) # Field name made lowercase.
    tdni = models.IntegerField(db_column='tDni', blank=True, null=True) # Field name made lowercase.
    tdireccion = models.CharField(db_column='tDireccion', max_length=155, blank=True) # Field name made lowercase.
    tdistrito = models.CharField(db_column='tDistrito', max_length=65, blank=True) # Field name made lowercase.
    tprovincia = models.CharField(db_column='tProvincia', max_length=65, blank=True) # Field name made lowercase.
    tdepartamento = models.CharField(db_column='tDepartamento', max_length=65, blank=True) # Field name made lowercase.
    tresultado = models.IntegerField(db_column='tResultado', blank=True, null=True) # Field name made lowercase.
    tsubresultado = models.IntegerField(db_column='tSubresultado', blank=True, null=True) # Field name made lowercase.
    tssubresultado = models.IntegerField(db_column='tSsubresultado', blank=True, null=True) # Field name made lowercase.
    tusuario = models.CharField(db_column='tUsuario', max_length=15, blank=True) # Field name made lowercase.
    ffechagrabacion = models.DateTimeField(db_column='fFechaGrabacion', blank=True, null=True) # Field name made lowercase.
    lestado = models.CharField(db_column='lEstado', max_length=1, blank=True) # Field name made lowercase.
    tintentos = models.IntegerField(db_column='tIntentos', blank=True, null=True) # Field name made lowercase.
    contact_fono = models.IntegerField(db_column='Contact_Fono', blank=True, null=True) # Field name made lowercase.
    oc7_1 = models.IntegerField(db_column='OC7_1', blank=True, null=True) # Field name made lowercase.
    oc7_2 = models.IntegerField(db_column='OC7_2') # Field name made lowercase.
    oc7_3 = models.CharField(db_column='OC7_3', max_length=10, blank=True) # Field name made lowercase.
    tduracion_ini = models.DateTimeField(db_column='tDuracion_ini', blank=True, null=True) # Field name made lowercase.
    tduracion_fin = models.DateTimeField(db_column='tDuracion_fin', blank=True, null=True) # Field name made lowercase.
    tduracion = models.IntegerField(db_column='tDuracion') # Field name made lowercase.
    tregistro = models.CharField(db_column='tRegistro', max_length=45, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ori_blaster'

class OriBlasterBk(models.Model):
    id_registro = models.IntegerField(db_column='ID_Registro', primary_key=True) # Field name made lowercase.
    id_base = models.IntegerField(db_column='ID_Base') # Field name made lowercase.
    id_proyecto = models.IntegerField(db_column='ID_Proyecto') # Field name made lowercase.
    id_campana = models.IntegerField(db_column='ID_Campana') # Field name made lowercase.
    id_gestion = models.IntegerField(db_column='ID_Gestion') # Field name made lowercase.
    tsecuencia = models.IntegerField(db_column='tSecuencia', blank=True, null=True) # Field name made lowercase.
    tidcliente = models.IntegerField(db_column='tIdCliente', blank=True, null=True) # Field name made lowercase.
    tnrotarjeta = models.CharField(db_column='tNroTarjeta', max_length=45, blank=True) # Field name made lowercase.
    tnrocuenta = models.CharField(db_column='tNroCuenta', max_length=45, blank=True) # Field name made lowercase.
    tmarca = models.CharField(db_column='tMarca', max_length=25, blank=True) # Field name made lowercase.
    ttarjeta = models.CharField(db_column='tTarjeta', max_length=20, blank=True) # Field name made lowercase.
    tlinea = models.IntegerField(db_column='tLinea', blank=True, null=True) # Field name made lowercase.
    ttasa = models.FloatField(db_column='tTasa', blank=True, null=True) # Field name made lowercase.
    tplazo = models.IntegerField(db_column='tPlazo', blank=True, null=True) # Field name made lowercase.
    tproductoofrec = models.CharField(db_column='tProductoOfrec', max_length=45, blank=True) # Field name made lowercase.
    tnombre = models.CharField(db_column='tNombre', max_length=55, blank=True) # Field name made lowercase.
    tdni = models.IntegerField(db_column='tDni', blank=True, null=True) # Field name made lowercase.
    tdireccion = models.CharField(db_column='tDireccion', max_length=155, blank=True) # Field name made lowercase.
    tdistrito = models.CharField(db_column='tDistrito', max_length=65, blank=True) # Field name made lowercase.
    tprovincia = models.CharField(db_column='tProvincia', max_length=65, blank=True) # Field name made lowercase.
    tdepartamento = models.CharField(db_column='tDepartamento', max_length=65, blank=True) # Field name made lowercase.
    tresultado = models.IntegerField(db_column='tResultado', blank=True, null=True) # Field name made lowercase.
    tsubresultado = models.IntegerField(db_column='tSubresultado', blank=True, null=True) # Field name made lowercase.
    tssubresultado = models.IntegerField(db_column='tSsubresultado', blank=True, null=True) # Field name made lowercase.
    tusuario = models.CharField(db_column='tUsuario', max_length=15, blank=True) # Field name made lowercase.
    ffechagrabacion = models.DateTimeField(db_column='fFechaGrabacion', blank=True, null=True) # Field name made lowercase.
    lestado = models.CharField(db_column='lEstado', max_length=1, blank=True) # Field name made lowercase.
    tintentos = models.IntegerField(db_column='tIntentos', blank=True, null=True) # Field name made lowercase.
    contact_fono = models.IntegerField(db_column='Contact_Fono', blank=True, null=True) # Field name made lowercase.
    oc7_1 = models.IntegerField(db_column='OC7_1', blank=True, null=True) # Field name made lowercase.
    oc7_2 = models.IntegerField(db_column='OC7_2') # Field name made lowercase.
    oc7_3 = models.CharField(db_column='OC7_3', max_length=10, blank=True) # Field name made lowercase.
    tduracion_ini = models.DateTimeField(db_column='tDuracion_ini', blank=True, null=True) # Field name made lowercase.
    tduracion_fin = models.DateTimeField(db_column='tDuracion_fin', blank=True, null=True) # Field name made lowercase.
    tduracion = models.IntegerField(db_column='tDuracion') # Field name made lowercase.
    tregistro = models.CharField(db_column='tRegistro', max_length=45, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'ori_blaster_bk'

class OriCampana(models.Model):
    id_ori_campana = models.IntegerField(primary_key=True)
    campana_nombre = models.CharField(max_length=80)
    campana_tipo = models.IntegerField()
    campana_tipo_detalle = models.IntegerField()
    campana_estado = models.IntegerField()
    campana_gestion = models.CharField(max_length=100)
    agregistrados = models.IntegerField(db_column='AgRegistrados') # Field name made lowercase.
    agocupados = models.IntegerField(db_column='AgOcupados') # Field name made lowercase.
    agdetenidos = models.IntegerField(db_column='AgDetenidos') # Field name made lowercase.
    agpausados = models.IntegerField(db_column='AgPausados') # Field name made lowercase.
    campana_canales = models.IntegerField()
    ver = models.IntegerField()
    bd_rellamada = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'ori_campana'

class OriChat(models.Model):
    id_ori_chat = models.IntegerField(primary_key=True)
    chat_fhora = models.DateTimeField()
    id_ori_usuario = models.IntegerField()
    nombre_usuario = models.CharField(max_length=50)
    id_ori_super = models.IntegerField()
    nombre_super = models.CharField(max_length=50)
    chat_mensaje = models.CharField(max_length=200)
    flag = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'ori_chat'

class OriEstados(models.Model):
    id_ori_estados = models.IntegerField(primary_key=True)
    cod_estado = models.IntegerField()
    txt_estado = models.CharField(max_length=15)
    id_ori_usuario = models.IntegerField()
    f_inicio = models.DateTimeField()
    f_fin = models.DateTimeField()
    flag = models.IntegerField()
    duracion = models.IntegerField(db_column='Duracion') # Field name made lowercase.
    id_ori_campana = models.IntegerField()
    age_ip = models.CharField(max_length=20)
    id_ori_seg_cola = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'ori_estados'

class OriEstados190314(models.Model):
    id_ori_estados = models.IntegerField(primary_key=True)
    cod_estado = models.IntegerField()
    txt_estado = models.CharField(max_length=15)
    id_ori_usuario = models.IntegerField()
    f_inicio = models.DateTimeField()
    f_fin = models.DateTimeField()
    flag = models.IntegerField()
    duracion = models.IntegerField(db_column='Duracion') # Field name made lowercase.
    id_ori_campana = models.IntegerField()
    age_ip = models.CharField(max_length=20)
    id_ori_seg_cola = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'ori_estados_190314'

class OriLlamadas(models.Model):
    id_ori_llamadas = models.IntegerField()
    age_ip = models.CharField(max_length=20, blank=True)
    age_codigo = models.CharField(max_length=10, blank=True)
    cam_codigo = models.IntegerField(blank=True, null=True)
    llam_numero = models.CharField(max_length=20, blank=True)
    llam_estado = models.IntegerField(blank=True, null=True)
    llam_flag = models.IntegerField(blank=True, null=True)
    llam_uniqueid = models.CharField(max_length=45, blank=True)
    tipo = models.IntegerField(blank=True, null=True)
    f_origen = models.DateTimeField()
    canal1 = models.CharField(max_length=50, blank=True)
    canal2 = models.CharField(max_length=50, blank=True)
    flagfin = models.IntegerField(db_column='flagFIN', blank=True, null=True) # Field name made lowercase.
    v_tring = models.IntegerField(blank=True, null=True)
    v_retry = models.IntegerField(blank=True, null=True)
    v_tipbusc = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    bill = models.IntegerField(blank=True, null=True)
    tregistro = models.IntegerField()
    gestion_editid1 = models.CharField(max_length=20, blank=True)
    gestion_editid2 = models.CharField(max_length=20, blank=True)
    gestion_editid3 = models.CharField(max_length=20, blank=True)
    f_llam_fin = models.DateTimeField()
    f_llam_discador = models.DateTimeField()
    f_llam_resuelve = models.DateTimeField()
    id_ori_campana = models.IntegerField()
    f_fingestion = models.DateTimeField()
    id_cliente = models.IntegerField(db_column='ID_Cliente') # Field name made lowercase.
    coderr = models.IntegerField(db_column='CodErr') # Field name made lowercase.
    audio = models.CharField(max_length=200)
    sql = models.IntegerField()
    gestion_editid4 = models.CharField(max_length=100)
    gestion_editid5 = models.CharField(max_length=100)
    gestion_editid6 = models.CharField(max_length=100)
    gestion_editid7 = models.CharField(max_length=100)
    gestion_editid8 = models.CharField(max_length=100)
    gestion_editid9 = models.CharField(max_length=100)
    gestion_editid10 = models.CharField(max_length=100)
    gestion_editid11 = models.CharField(max_length=100)
    id_ori_seg_cola = models.IntegerField()
    age_nombre = models.CharField(max_length=100)
    anexo = models.IntegerField()
    espera = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'ori_llamadas'

class OriLlamadas070213(models.Model):
    id_ori_llamadas = models.IntegerField()
    age_ip = models.CharField(max_length=20, blank=True)
    age_codigo = models.CharField(max_length=10, blank=True)
    cam_codigo = models.IntegerField(blank=True, null=True)
    llam_numero = models.CharField(max_length=20, blank=True)
    llam_estado = models.IntegerField(blank=True, null=True)
    llam_flag = models.IntegerField(blank=True, null=True)
    llam_uniqueid = models.CharField(max_length=45, blank=True)
    tipo = models.IntegerField(blank=True, null=True)
    f_origen = models.DateTimeField()
    canal1 = models.CharField(max_length=50, blank=True)
    canal2 = models.CharField(max_length=50, blank=True)
    flagfin = models.IntegerField(db_column='flagFIN', blank=True, null=True) # Field name made lowercase.
    v_tring = models.IntegerField(blank=True, null=True)
    v_retry = models.IntegerField(blank=True, null=True)
    v_tipbusc = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    bill = models.IntegerField(blank=True, null=True)
    tregistro = models.IntegerField()
    gestion_editid1 = models.CharField(max_length=20, blank=True)
    gestion_editid2 = models.CharField(max_length=20, blank=True)
    gestion_editid3 = models.CharField(max_length=20, blank=True)
    f_llam_fin = models.DateTimeField()
    f_llam_discador = models.DateTimeField()
    f_llam_resuelve = models.DateTimeField()
    id_ori_campana = models.IntegerField()
    f_fingestion = models.DateTimeField()
    id_cliente = models.IntegerField(db_column='ID_Cliente') # Field name made lowercase.
    coderr = models.IntegerField(db_column='CodErr') # Field name made lowercase.
    audio = models.CharField(max_length=200)
    sql = models.IntegerField()
    gestion_editid4 = models.CharField(max_length=100)
    gestion_editid5 = models.CharField(max_length=100)
    gestion_editid6 = models.CharField(max_length=100)
    gestion_editid7 = models.CharField(max_length=100)
    gestion_editid8 = models.CharField(max_length=100)
    gestion_editid9 = models.CharField(max_length=100)
    gestion_editid10 = models.CharField(max_length=100)
    gestion_editid11 = models.CharField(max_length=100)
    id_ori_seg_cola = models.IntegerField()
    age_nombre = models.CharField(max_length=100)
    anexo = models.IntegerField()
    espera = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'ori_llamadas_070213'

class OriLlamadas110712(models.Model):
    id_ori_llamadas = models.IntegerField()
    age_ip = models.CharField(max_length=20, blank=True)
    age_codigo = models.CharField(max_length=10, blank=True)
    cam_codigo = models.IntegerField(blank=True, null=True)
    llam_numero = models.CharField(max_length=20, blank=True)
    llam_estado = models.IntegerField(blank=True, null=True)
    llam_flag = models.IntegerField(blank=True, null=True)
    llam_uniqueid = models.CharField(max_length=45, blank=True)
    tipo = models.IntegerField(blank=True, null=True)
    f_origen = models.DateTimeField()
    canal1 = models.CharField(max_length=50, blank=True)
    canal2 = models.CharField(max_length=50, blank=True)
    flagfin = models.IntegerField(db_column='flagFIN', blank=True, null=True) # Field name made lowercase.
    v_tring = models.IntegerField(blank=True, null=True)
    v_retry = models.IntegerField(blank=True, null=True)
    v_tipbusc = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    bill = models.IntegerField(blank=True, null=True)
    tregistro = models.IntegerField()
    gestion_editid1 = models.CharField(max_length=20, blank=True)
    gestion_editid2 = models.CharField(max_length=20, blank=True)
    gestion_editid3 = models.CharField(max_length=20, blank=True)
    f_llam_fin = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'ori_llamadas_110712'

class OriLlamadas190314(models.Model):
    id_ori_llamadas = models.IntegerField()
    age_ip = models.CharField(max_length=20, blank=True)
    age_codigo = models.CharField(max_length=10, blank=True)
    cam_codigo = models.IntegerField(blank=True, null=True)
    llam_numero = models.CharField(max_length=20, blank=True)
    llam_estado = models.IntegerField(blank=True, null=True)
    llam_flag = models.IntegerField(blank=True, null=True)
    llam_uniqueid = models.CharField(max_length=45, blank=True)
    tipo = models.IntegerField(blank=True, null=True)
    f_origen = models.DateTimeField()
    canal1 = models.CharField(max_length=50, blank=True)
    canal2 = models.CharField(max_length=50, blank=True)
    flagfin = models.IntegerField(db_column='flagFIN', blank=True, null=True) # Field name made lowercase.
    v_tring = models.IntegerField(blank=True, null=True)
    v_retry = models.IntegerField(blank=True, null=True)
    v_tipbusc = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    bill = models.IntegerField(blank=True, null=True)
    tregistro = models.IntegerField()
    gestion_editid1 = models.CharField(max_length=20, blank=True)
    gestion_editid2 = models.CharField(max_length=20, blank=True)
    gestion_editid3 = models.CharField(max_length=20, blank=True)
    f_llam_fin = models.DateTimeField()
    f_llam_discador = models.DateTimeField()
    f_llam_resuelve = models.DateTimeField()
    id_ori_campana = models.IntegerField()
    f_fingestion = models.DateTimeField()
    id_cliente = models.IntegerField(db_column='ID_Cliente') # Field name made lowercase.
    coderr = models.IntegerField(db_column='CodErr') # Field name made lowercase.
    audio = models.CharField(max_length=200)
    sql = models.IntegerField()
    gestion_editid4 = models.CharField(max_length=100)
    gestion_editid5 = models.CharField(max_length=100)
    gestion_editid6 = models.CharField(max_length=100)
    gestion_editid7 = models.CharField(max_length=100)
    gestion_editid8 = models.CharField(max_length=100)
    gestion_editid9 = models.CharField(max_length=100)
    gestion_editid10 = models.CharField(max_length=100)
    gestion_editid11 = models.CharField(max_length=100)
    id_ori_seg_cola = models.IntegerField()
    age_nombre = models.CharField(max_length=100)
    anexo = models.IntegerField()
    espera = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'ori_llamadas_190314'

class OriLlamadas240313(models.Model):
    id_ori_llamadas = models.IntegerField()
    age_ip = models.CharField(max_length=20, blank=True)
    age_codigo = models.CharField(max_length=10, blank=True)
    cam_codigo = models.IntegerField(blank=True, null=True)
    llam_numero = models.CharField(max_length=20, blank=True)
    llam_estado = models.IntegerField(blank=True, null=True)
    llam_flag = models.IntegerField(blank=True, null=True)
    llam_uniqueid = models.CharField(max_length=45, blank=True)
    tipo = models.IntegerField(blank=True, null=True)
    f_origen = models.DateTimeField()
    canal1 = models.CharField(max_length=50, blank=True)
    canal2 = models.CharField(max_length=50, blank=True)
    flagfin = models.IntegerField(db_column='flagFIN', blank=True, null=True) # Field name made lowercase.
    v_tring = models.IntegerField(blank=True, null=True)
    v_retry = models.IntegerField(blank=True, null=True)
    v_tipbusc = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    bill = models.IntegerField(blank=True, null=True)
    tregistro = models.IntegerField()
    gestion_editid1 = models.CharField(max_length=20, blank=True)
    gestion_editid2 = models.CharField(max_length=20, blank=True)
    gestion_editid3 = models.CharField(max_length=20, blank=True)
    f_llam_fin = models.DateTimeField()
    f_llam_discador = models.DateTimeField()
    f_llam_resuelve = models.DateTimeField()
    id_ori_campana = models.IntegerField()
    f_fingestion = models.DateTimeField()
    id_cliente = models.IntegerField(db_column='ID_Cliente') # Field name made lowercase.
    coderr = models.IntegerField(db_column='CodErr') # Field name made lowercase.
    audio = models.CharField(max_length=200)
    sql = models.IntegerField()
    gestion_editid4 = models.CharField(max_length=100)
    gestion_editid5 = models.CharField(max_length=100)
    gestion_editid6 = models.CharField(max_length=100)
    gestion_editid7 = models.CharField(max_length=100)
    gestion_editid8 = models.CharField(max_length=100)
    gestion_editid9 = models.CharField(max_length=100)
    gestion_editid10 = models.CharField(max_length=100)
    gestion_editid11 = models.CharField(max_length=100)
    id_ori_seg_cola = models.IntegerField()
    age_nombre = models.CharField(max_length=100)
    anexo = models.IntegerField()
    espera = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'ori_llamadas_240313'

class OriLlamadas240714(models.Model):
    id_ori_llamadas = models.IntegerField()
    age_ip = models.CharField(max_length=20, blank=True)
    age_codigo = models.CharField(max_length=10, blank=True)
    cam_codigo = models.IntegerField(blank=True, null=True)
    llam_numero = models.CharField(max_length=20, blank=True)
    llam_estado = models.IntegerField(blank=True, null=True)
    llam_flag = models.IntegerField(blank=True, null=True)
    llam_uniqueid = models.CharField(max_length=45, blank=True)
    tipo = models.IntegerField(blank=True, null=True)
    f_origen = models.DateTimeField()
    canal1 = models.CharField(max_length=50, blank=True)
    canal2 = models.CharField(max_length=50, blank=True)
    flagfin = models.IntegerField(db_column='flagFIN', blank=True, null=True) # Field name made lowercase.
    v_tring = models.IntegerField(blank=True, null=True)
    v_retry = models.IntegerField(blank=True, null=True)
    v_tipbusc = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    bill = models.IntegerField(blank=True, null=True)
    tregistro = models.IntegerField()
    gestion_editid1 = models.CharField(max_length=20, blank=True)
    gestion_editid2 = models.CharField(max_length=20, blank=True)
    gestion_editid3 = models.CharField(max_length=20, blank=True)
    f_llam_fin = models.DateTimeField()
    f_llam_discador = models.DateTimeField()
    f_llam_resuelve = models.DateTimeField()
    id_ori_campana = models.IntegerField()
    f_fingestion = models.DateTimeField()
    id_cliente = models.IntegerField(db_column='ID_Cliente') # Field name made lowercase.
    coderr = models.IntegerField(db_column='CodErr') # Field name made lowercase.
    audio = models.CharField(max_length=200)
    sql = models.IntegerField()
    gestion_editid4 = models.CharField(max_length=100)
    gestion_editid5 = models.CharField(max_length=100)
    gestion_editid6 = models.CharField(max_length=100)
    gestion_editid7 = models.CharField(max_length=100)
    gestion_editid8 = models.CharField(max_length=100)
    gestion_editid9 = models.CharField(max_length=100)
    gestion_editid10 = models.CharField(max_length=100)
    gestion_editid11 = models.CharField(max_length=100)
    id_ori_seg_cola = models.IntegerField()
    age_nombre = models.CharField(max_length=100)
    anexo = models.IntegerField()
    espera = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'ori_llamadas_240714'

class OriLlamadas250811(models.Model):
    id_ori_llamadas = models.IntegerField()
    age_ip = models.CharField(max_length=20, blank=True)
    age_codigo = models.CharField(max_length=10, blank=True)
    cam_codigo = models.IntegerField(blank=True, null=True)
    llam_numero = models.CharField(max_length=20, blank=True)
    llam_estado = models.IntegerField(blank=True, null=True)
    llam_flag = models.IntegerField(blank=True, null=True)
    llam_uniqueid = models.CharField(max_length=45, blank=True)
    tipo = models.IntegerField(blank=True, null=True)
    f_origen = models.DateTimeField()
    canal1 = models.CharField(max_length=50, blank=True)
    canal2 = models.CharField(max_length=50, blank=True)
    flagfin = models.IntegerField(db_column='flagFIN', blank=True, null=True) # Field name made lowercase.
    v_tring = models.IntegerField(blank=True, null=True)
    v_retry = models.IntegerField(blank=True, null=True)
    v_tipbusc = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    bill = models.IntegerField(blank=True, null=True)
    tregistro = models.IntegerField()
    gestion_editid1 = models.CharField(max_length=20, blank=True)
    gestion_editid2 = models.CharField(max_length=20, blank=True)
    gestion_editid3 = models.CharField(max_length=20, blank=True)
    class Meta:
        managed = False
        db_table = 'ori_llamadas_250811'

class OriLlamadas261013(models.Model):
    id_ori_llamadas = models.IntegerField()
    age_ip = models.CharField(max_length=20, blank=True)
    age_codigo = models.CharField(max_length=10, blank=True)
    cam_codigo = models.IntegerField(blank=True, null=True)
    llam_numero = models.CharField(max_length=20, blank=True)
    llam_estado = models.IntegerField(blank=True, null=True)
    llam_flag = models.IntegerField(blank=True, null=True)
    llam_uniqueid = models.CharField(max_length=45, blank=True)
    tipo = models.IntegerField(blank=True, null=True)
    f_origen = models.DateTimeField()
    canal1 = models.CharField(max_length=50, blank=True)
    canal2 = models.CharField(max_length=50, blank=True)
    flagfin = models.IntegerField(db_column='flagFIN', blank=True, null=True) # Field name made lowercase.
    v_tring = models.IntegerField(blank=True, null=True)
    v_retry = models.IntegerField(blank=True, null=True)
    v_tipbusc = models.IntegerField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    bill = models.IntegerField(blank=True, null=True)
    tregistro = models.IntegerField()
    gestion_editid1 = models.CharField(max_length=20, blank=True)
    gestion_editid2 = models.CharField(max_length=20, blank=True)
    gestion_editid3 = models.CharField(max_length=20, blank=True)
    f_llam_fin = models.DateTimeField()
    f_llam_discador = models.DateTimeField()
    f_llam_resuelve = models.DateTimeField()
    id_ori_campana = models.IntegerField()
    f_fingestion = models.DateTimeField()
    id_cliente = models.IntegerField(db_column='ID_Cliente') # Field name made lowercase.
    coderr = models.IntegerField(db_column='CodErr') # Field name made lowercase.
    audio = models.CharField(max_length=200)
    sql = models.IntegerField()
    gestion_editid4 = models.CharField(max_length=100)
    gestion_editid5 = models.CharField(max_length=100)
    gestion_editid6 = models.CharField(max_length=100)
    gestion_editid7 = models.CharField(max_length=100)
    gestion_editid8 = models.CharField(max_length=100)
    gestion_editid9 = models.CharField(max_length=100)
    gestion_editid10 = models.CharField(max_length=100)
    gestion_editid11 = models.CharField(max_length=100)
    id_ori_seg_cola = models.IntegerField()
    age_nombre = models.CharField(max_length=100)
    anexo = models.IntegerField()
    espera = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ori_llamadas_261013'

class OriLog01(models.Model):
    id_ori_log = models.IntegerField(primary_key=True)
    fechahora = models.DateTimeField()
    estado = models.IntegerField()
    id_ori_usuario = models.IntegerField()
    flag = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'ori_log01'

class OriMonitoreo(models.Model):
    id_ori_monitoreo = models.IntegerField(unique=True)
    age_nombre = models.CharField(max_length=255)
    age_ip = models.CharField(max_length=15, blank=True)
    age_campana = models.CharField(max_length=255, blank=True)
    age_anexo = models.CharField(max_length=5, blank=True)
    age_estado = models.IntegerField()
    tie_estado = models.CharField(max_length=30, blank=True)
    age_intera = models.IntegerField()
    tie_intera = models.CharField(max_length=30, blank=True)
    cha_intera = models.CharField(max_length=30, blank=True)
    num_destino = models.CharField(max_length=20, blank=True)
    id_ori_usuario = models.IntegerField()
    age_gestion = models.IntegerField()
    tie_gestion = models.CharField(max_length=30, blank=True)
    age_sup = models.CharField(max_length=9, blank=True)
    cantidad = models.IntegerField()
    cantidad1 = models.IntegerField()
    id_ori_campana = models.CharField(max_length=3, blank=True)
    est_ag_progresivo = models.IntegerField(blank=True, null=True)
    tot_llam_prog = models.IntegerField()
    est_ag_predictivo = models.IntegerField(blank=True, null=True)
    flag_mon = models.IntegerField()
    campana_estado = models.IntegerField()
    in_orden = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'ori_monitoreo'

class OriUsuario(models.Model):
    id_ori_usuario = models.IntegerField(primary_key=True)
    usuario_logeo = models.CharField(max_length=20)
    usuario_nombre = models.CharField(max_length=80)
    usuario_clave = models.CharField(max_length=60)
    usuario_tipo = models.CharField(max_length=60)
    id_ori_campana = models.IntegerField()
    usuario_ip = models.CharField(max_length=20)
    usuario_estado = models.IntegerField()
    usuario_gestion = models.IntegerField()
    usuario_destino = models.CharField(max_length=20)
    usuario_canal = models.CharField(max_length=50)
    usuario_anexo = models.CharField(max_length=5)
    usuario_duracion = models.DateTimeField()
    gestion_editid1 = models.CharField(max_length=20)
    gestion_editid2 = models.CharField(max_length=20)
    gestion_editid3 = models.CharField(max_length=20)
    gestion_editid4 = models.CharField(max_length=100)
    gestion_editid5 = models.CharField(max_length=20)
    gestion_editid6 = models.CharField(max_length=20)
    gestion_editid7 = models.CharField(max_length=20)
    gestion_editid8 = models.CharField(max_length=20)
    gestion_editid9 = models.CharField(max_length=20)
    gestion_editid10 = models.CharField(max_length=20)
    incall_cant = models.IntegerField()
    incall_dur = models.IntegerField()
    outcall_cant = models.IntegerField()
    outcall_dur = models.IntegerField()
    in_did = models.CharField(db_column='in_DID', max_length=20) # Field name made lowercase.
    audio = models.CharField(max_length=200)
    cod_int = models.CharField(max_length=11)
    gestion_editid11 = models.CharField(max_length=20)
    usuario_telefonia = models.IntegerField()
    flag_mon = models.IntegerField()
    bill = models.IntegerField()
    id_ori_llamadas = models.IntegerField()
    acd = models.IntegerField()
    abandonada_in = models.IntegerField()
    abandonada_out = models.IntegerField()
    age_base = models.IntegerField()
    age_procesadas = models.IntegerField()
    age_pendientes = models.IntegerField()
    checa = models.IntegerField()
    tproyecto = models.CharField(db_column='tProyecto', max_length=20) # Field name made lowercase.
    tbase = models.CharField(db_column='tBase', max_length=20) # Field name made lowercase.
    est_ag_predictivo = models.IntegerField()
    contesta = models.IntegerField()
    no_contesta = models.IntegerField()
    colas = models.CharField(max_length=300)
    segmentos = models.CharField(max_length=300)
    skill = models.CharField(max_length=300)
    idusuario_servicio = models.IntegerField()
    kalive01 = models.IntegerField()
    kalive02 = models.IntegerField()
    en_pausa = models.TimeField()
    en_llamada = models.TimeField()
    libre = models.TimeField()
    acw = models.TimeField()
    en_pausa_cnt = models.IntegerField()
    en_llamada_cnt = models.IntegerField()
    libre_cnt = models.IntegerField()
    acw_cnt = models.IntegerField()
    tipo_disc = models.CharField(max_length=10)
    cose_tipo = models.IntegerField()
    cose_id = models.IntegerField()
    cose_valor = models.CharField(max_length=80)
    mod1 = models.IntegerField()
    mod2 = models.IntegerField()
    mod3 = models.IntegerField()
    mod4 = models.IntegerField()
    mod5 = models.IntegerField()
    mod6 = models.IntegerField()
    lis_camp = models.CharField(max_length=300)
    lis_rep = models.CharField(max_length=200)
    mod7 = models.IntegerField()
    mod8 = models.IntegerField()
    mod9 = models.IntegerField()
    mod10 = models.IntegerField()
    mod11 = models.IntegerField()
    mod12 = models.IntegerField()
    usuario_password = models.CharField(max_length=10)
    filtro_campag = models.IntegerField()
    id_chat = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'ori_usuario'

class OriVestados(models.Model):
    id_ori_vestados = models.IntegerField(primary_key=True)
    txt_estados = models.CharField(max_length=30)
    flag = models.IntegerField()
    c_letra = models.CharField(max_length=15)
    c_fondo = models.CharField(max_length=15)
    class Meta:
        managed = False
        db_table = 'ori_vestados'

class Reportes(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo = models.IntegerField()
    nombre = models.CharField(max_length=200)
    campos = models.CharField(max_length=500)
    tamano = models.CharField(max_length=500)
    ssql = models.CharField(max_length=3000)
    pie_sql = models.CharField(max_length=3000)
    filtro = models.CharField(db_column='FILTRO', max_length=500) # Field name made lowercase.
    disa = models.CharField(max_length=200)
    grup_sql = models.CharField(max_length=500)
    ord_sql = models.CharField(max_length=500)
    where_sql = models.CharField(max_length=1000)
    f_sup = models.IntegerField()
    f_camp = models.IntegerField()
    f_fecha = models.IntegerField()
    f_hora = models.IntegerField()
    f_agent = models.IntegerField()
    ip_server = models.CharField(max_length=100)
    base_datos = models.CharField(max_length=100)
    user_datos = models.CharField(max_length=100)
    passw_datos = models.CharField(max_length=100)
    clase = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'reportes'

class TipoRep(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'tipo_rep'

