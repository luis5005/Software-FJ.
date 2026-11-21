class SoftwareFJError(Exception):
    """Excepción base del sistema."""

class DatoInvalidoError(SoftwareFJError):
    """Se utiliza cuando un dato no cumple las reglas."""

class RegistroDuplicadoError(SoftwareFJError):
    """Se genera cuando un identificador ya existe."""

class RegistroNoEncontradoError(SoftwareFJError):
    """Se genera cuando no existe el registro solicitado."""

class ReservaNoDisponibleError(SoftwareFJError):
    """Se genera cuando el servicio ya está reservado en esa fecha y hora."""
