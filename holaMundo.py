def validacionSigno (valor):
    if(valor == "1"):
        return True
        print ("toy validando en true")
    else:
        return False

def validacionNumerica (var, posicion):
    resultado = True
    size = len(var)

    for (int i = posicion; i < size ; i++)# :P los for son diferentes
        if (var[i].isdigit() &&  size >= 1)
            resultado = True
        else
            resultado = False
    return resultado

#Metodo Principal?

print ("Hola hola ;)")
valor = str (input ("Dame un numero, que soy todo un adivino ... "))

if (validacionSigno(valor) == True):
    if(valor == "1"):
        print ("valido true :)")
    else:
        print ("El número que me diste fue: ", valor, " :P \nChao chao.\n")
else:
    print ("\nNo me diste ningun numero :( ")

