from dataclasses import dataclass

@dataclass
class Arbol_EnfermedadVO:
    id_Arbol_Enfermedad:int =-1
    id_arbol: int=-1
    id_enfermedad: int=-1
    fecha_diagnostico: str="Sin asignar"


