class Empresa:
    def __init__(self,nom,ruc,tel,dir):
        self.nombre=nom
        self.ruc=ruc
        self.telefono=tel
        self.direccion=dir
    
    def mostrarEmpresa(self):
        print("Empresa: {}, RUC: {}".format(self.nombre,self.ruc))

class Cliente:
    def __init__(self,nom,ced,tel):
        self.nombre=nom
        self.cedula=ced
        self.telefono=tel
    
    def mostrarCliente(self):
        print(self.nombre,self.cedula,self.telefono)

class ClienteCorporativo(Cliente):
    def __init__(self,contrato):
        super().__init__(nom,ced,tel,contrato)
        self.__contrato=contrato

    @property
    def contrato(self):     #getter: obtener el valor del atributo privado
        return self.__contrato
    @contrato.setter
    def contrato(self,value):     #setter: asigna el valor del atributo privado
        self.__contrato = value 

    def mostrarCliente(self):
        print(self.nombre, self.__contrato)

class ClientePersonal(Cliente):
    def __init__(self,contrato):
        super().__init__(nom,ced,tel,promocion)
        self.__promocion=promocion

    @property
    def promocion(self):     #getter: obtener el valor del atributo privado
        return self.__promocion
    return None

    def mostrarCliente(self):
        print(self.nombre, self.__promocion)        

# emp=Empresa("El mas barato","0953156049","0998132446","Coop. Juan Montalvo")
# emp.mostrarEmpresa()
# print(emp.nombre)

cli=ClienteCorporativo("0001")
cli.mostrarCliente
print("terminado")

