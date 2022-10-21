
#input

ventas =([
        (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
        (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
        (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),    
        (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
        (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')], 2010)

ventas1 = ([
        (9852,'Culata', 'XC9875',2,165,'Luis Molero',3455846,'15/06/2020'),
        (9852,'Culata', 'XC9875',2,165,'Jose Mejia',1355846,'15/06/2020'),
        (2564,'Cárter', 'PT29872',2,32,'Peter Cerezo',8545436,'15/06/2020'),
        (5412,'válvula', 'AZ8798',2,11,'Juan Peña',568975,'15/06/2020')], 2564)

#Functions
def Autopartes(ventas: list) -> dict:
    return {'Registro': ventas[0]}

def consultaRegistro(ventas: dict, idProducto: int) -> str:
    lst = []
    r = ventas['Registro']
    for i in r:
        if i[0] == idProducto:
            lst.append(f'Producto consultado : {i[0]} Descripción {i[1]} #Parte {i[2]} Cantidad vendida {i[3]} Stock {i[4]} Comprador {i[5]} Documento {i[6]} Fecha Venta {i[7]}')
    if len(lst) == 0:
        lst.append('No hay registro de venta de ese producto')
    return lst

if __name__ == '__main__':
    a = consultaRegistro(Autopartes(ventas), 2010)
    print(*a)