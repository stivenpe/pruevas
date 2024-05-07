
import os
import json
import funciones.produtos as cf
import funciones.globale as fg
import modules.corefiles as mc
def tienda():

    id = input ("ingrese el id del produto :")
    nombre = input ("ingrese el nombre del produto :")
    valorUnitario = input ("ingrese el valor unitario del produto :")
    stockmin = input ("ingrse el stockmin del produto :")
    stockmax = input ("ingrse el stockmax del produto :")

    tienda = {  
        id : "id",
        nombre : "nombre",
        valorUnitario : "valorUnitario ",
        stockmin : "stockmin",
        stockmax : " stockmax "
    }


if __name__ == "__main__":
   tienda()

mc.addData("data",id, tienda)