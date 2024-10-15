from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import timedelta
from datetime import date
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


# Aquí se crean los modelos de la aplicación.
# Un modelo en Django es una clase que define la estructura de una tabla en la base de datos.




# Inicio del modelo Empresa

class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=100)
    ruc = models.CharField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre_empresa

    def delete(self, *args, **kwargs):
        raise ValidationError("La eliminación de registros no está permitida.")

# Fin del modelo Empresa
# ===========================================




# Inicio del modelo PersonaStaff

class PersonaStaff(models.Model):
    id_persona_staff = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombres = models.CharField(max_length=255, null=True, blank=True)
    apellidos = models.CharField(max_length=255, null=True, blank=True)
    area = models.CharField(max_length=255, null=True, blank=True)
    dni = models.CharField(max_length=8, null=True, blank=True)
    conyuge = models.BooleanField(default=False)  # Por defecto 'No'
    correo = models.EmailField(max_length=100, null=True, blank=True)
    celular = models.CharField(max_length=9, null=True, blank=True)
    fecha_inicio = models.DateField(default=timezone.now)  # Fecha por defecto: hoy
    fecha_fin = models.DateField(null=True, blank=True)
    rol = models.CharField(null=True, blank=True)
    foto = models.ImageField(upload_to='personas/', null=True, blank=True)  # Nuevo campo
    centro_costos = models.CharField(max_length=100,null=True, blank=True)

    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombres
    
    def delete(self, *args, **kwargs):
        raise ValidationError("La eliminación de registros no está permitida.")

# Fin del modelo PersonaStaff
# ===========================================




# Inicio del modelo Proyecto

class Proyecto(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    nombre_proyecto = models.CharField(max_length=100)
    fecha_inicio = models.DateField(null=True, blank=True)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True, blank=True)
    
    imagen = models.ImageField(upload_to='proyectos/', null=True, blank=True)  # Nuevo campo

    def save(self, *args, **kwargs):
        if not self.id_proyecto:  # Solo si no hay un ID asignado
            existing_ids = Proyecto.objects.values_list('id_proyecto', flat=True).order_by('id_proyecto')
            if existing_ids:
                missing_ids = set(range(1, max(existing_ids) + 1)) - set(existing_ids)
                if missing_ids:
                    self.id_proyecto = min(missing_ids)
                else:
                    self.id_proyecto = max(existing_ids) + 1
            else:
                # Si no hay objetos en la base de datos, el primer ID será 1
                self.id_proyecto = 1

        super(Proyecto, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre_proyecto
    
    def delete(self, *args, **kwargs):
        raise ValidationError("La eliminación de registros no está permitida.")

# Fin del modelo Proyecto
# ===========================================



# Inicio del modelo Lote

class Lote(models.Model):
    id_lote = models.AutoField(primary_key=True)
    manzana_lote = models.CharField(max_length=50, null=True, blank=True)
    area = models.FloatField(null=True, blank=True)
    perimetro = models.FloatField(max_length=50, null=True, blank=True)
    colindancia_frente = models.CharField(max_length=50, null=True, blank=True)
    colindancia_derecha = models.CharField(max_length=50, null=True, blank=True)
    colindancia_izquierda = models.CharField(max_length=50, null=True, blank=True)
    colindancia_fondo = models.CharField(max_length=50, null=True, blank=True)
    distancia_frente = models.FloatField(max_length=50, null=True, blank=True)
    distancia_derecha = models.FloatField(max_length=50, null=True, blank=True)
    distancia_izquierda = models.FloatField(max_length=50, null=True, blank=True)
    distancia_fondo = models.FloatField(max_length=50, null=True, blank=True)
    precio_lote_dolares = models.FloatField(max_length=50, null=True, blank=True)
    precio_m2_dolares = models.FloatField(max_length=50, null=True, blank=True)
    estado = models.CharField(max_length=50, null=True, blank=True)

    id_proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.id_lote:  # Solo si no hay un ID asignado
            existing_ids = Lote.objects.values_list('id_lote', flat=True).order_by('id_lote')
            if existing_ids:
                missing_ids = set(range(1, max(existing_ids) + 1)) - set(existing_ids)
                if missing_ids:
                    self.id_lote = min(missing_ids)
                else:
                    self.id_lote = max(existing_ids) + 1
            else:
                # Si no hay objetos en la base de datos, el primer ID será 1
                self.id_lote = 1

        super(Lote, self).save(*args, **kwargs)

    def __str__(self):
        return f"Lote {self.manzana_lote} - Proyecto {self.id_proyecto.nombre_proyecto}"
    
    def delete(self, *args, **kwargs):
        raise ValidationError("La eliminación de registros no está permitida.")


# Fin del modelo Lote
# ===========================================


# Inicio del modelo PersonaClient

class PersonaClient(models.Model):
    id_persona_client = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=255, null=True, blank=True)
    apellidos = models.CharField(max_length=255, null=True, blank=True)
    genero = models.CharField(max_length=255, null=True, blank=True)
    celular = models.CharField(max_length=9, null=True, blank=True)
    correo = models.EmailField(max_length=100, null=True, blank=True)
    pais = models.CharField(max_length=255, default="PERU")
    departamento = models.CharField(max_length=255, null=True, blank=True)
    provincia = models.CharField(max_length=255, null=True, blank=True)
    distrito = models.CharField(max_length=255, null=True, blank=True)
    fecha_creacion = models.DateField(default=timezone.now)  # Fecha por defecto: hoy
    ocupacion = models.CharField(max_length=100, null=True, blank=True)
    centro_trabajo = models.CharField(max_length=255, null=True, blank=True)
    tipo_documento = models.CharField(max_length=255, null=True, blank=True)
    num_documento = models.CharField(max_length=255, null=True, blank=True)
    conyuge = models.BooleanField(default=False)  # Por defecto 'No'
    telefono_fijo = models.CharField(max_length=20, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)

    # def clean(self):
    #     # Validación personalizada: si usuario es True, password no puede estar vacío
    #     if self.usuario and not self.password:
    #         raise ValidationError("El campo 'password' es obligatorio cuando 'usuario' está activado.")
    
    def __str__(self):
        return f"{self.nombres} - {self.num_documento}"
    
    # def save(self, *args, **kwargs):
    #     # Encriptar la contraseña si no está ya encriptada
    #     if self.password and not self.password.startswith('pbkdf2_sha256$'):
    #         self.password = make_password(self.password)
    #     super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        raise ValidationError("La eliminación de registros no está permitida.")

