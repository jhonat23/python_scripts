
def frutas():
    print('Manzana')
    print('Fresa')
    print('Mango')
    yield

def suena_telefono():
    print('Suena el teléfono')
    yield
    print('Contesto el tel+efono')
    yield
    print('Cuelgo el telefóno')

def hacer_arroz():
    print('Tomo una taza de arroz')
    print('Echo el arroz en la olla con agua')
    yield
    print('Enciendo la estufa')
    yield from frutas()
    print('Reviso el arroz')
    yield
    print('Saco el arroz')
    print('Sirvo el arroz')


def enviar_email():
    print('Abro el PC')
    print('Enciendo el PC')
    yield
    print('Abro mi navegador')
    print('Abro mi correo electrónico')
    yield
    print('Creo un nuevo mensaje')
    yield
    print('Envío el mensaje')


if __name__ == '__main__':
    def loop(tareas: list) -> None:
        while tareas:
            tarea_actual = tareas.pop(0)
            print('---')
            try:
                next(tarea_actual)
                tareas.append(tarea_actual)
            except StopIteration:
                pass
    
    loop([hacer_arroz(), enviar_email()])
