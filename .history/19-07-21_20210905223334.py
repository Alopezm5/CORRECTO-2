class  MENU ():
    def  __init__(self,titulo,opciones=[]):
        self.titulo = titulo
        self.opciones = opciones

    def menu(self):
        print(self.titulo)
        for opcion  in range(self.opciones) :
            print ( opcion )
        opc = input ( "Elije opcion [1 ..... {}]:" . formato ( len ( self . opciones )))
        return  opc

menu1 = MENU ( "Menú Principal" , [ "1) Calculadora" , "2) Numeros" , "3) Listas" , "4) Cadenas" , "5) Salir" ])
opc  =  menu1.menu()
if  opc == "1" :
            menu1 = MENU ( "Menú Calculadora" , [ "1) Suma" , "2) Resta" , "3) Multiplicacion" , "4) División" , "5) Salir" ])
            opc1  =  menu1 . menu ()
            if  opc1 == "1" :
                print ( "Opcion Suma" )
                n1 = int ( input ( "Ingresar n1:" ))
                n2 = int ( input ( "Ingresar n2:" ))
                suma = n1 + n2
                print ( "{} + {} = {}" . formato ( n1 , n2 , suma ))
            elif  opc1 == "2" :
                print ( "Opcion Resta" )
                n1  =  int ( input ( "Ingresar n1:" ))
                n2  =  int ( input ( "Ingresar n2:" ))
                resta  =  n1  -  n2
                print ( "{} - {} = {}" . formato ( n1 , n2 , resta ))
            elif  opc1 == "3" :
                print ( "Opcion Multiplicacion" )
                n1  =  int ( input ( "Ingresar n1:" ))
                n2  =  int ( input ( "Ingresar n2:" ))
                multiplicacion  =  n1  *  n2
                print ( "{} * {} = {}" . formato ( n1 , n2 , multiplicacion ))
            elif  opc1  ==  "4" :
                print ( "Opcion Division" )
                n1  =  int ( input ( "Ingresar n1:" ))
                n2  =  int ( input ( "Ingresar n2:" ))
                division  =  n1  /  n2
                print ( "{} / {} = {}" . formato ( n1 , n2 , division ))
            elif  opc1 == "5" :
                print ( "Opcion Salir" )
elif  opc == "2" :
            menu2 = MENU ( "Menú Numero" , [ "1) Perfecto" , "2) Primo" , "3) Salir" ])
            opc2  =  input ( "Elije opcion [1 ..... 3]:" )
elif  opc == "3" :
            print ( "Listas de menú" )
elif  opc == "4" :
            print ( "Menú Cadenas" )
elif  opc == "5" :
            print ( "Menú Salir" )
else:
            print ( "Opcion no valida" )
            