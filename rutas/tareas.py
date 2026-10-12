from fastapi import APIRouter, HTTPException
from esquemas import TareaNueva, TareaGuardada
from almacen import cargar_datos, guardar_datos

router = APIRouter(prefix="/tareas", tags=["tareas"])

@router.get("/")
def ver_todas():
    return cargar_datos()

@router.get("/{id_tarea}")
def ver_una(id_tarea: int):
    datos = cargar_datos()
    for d in datos:
        if d["id_tarea"] == id_tarea:
            return d
    raise HTTPException(status_code=404, detail="tarea no encontrada")

@router.post("/")
def agre_tarea(tarea: TareaNueva):
    datos = cargar_datos()
    nuevo_id = 1 if len(datos) == 0 else datos[-1]["id_tarea"] + 1
    
    nueva = {
        "id_tarea": nuevo_id,
        "titulo": tarea.titulo,
        "desc": tarea.desc,
        "term": False
    }
    
    datos.append(nueva)
    guardar_datos(datos)
    return nueva

@router.put("/{id_tarea}")
def act_estado(id_tarea: int):
    datos = cargar_datos()
    modificado = False
    
    for d in datos:
        if d["id_tarea"] == id_tarea:
            d["term"] = True
            modificado = True
            break
            
    if not modificado:
        raise HTTPException(status_code=404, detail="no se encontro esa tarea")
        
    guardar_datos(datos)
    return {"mensaje": "tarea marcada como terminada"}

@router.delete("/{id_tarea}")
def borrar_tarea(id_tarea: int):
    datos = cargar_datos()
    # filtramos la lista para quedarnos con todas menos la que queremos borrar
    datos_nuevos = [d for d in datos if d["id_tarea"] != id_tarea]
    
    if len(datos) == len(datos_nuevos):
        raise HTTPException(status_code=404, detail="tarea no encontrada para borrar")
        
    guardar_datos(datos_nuevos)
    return {"mensaje": "tarea eliminada exitosamente"}
