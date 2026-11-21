from sistema import GestorSistema, Cliente, Sala, Equipo, Asesoria, Reserva
from excepciones import SoftwareFJError

def cargar_datos_demo(gestor):
    gestor.registrar_cliente(Cliente("C001", "Ana Pérez", "ana@email.com", "3001234567"))
    gestor.registrar_cliente(Cliente("C002", "Carlos Gómez", "carlos@email.com", "3017654321"))
    gestor.registrar_servicio(Sala("S001", "Sala de juntas", 10, 50000))
    gestor.registrar_servicio(Equipo("E001", "Video beam", "Proyector HD", 30000))
    gestor.registrar_servicio(Asesoria("A001", "Asesoría de software", "Desarrollo de sistemas", 80000))

def menu():
    gestor = GestorSistema()
    cargar_datos_demo(gestor)
    while True:
        print("\\n========== SOFTWARE FJ ==========")
        print("1. Ver clientes")
        print("2. Registrar cliente")
        print("3. Ver servicios")
        print("4. Crear reserva")
        print("5. Ver reservas")
        print("6. Cancelar reserva")
        print("7. Salir")
        opcion = input("Seleccione una opción: ").strip()
        try:
            if opcion == "1":
                for c in gestor.clientes.values(): print(c)
            elif opcion == "2":
                cliente = Cliente(input("ID: "), input("Nombre: "), input("Correo: "), input("Teléfono: "))
                gestor.registrar_cliente(cliente)
                print("Cliente registrado.")
            elif opcion == "3":
                for s in gestor.servicios.values(): print(s)
            elif opcion == "4":
                cliente_id = input("ID del cliente: ").strip()
                servicio_id = input("ID del servicio: ").strip()
                fecha = input("Fecha (AAAA-MM-DD): ").strip()
                hora = input("Hora (HH:MM): ").strip()
                reserva = Reserva(f"R{len(gestor.reservas)+1:03}", cliente_id, servicio_id, fecha, hora)
                gestor.crear_reserva(reserva)
                print(f"Reserva creada: {reserva.id}")
            elif opcion == "5":
                for r in gestor.reservas.values(): print(r)
            elif opcion == "6":
                gestor.cancelar_reserva(input("ID de la reserva: ").strip())
                print("Reserva cancelada.")
            elif opcion == "7":
                print("Gracias por utilizar Software FJ.")
                break
            else:
                print("Opción no válida.")
        except SoftwareFJError as exc:
            print(f"No fue posible completar la operación: {exc}")
        except Exception as exc:
            print(f"Error inesperado: {exc}")

if __name__ == "__main__":
    menu()
