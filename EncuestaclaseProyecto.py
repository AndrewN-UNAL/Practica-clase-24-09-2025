#Autor: AndresF.Nuñez
#Fecha: 24/09/2025

def main():
    encuesta()


def encuesta():
    x=1
    resp="Estos son los resultados de la encuesta"
    while x<=10:
        nombre=input("Ingrese su nombre: ")
        proy=input("Ingrese su proyecto de curso: ")
        resp=resp+"\n Nombre: "+nombre+" Proyecto: "+proy
       
        x=x+1
    print(resp)

if __name__ == "__main__":
    main()