# Fin del modelo PersonaClient
# ===========================================




# Inicio del modelo Observaciones

class Observaciones(models.Model):
    id_observaciones = models.AutoField(primary_key=True)
    descripcion_observaciones = models.CharField(max_length=255)
    adjuntar_informacion = models.CharField(max_length=255)
    id_persona_client = models.ForeignKey(
        PersonaClient, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.descripcion_observaciones
    
    def delete(self, *args, **kwargs):
        raise ValidationError("La eliminación de registros no está permitida.")

# Fin del modelo O  bservaciones
# ===========================================



# Inicio del modelo CronogramaPagos

class CronogramaPagos(models.Model):
    id_cpagos = models.AutoField(primary_key=True)
    cuota_inicial_dolares = models.FloatField(null=True, blank=True)
    cuota_inicial_soles = models.FloatField(null=True, blank=True)
    fecha_pago_cuota = models.DateField(null=True, blank=True)
    fecha_inicio_pago = models.DateField(null=True, blank=True)
    descuento = models.FloatField(null=True, blank=True)
    precio_venta_soles = models.FloatField(null=True, blank=True)
    precio_venta_dolares = models.FloatField(null=True, blank=True)
    precio_m2_soles = models.FloatField(max_length=50, null=True, blank=True)
    precio_m2_dolares = models.FloatField(max_length=50, null=True, blank=True)
    deuda_total_soles= models.FloatField(null=True, blank=True)
    deuda_total_dolares = models.FloatField(null=True, blank=True)
    TEA = models.FloatField(default=0)
    observaciones = models.CharField(max_length=255, null=True, blank=True)
    tipo_cambio = models.FloatField(null=True, blank=True)
    numero_cuotas = models.IntegerField(null=True, blank=True)
    numero_cuotas_pagadas = models.IntegerField(null=True, blank=True)
    tipo_cuota_inicial = models.CharField(max_length=50, null=True, blank=True)
    tipo_moneda = models.CharField(default="SOLES",null=True, blank=True)
    inicial_separacion = models.FloatField(null=True, blank=True)
    inicial_f1 = models.FloatField(null=True, blank=True)  # Primer fracción
    inicial_f2 = models.FloatField(null=True, blank=True)  # Segunda fracción


    def __str__(self):
        return f"CronogramaPagos {self.id_cpagos}"
    
    def delete(self, *args, **kwargs):
        raise ValidationError("La eliminación de registros no está permitida.")


# Fin del modelo CronogramaPagos
# ===========================================




# Inicio del modelo Cuota

class Cuota(models.Model):
    id_cuota = models.AutoField(primary_key=True)
    fecha_pago_cuota = models.DateField(null=True, blank=True)
    pago_adelantado = models.BooleanField(default=False)
    monto_pago_adelantado = models.FloatField(null=True, blank=True)
    monto_cuota = models.FloatField(null=True, blank=True)
    estado = models.BooleanField(default=False) # True: moroso, False: pagado
    dias_morosidad = models.IntegerField(null=True, blank=True)
    id_cpagos = models.ForeignKey(
        CronogramaPagos, on_delete=models.CASCADE, null=True)
    tipo_moneda = models.CharField(default="SOLES",null=True, blank=True)

    def __str__(self):
        return f"Cuota {self.id_cuota} - {self.id_cpagos}"
    
    def clean(self):
        # Validación para asegurar que monto_pago_adelantado solo se llena si pago_adelantado es True
        if not self.pago_adelantado and self.monto_pago_adelantado:
            raise ValidationError("No se puede llenar monto_pago_adelantado si pago_adelantado es False.")

    def delete(self, *args, **kwargs):
        raise ValidationError("La eliminación de registros no está permitida.")

# Fin del modelo Cuota
# ===========================================




# Inicio del modelo FichaDatosCliente

class FichaDatosCliente(models.Model):
    id_fichadc= models.AutoField(primary_key=True)
    estado_legal = models.CharField(null=True, blank=True)
    fecha_cierre = models.DateField(null=True, blank=True)
    fecha_separacion = models.DateField(null=True, blank=True)
    fecha_limite_separacion = models.DateField(null=True, blank=True)
    cod_boleta = models.CharField(null=True, blank=True)
    asesor = models.CharField(null=True, blank=True)

    id_cpagos = models.ForeignKey(
        CronogramaPagos, on_delete=models.CASCADE, null=True, blank=True)
    id_lote = models.ForeignKey(
        Lote, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Cronograma {self.id_cpagos} - Lote {self.id_lote}"
    
    def delete(self, *args, **kwargs):
        raise ValidationError("La eliminación de registros no está permitida.")

# Fin del modelo FichaDatosCliente
# ===========================================




# Inicio del modelo DetallePersona

class DetallePersona(models.Model):
    id_detalle_persona = models.AutoField(primary_key=True)
    tipo_cliente = models.CharField(max_length=255, null=True, blank=True)
    usuario = models.BooleanField(default=False)  # Booleano para indicar si es usuario
    canal = models.CharField(max_length=255, null=True, blank=True)
    medio = models.CharField(max_length=255, null=True, blank=True)
    area = models.CharField(max_length=255, null=True, blank=True)
    origen = models.CharField(max_length=255, null=True, blank=True)
    id_persona_client = models.ForeignKey(
        PersonaClient, on_delete=models.CASCADE, null=True, blank=True)
    id_fichadc = models.ForeignKey(
        FichaDatosCliente, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Detalle Persona {self.id_detalle_persona}"
    
    def delete(self, *args, **kwargs):
        raise ValidationError("La eliminación de registros no está permitida.")


# Fin del modelo DetallePersona
# ===========================================




# Inicio del modelo CuotaInicialFraccionada

class CuotaInicialFraccionada(models.Model):
    id_cuota_inicial = models.AutoField(primary_key=True)
    monto_inicial = models.FloatField(null=True, blank=True)
    id_cpagos = models.ForeignKey(CronogramaPagos, on_delete=models.CASCADE, related_name='cuotas_iniciales_fraccionadas')

    def __str__(self):
        return f"Cuota Inicial {self.id_cuota_inicial} - Cronograma {self.id_cpagos.id_cpagos}"

    def delete(self, *args, **kwargs):
        raise ValidationError("La eliminación de registros no está permitida.")


# Fin del modelo CuotaInicialFraccionada
# ===========================================


# Inicio del modelo PasswordResetToken

class PasswordResetToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        return timezone.now() - self.created_at < timedelta(hours=24)
    
    def delete(self, *args, **kwargs):
        raise ValidationError("La eliminación de registros no está permitida.")

# Fin del modelo PasswordResetToken
# ===========================================



# Inicio del modelo SeparacionCliente

class SeparacionCliente(models.Model):
    id_separacion = models.AutoField(primary_key=True)
    fecha_separacion = models.DateField(default=timezone.now)
    fecha_limite_separacion = models.DateField(null=True, blank=True)
    monto_separacion = models.FloatField(null=True, blank=True)
    estado_separacion = models.CharField(max_length=20, choices=[
        ('ACTIVO', 'Activo'),
        ('CANCELADO', 'Cancelado'),
    ], default='ACTIVO')
    
    id_fichadc = models.ForeignKey('FichaDatosCliente', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Separación {self.id_separacion} - Ficha {self.id_fichadc}"

    def delete(self, *args, **kwargs):
        raise ValidationError("La eliminación de registros no está permitida.")

# Fin del modelo SeparacionCliente
# ===========================================


# Inicio del modelo ObservacionSeparacion

class ObservacionSeparacion(models.Model):
    id_observacion = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    id_separacion = models.ForeignKey('SeparacionCliente', on_delete=models.CASCADE)

    def __str__(self):
        return f"Observación {self.id_observacion} - Separación {self.id_separacion.id_separacion}"

    def delete(self, *args, **kwargs):
        raise ValidationError("La eliminación de registros no está permitida.")

# Fin del modelo ObservacionSeparacion
# ===========================================