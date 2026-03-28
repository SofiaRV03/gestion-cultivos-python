from dataclasses import dataclass

@dataclass
class TopArbolesVO:
    id_arbol: int=-1
    fecha_siembra: str="Sin asignar"
    calidad: str="Sin asignar"
    total_por_calidad: float=-1
    total_general: float=-1
    fecha_referencia: str="Sin asignar"