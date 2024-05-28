<<<<<<< HEAD
from django.db import models


# Aquí se crean los modelos de la aplicación.
# Un modelo en Django es una clase que define la estructura de una tabla en la base de datos.






# Inicio del modelo Area

class Area(models.Model):

    id_area = models.AutoField(primary_key=True)
    nombre_area = models.CharField(max_length=100)
    descripcion_area = models.CharField(max_length=255, null=True, blank=True)
=======
from hashlib import blake2b
from operator import truediv
from platform import mac_ver
from pyexpat import model
from sys import maxsize
from tkinter import CASCADE
from django.db import models
from urllib3 import ProxyManager

# Create your models here.


class Programmer(models.Model):
    fullname = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)


# ============================================================


class Cuota(models.Model):
    id_cuota = models.AutoField(primary_key=True)
    numero_cuotas = models.CharField(max_length=50)
    fecha_vencimiento = models.CharField(max_length=50)
    deuda_total = models.FloatField()
    amortizacion = models.FloatField()

    def __str__(self):
        return self.id_cuota


# ============================================================


class Permiso(models.Model):
    id_permiso = models.AutoField(primary_key=True)
    nombre_permiso = models.CharField(max_length=50)
    descripcion_permiso = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombre_permiso


class Area(models.Model):
    id_area = models.AutoField(primary_key=True)
    nombre_area = models.CharField(max_length=100)
    descripcion_area = models.CharField(max_length=255, null=True, blank=True)
    permisos = models.ManyToManyField(Permiso, through='PermisoArea', related_name='areas')
>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9

    def __str__(self):
        return self.nombre_area


<<<<<<< HEAD
# Fin del modelo Area
# ===========================================


# Inicio del modelo Origen

class Origen (models.Model):
    id_origen = models.AutoField(primary_key=True)
    nombre_origen = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_origen

# Fin del modelo Origen
# ===========================================


# Inicio del modelo Canal

class Canal (models.Model):
    id_canal = models.AutoField(primary_key=True)
    tipo_canal = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo_canal


# Fin del modelo Canal
# ===========================================


# Inicio del modelo Medio
=======
class PermisoArea(models.Model):
    id_permiso = models.ForeignKey(Permiso, on_delete=models.CASCADE, null=True, blank=True)
    id_area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Permiso {self.id_permiso} - Area {self.id_area}"

# ============================================================


class Observaciones(models.Model):
    id_observaciones = models.AutoField(primary_key=True)
    descripcion_observaciones = models.CharField(max_length=255)
    adjuntar_informacion = models.CharField(max_length=255)

    def __str__(self):
        return self.id_observaciones


# ============================================================
>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9

class Medio (models.Model):
    id_medio = models.AutoField(primary_key=True)
    nombre_medio = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_medio

<<<<<<< HEAD
# Fin del modelo Medio
# ===========================================


# Inicio del modelo Rol
=======

class Canal (models.Model):
    id_canal = models.AutoField(primary_key=True)
    tipo_canal = models.CharField(max_length=100)
    id_medio = models.ForeignKey(Medio, on_delete=models.CASCADE)


