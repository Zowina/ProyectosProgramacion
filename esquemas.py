from pydantic import BaseModel
from typing import Optional

class TareaNueva(BaseModel):
    titulo: str
    desc: Optional[str] = ""

class TareaGuardada(TareaNueva):
    id_tarea: int
    term: bool = False
