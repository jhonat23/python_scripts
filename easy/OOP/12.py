class Lapiz: #creación de una clase y algunos atributos

    def __init__(self, Color, Tamano, Tiene_borrador):#cuando quiero que los objetos inicien con unos atributos establecidos (son valores por default). También puedo agregar parametros al __init__ y a cada parametro un valor inicial
        self.Color=Color #atributos
        self.Tamano=Tamano
        self.Tiene_borrador=Tiene_borrador

    #metodo: acciones que puede realizar un objeto (es una función dentro de la clase), lo creo dentro de la clase
    def dibujar(self): #es necesario colocar la palabra self para métodos (funciones) dentro de la clase
        print("el lapiz esta dibujando")

    def borrar(self): #es necesario colocar la palabra self para métodos (funciones) dentro de la clase
        if self.se_puede_borrar(): #se invoca un metodo en otro anteponiendo la palabra self
            print("el lapiz esta borrando")
        else:
            print("no se puede borrar")

    def se_puede_borrar(self): #puedo llamar un método dentro de otro método # me regresa un verdadero o falso
        return self.Tiene_borrador #si voy a llamar un atributo dentro de un método debo poner .self antes del atributo

Mi_lapiz= Lapiz("Verde", "1.50", True) #es una instancia (objeto creado a partir de una clase) #con __init__ puedo darle de una vez los atributos que quiero o entre los parentesis puedo asignarle de una vez atributos
print(Mi_lapiz.Color)#los atributos no necesitan parentesis
print(Mi_lapiz.Tamano)
print(Mi_lapiz.Tiene_borrador) #visualización de atributos del objeto o instancia
Mi_lapiz.Tiene_borrador=True #puedo modificar atributos desde los llamados
Mi_lapiz.borrar()
Mi_lapiz.dibujar()#los métodos aplicados a objetos deben ir con un parentesis