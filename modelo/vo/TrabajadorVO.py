from dataclasses import dataclass

@dataclass
class TrabajadorVO:
    id_trabajador: int
    nombre: str
    telefono: str
    EPS: str
    ARL: str
    fecha_creacion: str