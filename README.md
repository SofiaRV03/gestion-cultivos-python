# Sistema de Gestión de Cultivos 

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![PyQt5](https://img.shields.io/badge/UI-PyQt5-green.svg)
![SQLite](https://img.shields.io/badge/Database-SQLite3-lightgrey.svg)
![Architecture](https://img.shields.io/badge/Architecture-MVC-orange.svg)

##  Descripción
Este es un sistema integral de escritorio diseñado para la administración y monitoreo de cultivos (árboles). Permite centralizar la información operativa, técnica y humana de una finca productiva, facilitando la toma de decisiones basada en datos históricos de salud y producción.

Desarrollado bajo el patrón de diseño **MVC (Modelo-Vista-Controlador)**, el sistema garantiza una separación clara de responsabilidades, facilitando su mantenimiento y escalabilidad.

---

##  Características Principales

###  Gestión de Inventario
- **Árboles:** Registro de siembra y seguimiento individual de cada árbol por ID.
- **Top 10 de Producción:** Reporte dinámico que identifica los árboles más productivos del cultivo.

###  Control Fitosanitario y Nutricional
- **Diagnósticos:** Registro de enfermedades detectadas en los árboles.
- **Fumigaciones:** Seguimiento de aplicaciones para el control de plagas y enfermedades.
- **Nutrición:** Registro de planes de fertilización y suplementos nutricionales.

###  Producción y Cosecha
- **Recolectas:** Registro detallado de la producción obtenida por árbol y fecha.

###  Gestión Humana
- **Trabajadores:** Administración de la base de datos de empleados (Nombre, Teléfono, EPS, ARL).

---

##  Arquitectura del Software           

El proyecto sigue una estructura robusta basada en:
- **Modelo:** 
  - **DAO (Data Access Object):** Encapsula la lógica de acceso a datos SQL.
  - **VO (Value Object):** Define las estructuras de datos para el transporte de información.
- **Vista:** Implementada con **PyQt5**, ofreciendo una interfaz gráfica fluida y adaptable.
- **Controlador:** Gestiona el flujo de datos entre la UI y la base de datos.

### Estructura de Directorios
```bash
├── controlador/    # Lógica de control de la aplicación
├── db/             # Base de datos SQLite y scripts de conexión
├── diagramas/      # Documentación visual (ER y Relacional)
├── modelo/         
│   ├── dao/        # Capa de persistencia
│   └── vo/         # Clases de entidad
├── vista/          # Definición de la interfaz gráfica
└── main.py         # Punto de entrada del sistema
```

---

##  Instalación y Configuración

### Requisitos Previos
- Python 3.x instalado.
- Entorno virtual (Recomendado).

### Pasos para Ejecutar
1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/gestion-cultivos-python.git
   cd gestion-cultivos-python
   ```

2. **Instalar dependencias:**
   ```bash
   pip install PyQt5
   ```

3. **Ejecutar la aplicación:**
   ```bash
   python main.py gui
   ```

---

##  Base de Datos
El sistema utiliza **SQLite3** por su portabilidad y eficiencia. El modelo incluye entidades relacionadas para:
- Árboles y Enfermedades (Relación N:M).
- Trabajadores y labores de campo.
- Registros históricos de producción y sanidad.

---

##  Contribuciones
Este proyecto fue desarrollado por:
- Sofia Restrepo Villegas