class Origen (models.Model):
    id_origen = models.AutoField(primary_key=True)
    nombre_origen = models.CharField(max_length=100)
    id_canal = models.ForeignKey(Canal, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_origen
>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9


class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_rol


<<<<<<< HEAD
# Fin del modelo Rol
# ===========================================



# Inicio del modelo Estado

class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre_estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_estado

# Fin del modelo Estado
# ===========================================














# Inicio del modelo Proyecto
=======
# ============================================================
>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9

class Proyecto(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    nombre_proyecto = models.CharField(max_length=100)
<<<<<<< HEAD
    fecha_inicio = models.CharField(max_length=50, null=True, blank=True)
    fecha_fin = models.CharField(max_length=50, null=True, blank=True)

=======
    fecha_inicio = models.CharField(max_length=50)
    fecha_fin = models.CharField(max_length=50)
>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9

    def __str__(self):
        return self.nombre_proyecto

<<<<<<< HEAD
# Fin del modelo Proyecto
# ===========================================



# Inicio del modelo Manzana


class Manzana(models.Model):
    id_manzana = models.AutoField(primary_key=True)
    nombre_manzana = models.CharField(max_length=10)
    id_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=True, blank=True)

    
    def __str__(self):
        return f"Manzana {self.nombre_manzana} - Proyecto {self.id_proyecto}" 

# Fin del modelo Manzana
# ===========================================


# Inicio del modelo Lote

class Lote(models.Model):
    id_lote = models.AutoField(primary_key=True)
    numero_lote = models.CharField(max_length=50, null=True, blank=True)
    area = models.FloatField(null=True, blank=True)
    perimetro = models.CharField(max_length=50, null=True, blank=True)
    colindancia_frente = models.CharField(max_length=50, null=True, blank=True)
    colindancia_derecha = models.CharField(max_length=50, null=True, blank=True)
    colindancia_izquierda = models.CharField(max_length=50, null=True, blank=True)
    colindancia_fondo = models.CharField(max_length=50, null=True, blank=True)
    distancia_frente = models.CharField(max_length=50, null=True, blank=True)
    distancia_derecha = models.CharField(max_length=50, null=True, blank=True)
    distancia_izquierda = models.CharField(max_length=50, null=True, blank=True)
    distancia_fondo = models.CharField(max_length=50, null=True, blank=True)
    precio_m2 = models.CharField(max_length=50, null=True, blank=True)

    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True, blank=True)
    id_manzana = models.ForeignKey(Manzana, on_delete=models.CASCADE, null=True, blank=True)
    
    
    def __str__(self):
        if self.id_manzana:
            return f"Lote {self.numero_lote} - Manzana {self.id_manzana.nombre_manzana}"
        else:
            return f"Lote {self.numero_lote} - Sin Manzana asignada"

# Fin del modelo Lote
# ===========================================


# Inicio del modelo Persona
=======
>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9

