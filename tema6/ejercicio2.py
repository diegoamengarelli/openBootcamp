class Alumno:

    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
 
    def imprimir(self):
               print("Nombre: ",self.nombre)
               print("Nota: ",self.nota)
  
    def resultado(self):
            if self.nota >= 6:
                print("El alumno ha aprobado")
            else:
                print("El alumno ha desaprobado")

alumno1 = Alumno()
alumno2 = Alumno()
alumno3 = Alumno()

alumno1.inicializar("Diego", 8)
alumno2.inicializar("Juan", 6)
alumno3.inicializar("Alberto", 4)

alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()
alumno3.imprimir()
alumno3.resultado()