class MENU():
    def __init__(self,titulo,opciones=[]):
        self.titulo=titulo
        self.opciones=opciones

    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc=input("Elije opcion [1.....{}]:".format(len(self.opciones)))
        return opc

menu1=MENU("Menu Principal",["1)Calculadora", "2)Numeros", "3)Listas", "4)Cadenas", "5)Salir"] )
opc = menu1.menu()
if opc=="1":
            menu1=MENU("Menu Calculadora", ["1)Suma","2)Resta","3)Multiplicacion","4)Division","5)Salir"])
            opc1 = menu1.menu()
            if opc1=="1":
                print("Opcion Suma")
                n1=int(input("Ingresar n1: "))
                n2=int(input("Ingresar n2: "))
                suma=n1+n2
                print("{} + {} = {}".format(n1,n2,suma))
            elif opc1=="2":
                print("Opcion Suma")
                n1 = int(input("Ingresar n1: "))
                n2 = int(input("Ingresar n2: "))
                suma = n1 - n2
                print("{} - {} = {}".format(n1, n2, suma))
            elif opc1=="3":
                print("Opcion Multiplicacion")
            elif opc1 == "4":
                print("Opcion Division")
            elif opc1=="5":
                print("Opcion Salir")
elif opc=="2":
            menu2=MENU("Menu Numero", ["1)Perfecto","2)Primo","3)Salir"])
            opc2 = input("Elije opcion [1.....3]:")
elif opc=="3":
            print("Menu Listas")
elif opc=="4":
            print("Menu Cadenas")
elif opc=="5":
            print("Menu Salir")
else:
            print("Opcion no valida")