class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombres_apellidos = models.CharField(max_length=255, null=True, blank=True)
    celular = models.CharField(max_length=9, null=True, blank=True)
    dni = models.CharField(max_length=8, null=True, blank=True)
    correo = models.EmailField()
    conyuge = models.BooleanField(null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
<<<<<<< HEAD
    fecha_registro = models.CharField(max_length=255, null=True, blank=True)
    profesion = models.CharField(max_length=100, null=True, blank=True)
    ocupacion = models.CharField(max_length=100, null=True, blank=True)
    centro_trabajo = models.CharField(max_length=255, null=True, blank=True)
    direccion_laboral = models.CharField(max_length=255, null=True, blank=True)
    antiguedad_laboral = models.CharField(
        max_length=100, null=True, blank=True)
    constancia_inicial = models.CharField(
        max_length=100, null=True, blank=True)
=======
>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9
    id_rol = models.ForeignKey(
        Rol, on_delete=models.CASCADE, null=True, blank=True)
    id_area = models.ForeignKey(
        Area, on_delete=models.CASCADE, null=True, blank=True)  # id tabla Area
<<<<<<< HEAD
    id_origen = models.ForeignKey(
        Origen, on_delete=models.CASCADE, null=True, blank=True)
    id_canal = models.ForeignKey(
        Canal, on_delete=models.CASCADE, null=True, blank=True)
    id_medio = models.ForeignKey(
        Medio, on_delete=models.CASCADE, null=True, blank=True)

    proyectos = models.ManyToManyField(
        Proyecto, through='PersonaProyecto', related_name='personas')
=======
    proyectos = models.ManyToManyField(Proyecto, through='PersonaProyecto', related_name='personas')
>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9

    def __str__(self):
        return self.nombres_apellidos

<<<<<<< HEAD
# Fin del modelo Persona
# ===========================================



# Inicio del modelo Observaciones

class Observaciones(models.Model):
    id_observaciones = models.AutoField(primary_key=True)
    descripcion_observaciones = models.CharField(max_length=255)
    adjuntar_informacion = models.CharField(max_length=255)
    id_persona = models.ForeignKey(
        Persona, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.id_observaciones

# Fin del modelo Observaciones
# ===========================================


# Inicio del modelo CronogramaPagos
=======

class ClienteCerrado(models.Model):
    id_cliente_cerrado = models.AutoField(primary_key=True)
    profesion = models.CharField(max_length=100)
    ocupacion = models.CharField(max_length=100)
    centro_trabajo = models.CharField(max_length=255)
    direccion_laboral = models.CharField(max_length=255)
    antiguedad_laboral = models.CharField(max_length=100)
    constancia_inicial = models.CharField(max_length=100)
    id_observaciones = models.ForeignKey(Observaciones, on_delete=models.CASCADE)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.id_cliente_cerrado


# ============================================================
>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9

class CronogramaPagos(models.Model):
    id_cpagos = models.AutoField(primary_key=True)
    descripcion_cpagos = models.CharField(max_length=255)
    cuota_inicial = models.FloatField()
    cuota_mensual = models.FloatField()
    fecha_inicio_pago = models.CharField(max_length=50)
    plazo_anios = models.CharField(max_length=50)
    plazo_meses = models.CharField(max_length=50)
    TEA = models.FloatField()
    dias_pago = models.CharField(max_length=50)
    descuento = models.FloatField()
<<<<<<< HEAD
    id_persona = models.ForeignKey(
        Persona, on_delete=models.CASCADE, null=True, blank=True)
=======
    id_cuota = models.ForeignKey(Cuota, on_delete=models.CASCADE)
    id_cliente_cerrado = models.ForeignKey(ClienteCerrado, on_delete=models.CASCADE,null=True)
>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9

    def __str__(self):
        return self.descripcion_cpagos

<<<<<<< HEAD
# Fin del modelo CronogramaPagos
# ===========================================


# Inicio del modelo Cuota

class Cuota(models.Model):
    id_cuota = models.AutoField(primary_key=True)
    numero_cuotas = models.CharField(max_length=50)
    fecha_vencimiento = models.CharField(max_length=50)
    deuda_total = models.FloatField()
    amortizacion = models.FloatField()
    id_cpagos = models.ForeignKey(
        CronogramaPagos, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.id_cuota

# Fin del modelo Cuota
# ===========================================


# Inicio del modelo PersonaProyecto
=======

# =============================================================


class CPagosPersona(models.Model):
    id_cpagos = models.ForeignKey(CronogramaPagos, on_delete=models.CASCADE)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('id_cpagos', 'id_persona'),)

    def __str__(self):
        return f"cpagos {self.id_cpagos} - Persona {self.id_persona}"


class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre_estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_estado





class Manzana(models.Model):
    id_manzana = models.AutoField(primary_key=True)
    nombre_manzana = models.CharField(max_length=10)
    id_proyecto = models.ForeignKey(
        Proyecto, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre_manzana


class Lote(models.Model):
    id_lote = models.AutoField(primary_key=True)
    numero_lote = models.CharField(max_length=50)
    area = models.FloatField()
    perimetro = models.CharField(max_length=50, null=True)
    colindacia_frente = models.CharField(max_length=50, null=True)
    colindacia_derecha = models.CharField(max_length=50, null=True)
    colindacia_izquierda = models.CharField(max_length=50, null=True)
    colindacia_fondo = models.CharField(max_length=50, null=True)
    distancia_frente = models.CharField(max_length=50, null=True)
    distancia_derecha = models.CharField(max_length=50, null=True)
    distancia_izquierda = models.CharField(max_length=50, null=True)
    distancia_fondo = models.CharField(max_length=50, null=True)
    precio_m2 = models.CharField(max_length=50, null=True)

    ip_estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True)
    ip_manzana = models.ForeignKey(
        Manzana, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.numero_lote

>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9

class PersonaProyecto(models.Model):
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    id_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
<<<<<<< HEAD
    id_manzana = models.ForeignKey(
        Manzana, on_delete=models.CASCADE, null=True, blank=True)
    id_lote = models.ForeignKey(
        Lote, on_delete=models.CASCADE, null=True, blank=True)
    id_cpagos = models.ForeignKey(
        CronogramaPagos, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Persona {self.id_persona} - Proyecto {self.id_proyecto} - Manzana {self.id_manzana} - Lote {self.id_lote}"

# Fin del modelo PersonaProyecto
# ===========================================

=======
    id_manzana = models.ForeignKey(Manzana, on_delete=models.CASCADE,null=True, blank=True)
    id_lote = models.ForeignKey(Lote, on_delete=models.CASCADE,null=True, blank=True)


    def __str__(self):
        return f"Persona {self.id_persona} - Proyecto {self.id_proyecto} - Manzana {self.id_manzana} - Lote {self.id_lote}"
>>>>>>> f29fca78a5079d453a12354ff714b4f741a9cab9
