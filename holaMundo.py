def validacionSigno (valor):
    resultado = False
    if(valor[0] == '-'):
        newValor = valor [1:]
        resultado = newValor.isdigit()
    elif(valor[0] == '+'):
        newValor = valor [1:]
        resultado = newValor.isdigit()
    else:
        resultado = valor.isdigit()
    return resultado

# Metodo principal ?

print ("Hola hola ;)")
valor = "NecesitoUnValorCualquiera"

while ( validacionSigno(valor) == False ):
    valor = str (input ("Dame un numero, que soy todo un adivino ... "))
    if ( validacionSigno(valor) == True ):
        if ( valor[0] == '+' ):
            newValor = valor [1:]
            print ("El numero que me diste fue: " , newValor , " :P \nChao chao.\n")
            break
        else:
            print ("El numero que me diste fue: " , valor , " :P \nChao chao.\n")
            break
    else:
        print ("No me diste ningun numero :(")
