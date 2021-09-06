class Calculadora:
    def __init__(self,numero1,numero2):
        self.numero1=numero1
        self.numero2=numero2

    def suma(self):
        return self.numero1+self.numero2

    def resta(self):
        return self.numero1-self.numero2
    
    def multiplicacion(self):
        return self.numero1*self.numero2

    def division(self):
        return self.numero1/self.numero2

class CalEstandar(Calculadora):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
    
    def multiplicacion(self):
        return self.numero1*self.numero2

    def exponente(self):
        pass

    def valorAbsoluto(self,numero):
        if numero<0:
            numero=numero*(-1)
        return numero

class CalEstandar(Calculadora):
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
                
# cal=Calculadora(4,8)  
# cal.multiplicacion()      
calEsta=CalEstandar(4,8)
print(calEsta.multiplicacion( ))
