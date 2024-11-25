from django.db import models

class Usuario(models.Model):
    # Atributos para el modelo Usuario
    name = models.CharField(max_length=100)  # Nombre del usuario
    email = models.EmailField(unique=True)   # Correo electrónico único

    def __str__(self):
        return self.name

class Camera(models.Model):
    # Atributos para el modelo Camera
    name = models.CharField(max_length=100, unique=True)  # Nombre único de la cámara
    lockers_count = models.PositiveIntegerField(default=0)  # Cantidad de casilleros que maneja la cámara

    def __str__(self):
        return self.name

class Casillero(models.Model):
    # Atributos para el modelo Casillero
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)  # Relación con el modelo Usuario
    password = models.CharField(max_length=100)  # Contraseña del casillero
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE, related_name='casilleros')  # Relación con la cámara
    locker_id = models.CharField(max_length=50, unique=True)  # Un identificador único para cada casillero

    def save(self, *args, **kwargs):
        # Generar el ID único para locker_id basado en la cámara y un número secuencial
        if not self.locker_id:  # Solo si no tiene un valor ya
            # Obtener el contador de casilleros de esa cámara y actualizarlo
            casillero_count = Casillero.objects.filter(camera=self.camera).count() + 1
            self.locker_id = f"{self.camera.name}_{casillero_count}"

            # Actualizar la cantidad de casilleros en la cámara
            self.camera.lockers_count = casillero_count
            self.camera.save()
        
        super().save(*args, **kwargs)  # Llamar al método save original para guardar la instancia

    def __str__(self):
        if self.camera is not None:
            return f"Locker {self.locker_id} for camera {self.camera.name}"
        return f"Locker {self.locker_id} (no camera assigned)"
class LockerLog(models.Model):
    EVENT_TYPES = [
        ('open', 'Apertura'),
        ('close', 'Cierre'),
    ]
    
    locker = models.ForeignKey(Casillero, on_delete=models.CASCADE, related_name='logs')
    event_type = models.CharField(max_length=5, choices=EVENT_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_event_type_display()} - Locker {self.locker.locker_id} at {self.timestamp}"
