from dataclasses import dataclass

@dataclass
class DiagnosticoVO:
    id_Arbol_Enfermedad:int=-1
    id_arbol: int=-1
    id_enfermedad: int=-1
    nombre_enfermedad: str="Sin asignar"
    descripcion: str="Sin asignar"
    causa: str="Sin asignar"
    tratamiento: str="Sin asignar"
    fecha_diagnostico: str="Sin asignar"