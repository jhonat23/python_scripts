import time
from asyncio import run, gather, sleep

numeros = [1,2,3]

#await sleep(0)

async def frutas():
    print('Manzana')
    await sleep(1)
    print('Fresa')
    await sleep(1)
    print('Mango')
    await sleep(1)

async def hacer_arroz():
    print('Tomo una taza de arroz')
    print('Echo el arroz en la olla con agua')
    await sleep(1)
    print('Enciendo la estufa')
    await frutas()
    print('Reviso el arroz')
    await sleep(1)
    print('Saco el arroz')
    print('Sirvo el arroz')

async def enviar_email():
    await sleep(1)
    print('Abro el PC')
    print('Enciendo el PC')
    time.sleep(3)
    await sleep(1)
    print('Abro mi navegador')
    print('Abro mi correo electrónico')
    await sleep(1)
    print('Creo un nuevo mensaje')
    await sleep(1)
    print('Envío el mensaje')

async def main():
    await gather(hacer_arroz(), enviar_email())

if __name__ == '__main__':
    # def loop(tareas: list) -> None:
    #     while tareas:
    #         tarea_actual = tareas.pop(0)
    #         print('---')
    #         try:
    #             next(tarea_actual)
    #             tareas.append(tarea_actual)
    #         except StopIteration:
    #             pass
    
    # loop([hacer_arroz(), enviar_email()])
    run(main())