import pandas as pd
import numpy as np

def letonia(valor):
    return "leto"

def arreglarGenero(gen):
    if (gen == "No identificado" ):
        return "Tatan"
    if(gen == "No aplica"):
        return "Persona juridica"
    return gen

def pepe():
    return 5

def arreglarPaisNacimiento(pais):
    if(pais == "No aplica"):
        return "Persona juridica"
    return pais

hola = pepe
csv = pd.read_csv("./embargosAutos.csv")
DataTypes = list(csv.columns)
print(DataTypes)
csv.dropna(inplace=False)

#for i in DataTypes:
#    csv[i] = csv[i].apply(letonia)

csv["titular_genero"] = csv["titular_genero"].apply(arreglarGenero)
print(csv , " ", csv["titular_genero"])
print("--------------------------------------------------------------------")
csv["titular_pais_nacimiento"] = csv["titular_pais_nacimiento"].apply(arreglarPaisNacimiento)
print(csv , " ", csv["titular_pais_nacimiento"])

print(hola)