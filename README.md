# Software FJ – Sistema Integral de Gestión

## Descripción
Aplicación de consola desarrollada en Python para administrar clientes, servicios y reservas de una empresa ficticia llamada Software FJ. Los servicios disponibles son reserva de salas, alquiler de equipos y asesorías especializadas.

## Requisitos
- Python 3.10 o superior.
- Visual Studio Code (recomendado).

No requiere instalar librerías externas ni utilizar bases de datos. Los datos se conservan en memoria mientras el programa está abierto. Los eventos y errores se registran en `software_fj.log`.

## Ejecución
1. Descomprima la carpeta del proyecto.
2. Abra la carpeta `Software_FJ_Proyecto_Individual` desde Visual Studio Code.
3. Abra la terminal integrada.
4. Ejecute: `python main.py`
5. Use el menú para registrar clientes, consultar servicios y gestionar reservas.

## Ejecutar pruebas
Desde la terminal, en la carpeta principal, ejecute:
`python -m unittest discover -s tests -v`

El proyecto incluye 15 pruebas automatizadas.

## Estructura
- `main.py`: menú e interacción con el usuario.
- `sistema.py`: clases, reglas del negocio y gestor principal.
- `excepciones.py`: excepciones personalizadas.
- `tests/test_sistema.py`: pruebas automatizadas.
- `software_fj.log`: se crea al ejecutar el programa.

## Conceptos de POO aplicados
- Abstracción: clase abstracta `Servicio`.
- Herencia: `Sala`, `Equipo` y `Asesoria` heredan de `Servicio`.
- Polimorfismo: cada servicio implementa su propia descripción y puede redefinir el cálculo del costo.
- Encapsulamiento: atributos internos y propiedades de acceso en `Servicio`.
- Sobrecarga: redefinición de métodos heredados (`calcular_costo`) y métodos especiales como `__str__`.

## Manejo de errores
Se implementan excepciones personalizadas y validaciones. En los procesos de registro y reserva se utilizan `try`, `except`, `else` y `finally`. Las excepciones se encadenan con `raise ... from exc` cuando se transforma un error de fecha u hora.

## Consideraciones
Este ejercicio es académico. No utiliza una base de datos; la información de clientes, servicios y reservas se almacena temporalmente en diccionarios en memoria. Para conservar datos después de cerrar el programa sería necesario incorporar persistencia, lo cual no forma parte de este alcance.
