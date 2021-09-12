from datetime import date
class Calculos:
    def antiguedad(self,fecha):
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
            return aa

cal = Calculos()
print(cal.antiguedad(date(1971, 6, 9)))
