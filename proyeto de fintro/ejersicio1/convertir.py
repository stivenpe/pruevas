def pesos_dolares(pesos):
    return pesos / 3944

def pesos_euros(pesos):
    return pesos / 4279

def pesos_yen(pesos):
    return pesos / 26.30
 
def euros_pesos(euros):
    return  euros / 4279

def convertir():
    print("1: ngrese el covertir pesos a dolares :")
    print("2: ingrese el convertir pesos a euros :")
    print("3: ingrese el  convertir pesos a yen :")
    print("4: ingrese el convertir euros a pesos ")
    
    opciones = int(input("ingrese opciones que desea :"))

    if opciones ==1:
        pesos = float(input("ingrese el convertir pesos a dolares :"))
        print('el convertir ','en dolar es :',pesos_dolares(pesos))

    elif opciones ==2:
        pesos = float("ingrese el convertir pesos a euros :")
        print("el convertir","en euros es",pesos_euros(pesos))

    elif opciones ==3:
        pesos = float(input("ingrese el convertir pesos a yen :"))
        print("el convertir","en yen es",pesos_yen(pesos)) 

    elif opciones ==4:
        euros = float(input("ingrese el euros a pesos :"))
        print("el convertir","el pesos es",euros_pesos(euros))       


if __name__ == "__main__":
    convertir()