from dataclasses import dataclass

@dataclass
class NutricionVO:
    id_nutricion: int=-1
    fecha_nutricion: str="Sin asignar"
    mezcla_nutricion: str="Sin asignar"
    id_trabajador: int=-1
    id_arbol: int=-1