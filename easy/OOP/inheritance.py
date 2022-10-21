class Notas(): # Clase padre
    #constructor
    def __init__(self, nota1, nota2, nota3):
      self.nota1 = nota1
      self.nota2 = nota2
      self.nota3 = nota3

class Promedio(Notas): # En este caso heredo los atributos de la clase Notas

    def calcular_promedio(self): # Método que requiere los atributos de la clase padre
        return (self.nota1 + self.nota2 + self.nota3) / 3

class Prom75(Promedio): # Heredo los atributos de Notas y los métodos de Promedio

    def prom75(self): # Método para obtener el 75% del promedio
        return self.calcular_promedio() * 0.75 # Traigo el método de la clase padre

class Examen(): # otra clase padre
    # Constructor
    def __init__(self, nota_examen):
      self.nota_examen = nota_examen

    def prom25(self): # Método
        return self.nota_examen * 0.25

class PromedioFinal(Prom75, Examen):# Heredo de dos clases distintas sus atributos y métodos
    def __init__(self, nota1, nota2, nota3, nota_examen):
        super().__init__(nota1, nota2, nota3) # El método super se usa cuando hago un constructor de clases heredadas, se necesita ya que requiero atributos de una de las clases heredadas, tener en cuenta que de esta forma solo aplica para la primer clase que heredé (Prom75)
        self.nota_examen = nota_examen

    def promedio_final(self):
        return self.prom75() + self.prom25() # Traigo lo métodos de las clases padre

if __name__ == '__main__':
    # Creo una instancia (objeto) de notas
    notas = Notas(1,2,3)
    p1 = Promedio(notas.nota1, notas.nota2, notas.nota3)
    # O puedo instanciar p1 directamente con el constructor heredado
    p1 = Promedio(1,2,3)
    #puedo calcular el promedio llamando a su método
    prom = p1.calcular_promedio()
    print(prom)
    # Calculando lo demás
    prom75_1 = Prom75(1,2,3)
    print(prom75_1.prom75())

    exam = Examen(5)
    print(exam.prom25())

    prom_final = PromedioFinal(notas.nota1, notas.nota2, notas.nota3, exam.nota_examen)
    resultado = prom_final.promedio_final()
    print(resultado)

