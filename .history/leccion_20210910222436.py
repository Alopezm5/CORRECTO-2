# frase=input("ingresas frase")
# c=frase.read()
# if c>1 and c<=5:
#     print(frase)
# else:
#     print("ingrese bien la frase")    

from datetime import date
class Calculos:
    def ant(self,fecha):
        hoy=date.today()
        if hoy<fecha:
            return -1
        else:
            anio=fecha.year
            mes=fecha.month
            dia=fecha.day
            aa=0
            while fecha<hoy:
                aa+=1
                fecha=date(anio+aa,mes,dia)
                
