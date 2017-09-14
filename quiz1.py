secreta= "orion"
opc=1



while opc <4:
    print("intento "+str(opc)+" de 3")
    adivina=input("adivina la palabra: ")
    if adivina.lower()==secreta:
        print("lo lograste")
        break
    else:print("no es la palabra correcta intentalo de nuevo")
    print( "\n Pista: Es una costelacion")
    opc+=1




