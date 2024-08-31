from django.db import models


# Aquí se crean los modelos de la aplicación.
# Un modelo en Django es una clase que define la estructura de una tabla en la base de datos.




# Inicio del modelo Area

class Area(models.Model):

    id_area = models.AutoField(primary_key=True)
    nombre_area = models.CharField(max_length=100, null=True, blank=True)
    descripcion_area = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nombre_area


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

class Medio (models.Model):
    id_medio = models.AutoField(primary_key=True)
    nombre_medio = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_medio

# Fin del modelo Medio
# ===========================================


# Inicio del modelo Rol


class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombre_rol


# Fin del modelo Rol
# ===========================================




# Inicio del modelo Proyecto

class Proyecto(models.Model):
    id_proyecto = models.AutoField(primary_key=True)
    nombre_proyecto = models.CharField(max_length=100)
    fecha_inicio = models.DateField(null=True, blank=True)
    
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

# Fin del modelo Proyecto
# ===========================================



# Inicio del modelo Lote

class Lote(models.Model):
    id_lote = models.AutoField(primary_key=True)
    manzana_lote = models.CharField(max_length=50, null=True, blank=True)
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
        return f"Lote {self.manzana_lote}"


# Fin del modelo Lote
# ===========================================


# Inicio del modelo Usuario

class Usuario(models.Model):

    id_usuario = models.AutoField(primary_key=True)
    password = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.id_usuario


# Fin del modelo Usuario
# ===========================================


# Inicio del modelo Documento

class Documento(models.Model):

    id_documento = models.AutoField(primary_key=True)
    nombre_documento = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nombre_documento


# Fin del modelo Usuario
# ===========================================


# Inicio del modelo Persona

class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=255, null=True, blank=True)
    apellidos = models.CharField(max_length=255, null=True, blank=True)
    celular = models.CharField(max_length=9, null=True, blank=True)
    dni = models.CharField(max_length=8, null=True, blank=True)
    correo = models.EmailField(max_length=100, null=True, blank=True)
    conyuge = models.BooleanField(null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    fecha_registro = models.CharField(max_length=255, null=True, blank=True)
    profesion = models.CharField(max_length=100, null=True, blank=True)
    ocupacion = models.CharField(max_length=100, null=True, blank=True)
    centro_trabajo = models.CharField(max_length=255, null=True, blank=True)
    direccion_laboral = models.CharField(max_length=255, null=True, blank=True)
    antiguedad_laboral = models.CharField(
        max_length=100, null=True, blank=True)
    constancia_inicial = models.CharField(
        max_length=100, null=True, blank=True)
    id_rol = models.ForeignKey(
        Rol, on_delete=models.CASCADE, null=True, blank=True)
    id_area = models.ForeignKey(
        Area, on_delete=models.CASCADE, null=True, blank=True)  # id tabla Area
    id_origen = models.ForeignKey(
        Origen, on_delete=models.CASCADE, null=True, blank=True)
    id_canal = models.ForeignKey(
        Canal, on_delete=models.CASCADE, null=True, blank=True)
    id_medio = models.ForeignKey(
        Medio, on_delete=models.CASCADE, null=True, blank=True)
    id_documento = models.ForeignKey(
        Documento, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombres

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
        return self.descripcion_observaciones

# Fin del modelo Observaciones
# ===========================================



# Inicio del modelo CronogramaPagos

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
    cuota_balloon = models.FloatField(null=True, blank=True)
    cuota_balloon_meses = models.CharField(max_length=50,null=True, blank=True)

    def __str__(self):
        return self.descripcion_cpagos

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
        return f"Cuota {self.numero_cuotas}"

# Fin del modelo Cuota
# ===========================================


# Inicio del modelo FichaDatosCliente

class FichaDatosCliente(models.Model):
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    id_lote = models.ForeignKey(
        Lote, on_delete=models.CASCADE, null=True, blank=True)
    id_cpagos = models.ForeignKey(
        CronogramaPagos, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Persona {self.id_persona} - Proyecto {self.id_proyecto} - Lote {self.id_lote}"

# Fin del modelo FichaDatosCliente
# ===========================================

