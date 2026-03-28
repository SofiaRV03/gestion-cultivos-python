from dataclasses import dataclass

@dataclass
class FumigacionVO:
    id_fumigacion: int=-1
    fecha_fumigacion: str="Sin asignar"
    mezcla_fumigacion: str="Sin asignar"
    id_trabajador: int=-1
    id_arbol: int=-1