archivo,f="datos.txt",""
docentes=[{"nombre":"Jose", "edad":21,"fac":"Ingenieria"},
    {"nombre":"Juan", "edad":30,"fac":"Salud"},
    {"nombre":"Yadil", "edad":40,"fac":"Administracion"}]

#Escribir archivo: w - a: write - writeline
with open(archivo,"M") as writer:
    for i in range(len(docentes)):
        linea=""
        for clave, valor in docentes[i].items():
            if clave =="fac":
                linea=linea+(str(valor) if type(valor)==int else valor)
                