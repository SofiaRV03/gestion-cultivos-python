from dataclasses import dataclass

@dataclass
class EnfermedadVO:
    id_enfermedad: int=-1
    nombre_enfermedad: str="Sin asignar"
    descripcion: str="Sin asignar"
    causa: str="Sin asignar"
    tratamiento: str="Sin asignar"