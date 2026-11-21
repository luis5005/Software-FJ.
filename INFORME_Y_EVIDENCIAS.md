# Informe de desarrollo – Software FJ

## 1. Objetivo
Desarrollar una aplicación orientada a objetos que permita gestionar clientes, servicios y reservas para Software FJ, aplicando principios de POO y mecanismos de manejo de excepciones.

## 2. Contexto del problema
Software FJ ofrece alquiler de salas, equipos tecnológicos y asesorías especializadas. La gestión manual puede ocasionar registros duplicados, pérdida de información y cruces de horarios. La aplicación centraliza temporalmente los registros y valida la disponibilidad de los servicios antes de confirmar una reserva.

## 3. Solución propuesta
El sistema permite registrar y consultar clientes y servicios, crear reservas, evitar que un mismo servicio sea asignado a dos reservas activas en la misma fecha y hora, y cancelar reservas. La información se administra en memoria, sin base de datos.

## 4. Diseño orientado a objetos
La clase abstracta `Servicio` define atributos y comportamientos comunes. Las clases `Sala`, `Equipo` y `Asesoria` especializan sus características. `Cliente` representa a los usuarios y `Reserva` relaciona un cliente con un servicio, fecha y hora. `GestorSistema` coordina las operaciones.

## 5. Excepciones y registros
Se definieron excepciones para datos inválidos, registros duplicados, registros inexistentes y horarios no disponibles. El módulo `logging` registra eventos y errores en el archivo `software_fj.log`.

## 6. Pruebas
El proyecto contiene 15 pruebas unitarias que verifican registros, duplicados, validación de correo, creación y cancelación de reservas, conflictos de horario, fechas inválidas y cálculo de costos.

## 7. Evidencias que debe capturar el estudiante
1. Proyecto abierto en Visual Studio Code mostrando sus archivos.
2. Ejecución del menú principal.
3. Registro y consulta de un cliente.
4. Visualización de los tres tipos de servicios.
5. Creación de una reserva.
6. Intento de crear una reserva duplicada en el mismo horario y mensaje de validación.
7. Cancelación de una reserva.
8. Ejecución de las 15 pruebas con resultado exitoso.
9. Archivo `software_fj.log` con eventos registrados.

## 8. Conclusión
El desarrollo permitió aplicar los principios de programación orientada a objetos en un caso práctico. La separación de responsabilidades facilita el mantenimiento del código y las validaciones disminuyen errores en la gestión de reservas. El sistema cumple el alcance académico definido y puede ampliarse posteriormente con persistencia de datos e interfaz gráfica.

## 9. Datos académicos por completar
- Estudiante: [Escriba su nombre completo]
- Curso: [Nombre del curso]
- Código del curso: [Código]
- Grupo: [Número o identificación del grupo]
- Docente: [Nombre]
- Universidad: [Nombre]
- Fecha: [Fecha de entrega]
