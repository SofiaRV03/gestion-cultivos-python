from dataclasses import dataclass

@dataclass
class RecolectaVO:
    id_recolecta: int=-1
    fecha_recolecta: str="Sin asignar"
    calidad: str="Sin asignar"
    peso: float=-1
    id_trabajador: int=-1
    id_arbol: int=-1
    id_produccion: int=-1