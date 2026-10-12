import json
import os

arch_datos = "datos.json"

def cargar_datos():
    if not os.path.exists(arch_datos):
        return []
    with open(arch_datos, "r") as arch:
        return json.load(arch)

def guardar_datos(lista_dicc):
    with open(arch_datos, "w") as arch:
        json.dump(lista_dicc, arch, indent=2)
      
