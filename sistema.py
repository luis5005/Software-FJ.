from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import date, time
import logging
from excepciones import (
    DatoInvalidoError, RegistroDuplicadoError,
    RegistroNoEncontradoError, ReservaNoDisponibleError
)

logging.basicConfig(
    filename="software_fj.log", level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"
)
logger = logging.getLogger("SoftwareFJ")

@dataclass
class Cliente:
    id: str
    nombre: str
    correo: str
    telefono: str

    def __post_init__(self):
        if not all(x.strip() for x in (self.id, self.nombre, self.correo, self.telefono)):
            raise DatoInvalidoError("Todos los campos del cliente son obligatorios.")
        if "@" not in self.correo:
            raise DatoInvalidoError("El correo electrónico no tiene un formato válido.")

    def __str__(self):
        return f"{self.id} | {self.nombre} | {self.correo} | {self.telefono}"

class Servicio(ABC):
    def __init__(self, id, nombre, tarifa):
        if not id.strip() or not nombre.strip() or tarifa <= 0:
            raise DatoInvalidoError("El servicio requiere ID, nombre y tarifa positiva.")
        self._id = id
        self._nombre = nombre
        self._tarifa = float(tarifa)

    @property
    def id(self): return self._id
    @property
    def nombre(self): return self._nombre
    @property
    def tarifa(self): return self._tarifa

    @abstractmethod
    def descripcion(self): pass

    def calcular_costo(self, horas=1):
        if horas <= 0: raise DatoInvalidoError("La duración debe ser mayor que cero.")
        return self.tarifa * horas

    def __str__(self):
        return f"{self.id} | {self.nombre} | {self.descripcion()} | ${self.tarifa:,.0f}"

class Sala(Servicio):
    def __init__(self, id, nombre, capacidad, tarifa):
        super().__init__(id, nombre, tarifa)
        if capacidad <= 0: raise DatoInvalidoError("La capacidad debe ser positiva.")
        self.capacidad = capacidad

    def descripcion(self):
        return f"Sala para {self.capacidad} personas"

    def calcular_costo(self, horas=1):
        return super().calcular_costo(horas) * (1.10 if horas >= 4 else 1)

class Equipo(Servicio):
    def __init__(self, id, nombre, especificaciones, tarifa):
        super().__init__(id, nombre, tarifa)
        self.especificaciones = especificaciones

    def descripcion(self):
        return f"Alquiler de equipo: {self.especificaciones}"

class Asesoria(Servicio):
    def __init__(self, id, nombre, especialidad, tarifa):
        super().__init__(id, nombre, tarifa)
        self.especialidad = especialidad

    def descripcion(self):
        return f"Asesoría especializada en {self.especialidad}"

@dataclass
class Reserva:
    id: str
    cliente_id: str
    servicio_id: str
    fecha: str
    hora: str
    estado: str = "ACTIVA"

    def __post_init__(self):
        try:
            date.fromisoformat(self.fecha)
            time.fromisoformat(self.hora)
        except ValueError as exc:
            raise DatoInvalidoError("Fecha u hora inválida. Use AAAA-MM-DD y HH:MM.") from exc

    def __str__(self):
        return (f"{self.id} | Cliente: {self.cliente_id} | Servicio: {self.servicio_id} "
                f"| {self.fecha} {self.hora} | {self.estado}")

class GestorSistema:
    def __init__(self):
        self.clientes = {}
        self.servicios = {}
        self.reservas = {}

    def _registrar(self, coleccion, objeto, tipo):
        try:
            if objeto.id in coleccion:
                raise RegistroDuplicadoError(f"El ID {objeto.id} ya está registrado.")
            coleccion[objeto.id] = objeto
            logger.info("%s registrado: %s", tipo, objeto.id)
        except RegistroDuplicadoError as exc:
            logger.exception("Intento de registro duplicado")
            raise
        else:
            logger.info("Operación de registro completada correctamente.")
        finally:
            logger.info("Finalizó el proceso de registro de %s.", tipo)

    def registrar_cliente(self, cliente):
        self._registrar(self.clientes, cliente, "cliente")

    def registrar_servicio(self, servicio):
        self._registrar(self.servicios, servicio, "servicio")

    def crear_reserva(self, reserva):
        try:
            if reserva.cliente_id not in self.clientes:
                raise RegistroNoEncontradoError("El cliente no está registrado.")
            if reserva.servicio_id not in self.servicios:
                raise RegistroNoEncontradoError("El servicio no está registrado.")
            if reserva.id in self.reservas:
                raise RegistroDuplicadoError("El ID de reserva ya existe.")
            for existente in self.reservas.values():
                if (existente.servicio_id == reserva.servicio_id and
                    existente.fecha == reserva.fecha and existente.hora == reserva.hora and
                    existente.estado == "ACTIVA"):
                    raise ReservaNoDisponibleError("El servicio ya tiene una reserva en ese horario.")
            self.reservas[reserva.id] = reserva
            logger.info("Reserva creada: %s", reserva.id)
        except (RegistroNoEncontradoError, RegistroDuplicadoError, ReservaNoDisponibleError) as exc:
            logger.exception("No se pudo crear la reserva")
            raise
        else:
            logger.info("Reserva validada y almacenada en memoria.")
        finally:
            logger.info("Finalizó el intento de creación de reserva.")

    def cancelar_reserva(self, reserva_id):
        if reserva_id not in self.reservas:
            raise RegistroNoEncontradoError(f"No existe la reserva {reserva_id}.")
        self.reservas[reserva_id].estado = "CANCELADA"
        logger.info("Reserva cancelada: %s", reserva_id)

    def buscar_cliente(self, cliente_id):
        if cliente_id not in self.clientes:
            raise RegistroNoEncontradoError(f"No existe el cliente {cliente_id}.")
        return self.clientes[cliente_id]

    def buscar_servicio(self, servicio_id):
        if servicio_id not in self.servicios:
            raise RegistroNoEncontradoError(f"No existe el servicio {servicio_id}.")
        return self.servicios[servicio_id]
