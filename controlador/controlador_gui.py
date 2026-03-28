# from modelo import queries,dml
from vista import vista_gui
from modelo.vo.ArbolVO import ArbolVO
from modelo.dao.ArbolDAO import ArbolDAO
from modelo.vo.TrabajadorVO import TrabajadorVO
from modelo.dao.TrabajadorDAO import TrabajadorDAO
from modelo.dao.FumigacionDAO import FumigacionDAO
from modelo.vo.FumigacionVO import FumigacionVO
from modelo.vo.NutricionVO import NutricionVO
from modelo.dao.NutricionDAO import NutricionDAO
from modelo.vo.RecolectaVO import RecolectaVO
from modelo.dao.RecolectaDAO import RecolectaDAO
from modelo.vo.DiagnosticoVO import DiagnosticoVO
from modelo.dao.DiagnosticoDAO import DiagnosticoDAO
from modelo.vo.EnfermedadVO import EnfermedadVO
from modelo.dao.EnfermedadDAO import EnfermedadDAO
from modelo.vo.Arbol_EnfermedadVO import  Arbol_EnfermedadVO
from modelo.dao.Arbol_EnfermedadDAO import Arbol_EnfermedadDAO
from modelo.vo.TopArbolesVO import TopArbolesVO
from modelo.dao.TopArbolesDAO import TopArbolesDAO




from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
import sys
import pprint as pp


class ControladorGUI:
    
    def __init__(self):
        
        self.app = QApplication(sys.argv)
        
        self.ventana_principal = vista_gui.VentanaPrincipal()

        self.formulario_trabajador=vista_gui.FormularioNuevoTrabajador()

        self.formulario_arbol=vista_gui.FormularioNuevoArbol()

        self.formulario_modificar_trabajador=vista_gui.FormularioModificarTrabajador()

        self.formulario_modificar_arbol=vista_gui.FormularioModificarArbol()

        self.formulario_fumigacion=vista_gui.FormularioNuevaFumigacion()

        self.formulario_modificar_fumigacion=vista_gui.FormularioModificarFumigacion()

        self.formulario_nutricion=vista_gui.FormularioNuevaNutricion()

        self.formulario_modificar_nutricion=vista_gui.FormularioModificarNutricion()

        self.formulario_recolecta=vista_gui.FormularioNuevaRecolecta()

        self.formulario_modificar_recolecta=vista_gui.FormularioModificarRecolecta()

        self.formulario_recolecta=vista_gui.FormularioNuevaRecolecta()

        self.formulario_diagnostico=vista_gui.FormularioNuevoDiagnostico()

        self.formulario_modificar_diagnostico=vista_gui.FormularioModificarDiagnostico()
        
        self.ventana_enfermedades=vista_gui.VentanaEnfermedades()
        
        self.formulario_enfermedad=vista_gui.FormularioNuevaEnfermedad()

        self.formulario_modificar_enfermedad=vista_gui.FormularioModificarEnfermedad()
        
        self.ventana_top_10=vista_gui.FormularioTop10()


        
        self._setup_handlers()        
        
    
    def _setup_handlers(self):
        
        def handler_llenar_tabla_arboles():
            listado_arboles = ArbolDAO().get_all()
            self.ventana_principal.w['tabla_arbol'].setColumnCount(2)
            self.ventana_principal.w['tabla_arbol'].setHorizontalHeaderLabels(['id_arbol','fecha_siembra',])
            self.ventana_principal.w['tabla_arbol'].setRowCount(len(listado_arboles))
            self.ventana_principal.w['tabla_arbol'].verticalHeader().setVisible(False)
            for indice,arbol in enumerate(listado_arboles):
                self.ventana_principal.w['tabla_arbol'].setItem(indice,0,QTableWidgetItem(str(arbol.id_arbol)))
                self.ventana_principal.w['tabla_arbol'].setItem(indice,1,QTableWidgetItem(arbol.fecha_siembra))

        def handler_llenar_tabla_trabajadores():
            listado_trabajadores = TrabajadorDAO().get_all()
            self.ventana_principal.w['tabla_trabajador'].setColumnCount(6)
            self.ventana_principal.w['tabla_trabajador'].setHorizontalHeaderLabels(['id_trabajador','nombre','telefono','EPS','ARL','fecha_creacion'])
            self.ventana_principal.w['tabla_trabajador'].setRowCount(len(listado_trabajadores))
            self.ventana_principal.w['tabla_trabajador'].verticalHeader().setVisible(False)
            for indice,trabajador in enumerate(listado_trabajadores):
                self.ventana_principal.w['tabla_trabajador'].setItem(indice,0,QTableWidgetItem(str(trabajador.id_trabajador)))
                self.ventana_principal.w['tabla_trabajador'].setItem(indice,1,QTableWidgetItem(trabajador.nombre))
                self.ventana_principal.w['tabla_trabajador'].setItem(indice,2,QTableWidgetItem(trabajador.telefono))
                self.ventana_principal.w['tabla_trabajador'].setItem(indice,3,QTableWidgetItem(trabajador.EPS))
                self.ventana_principal.w['tabla_trabajador'].setItem(indice,4,QTableWidgetItem(trabajador.ARL))
                self.ventana_principal.w['tabla_trabajador'].setItem(indice,5,QTableWidgetItem(trabajador.fecha_creacion))

        def handler_llenar_tabla_fumigaciones():
            listado_fumigaciones = FumigacionDAO().get_all()
            self.ventana_principal.w['tabla_fumigacion'].setColumnCount(5)
            self.ventana_principal.w['tabla_fumigacion'].setHorizontalHeaderLabels(['id_fumigacion','fecha_fumigacion','mezcla_fumigacion','id_trabajador','id_arbol'])
            self.ventana_principal.w['tabla_fumigacion'].setRowCount(len(listado_fumigaciones))
            self.ventana_principal.w['tabla_fumigacion'].verticalHeader().setVisible(False)
            for indice,fumigacion in enumerate(listado_fumigaciones):
                self.ventana_principal.w['tabla_fumigacion'].setItem(indice,0,QTableWidgetItem(str(fumigacion.id_fumigacion)))
                self.ventana_principal.w['tabla_fumigacion'].setItem(indice,1,QTableWidgetItem(fumigacion.fecha_fumigacion))
                self.ventana_principal.w['tabla_fumigacion'].setItem(indice,2,QTableWidgetItem(fumigacion.mezcla_fumigacion))
                self.ventana_principal.w['tabla_fumigacion'].setItem(indice,3,QTableWidgetItem(str(fumigacion.id_trabajador)))
                self.ventana_principal.w['tabla_fumigacion'].setItem(indice,4,QTableWidgetItem(str(fumigacion.id_arbol)))

        def handler_llenar_tabla_nutriciones():
            listado_nutriciones = NutricionDAO().get_all()
            self.ventana_principal.w['tabla_nutricion'].setColumnCount(5)
            self.ventana_principal.w['tabla_nutricion'].setHorizontalHeaderLabels(['id_nutricion','fecha_nutricion','mezcla_nutricion','id_trabajador','id_arbol'])
            self.ventana_principal.w['tabla_nutricion'].setRowCount(len(listado_nutriciones))
            self.ventana_principal.w['tabla_nutricion'].verticalHeader().setVisible(False)
            for indice,nutricion in enumerate(listado_nutriciones):
                self.ventana_principal.w['tabla_nutricion'].setItem(indice,0,QTableWidgetItem(str(nutricion.id_nutricion)))
                self.ventana_principal.w['tabla_nutricion'].setItem(indice,1,QTableWidgetItem(nutricion.fecha_nutricion))
                self.ventana_principal.w['tabla_nutricion'].setItem(indice,2,QTableWidgetItem(nutricion.mezcla_nutricion))
                self.ventana_principal.w['tabla_nutricion'].setItem(indice,3,QTableWidgetItem(str(nutricion.id_trabajador)))
                self.ventana_principal.w['tabla_nutricion'].setItem(indice,4,QTableWidgetItem(str(nutricion.id_arbol)))

        def handler_llenar_tabla_recolectas():
            listado_recolectas = RecolectaDAO().get_all()
            self.ventana_principal.w['tabla_recolecta'].setColumnCount(7)
            self.ventana_principal.w['tabla_recolecta'].setHorizontalHeaderLabels(['id_recolecta','fecha_recolecta','calidad','peso','id_trabajador','id_arbol','id_produccion'])
            self.ventana_principal.w['tabla_recolecta'].setRowCount(len(listado_recolectas))
            self.ventana_principal.w['tabla_recolecta'].verticalHeader().setVisible(False)
            for indice,recolecta in enumerate(listado_recolectas):
                self.ventana_principal.w['tabla_recolecta'].setItem(indice,0,QTableWidgetItem(str(recolecta.id_recolecta)))
                self.ventana_principal.w['tabla_recolecta'].setItem(indice,1,QTableWidgetItem(recolecta.fecha_recolecta))
                self.ventana_principal.w['tabla_recolecta'].setItem(indice,2,QTableWidgetItem(recolecta.calidad))
                self.ventana_principal.w['tabla_recolecta'].setItem(indice,3,QTableWidgetItem(str(recolecta.peso)))
                self.ventana_principal.w['tabla_recolecta'].setItem(indice,4,QTableWidgetItem(str(recolecta.id_trabajador)))
                self.ventana_principal.w['tabla_recolecta'].setItem(indice,5,QTableWidgetItem(str(recolecta.id_arbol)))
                self.ventana_principal.w['tabla_recolecta'].setItem(indice,6,QTableWidgetItem(str(recolecta.id_produccion)))







        def handler_llenar_tabla_enfermedades():
            listado_enfermedades = EnfermedadDAO().get_all()
            self.formulario_diagnostico.w['tabla_enfermedades'].setColumnCount(5)
            self.formulario_diagnostico.w['tabla_enfermedades'].setHorizontalHeaderLabels(['id_enfermedad','nombre','descripcion','causa','tratamiento'])
            self.formulario_diagnostico.w['tabla_enfermedades'].setRowCount(len(listado_enfermedades))
            self.formulario_diagnostico.w['tabla_enfermedades'].verticalHeader().setVisible(False)
            for indice, enfermedad in enumerate(listado_enfermedades):
                self.formulario_diagnostico.w['tabla_enfermedades'].setItem(indice,0,QTableWidgetItem(str(enfermedad.id_enfermedad)))
                self.formulario_diagnostico.w['tabla_enfermedades'].setItem(indice,1,QTableWidgetItem(enfermedad.nombre_enfermedad))
                self.formulario_diagnostico.w['tabla_enfermedades'].setItem(indice,2,QTableWidgetItem(enfermedad.descripcion))
                self.formulario_diagnostico.w['tabla_enfermedades'].setItem(indice,3,QTableWidgetItem(enfermedad.causa))
                self.formulario_diagnostico.w['tabla_enfermedades'].setItem(indice,4,QTableWidgetItem(enfermedad.tratamiento))


        def handler_tabla_consulta_enfermedades():
            listado_enfermedades = EnfermedadDAO().get_all()
            self.ventana_enfermedades.w['tabla_enfermedades'].setColumnCount(5)
            self.ventana_enfermedades.w['tabla_enfermedades'].setHorizontalHeaderLabels(['id_enfermedad','nombre','descripcion','causa','tratamiento'])
            self.ventana_enfermedades.w['tabla_enfermedades'].setRowCount(len(listado_enfermedades))
            self.ventana_enfermedades.w['tabla_enfermedades'].verticalHeader().setVisible(False)
            for indice, enfermedad in enumerate(listado_enfermedades):
                self.ventana_enfermedades.w['tabla_enfermedades'].setItem(indice,0,QTableWidgetItem(str(enfermedad.id_enfermedad)))
                self.ventana_enfermedades.w['tabla_enfermedades'].setItem(indice,1,QTableWidgetItem(enfermedad.nombre_enfermedad))
                self.ventana_enfermedades.w['tabla_enfermedades'].setItem(indice,2,QTableWidgetItem(enfermedad.descripcion))
                self.ventana_enfermedades.w['tabla_enfermedades'].setItem(indice,3,QTableWidgetItem(enfermedad.causa))
                self.ventana_enfermedades.w['tabla_enfermedades'].setItem(indice,4,QTableWidgetItem(enfermedad.tratamiento))


        def handler_llenar_tabla_diagnosticos():
            listado_diagnosticos = DiagnosticoDAO().get_all()
            self.ventana_principal.w['tabla_diagnostico'].setColumnCount(8) 
            self.ventana_principal.w['tabla_diagnostico'].setHorizontalHeaderLabels([
                'id_Arbol_Enfermedad',
                'id_arbol','id_enfermedad', 'nombre_enfermedad', 
                'descripcion', 'causa', 'tratamiento', 'fecha_diagnostico'
            ])
            self.ventana_principal.w['tabla_diagnostico'].setRowCount(len(listado_diagnosticos))
            self.ventana_principal.w['tabla_diagnostico'].verticalHeader().setVisible(False)
            
            for indice, diagnostico in enumerate(listado_diagnosticos):
                self.ventana_principal.w['tabla_diagnostico'].setItem(indice,0,QTableWidgetItem(str(diagnostico.id_Arbol_Enfermedad)))
                self.ventana_principal.w['tabla_diagnostico'].setItem(indice,1,QTableWidgetItem(str(diagnostico.id_arbol)))
                self.ventana_principal.w['tabla_diagnostico'].setItem(indice,2,QTableWidgetItem(str(diagnostico.id_enfermedad)))
                self.ventana_principal.w['tabla_diagnostico'].setItem(indice,3,QTableWidgetItem(diagnostico.nombre_enfermedad))
                self.ventana_principal.w['tabla_diagnostico'].setItem(indice,4,QTableWidgetItem(diagnostico.descripcion))
                self.ventana_principal.w['tabla_diagnostico'].setItem(indice,5,QTableWidgetItem(diagnostico.causa))
                self.ventana_principal.w['tabla_diagnostico'].setItem(indice,6,QTableWidgetItem(diagnostico.tratamiento))
                self.ventana_principal.w['tabla_diagnostico'].setItem(indice,7  ,QTableWidgetItem(diagnostico.fecha_diagnostico))


        def handler_mostrar_fumigaciones_arbol():
            fila = self.ventana_principal.w['tabla_arbol'].currentRow()
            id_arbol = int(self.ventana_principal.w['tabla_arbol'].item(fila, 0).text())
            arbol = ArbolVO(id_arbol=id_arbol, fecha_siembra=None)
            listado_fumigaciones = FumigacionDAO().mostrar_fumigaciones_arbol(arbol)
        
            self.formulario_modificar_arbol.w['tabla_fumigaciones'].setColumnCount(5)
            self.formulario_modificar_arbol.w['tabla_fumigaciones'].setHorizontalHeaderLabels(['id_fumigacion','fecha_fumigacion','mezcla_fumigacion','id_trabajador','id_arbol'])
            self.formulario_modificar_arbol.w['tabla_fumigaciones'].setRowCount(len(listado_fumigaciones))
            self.formulario_modificar_arbol.w['tabla_fumigaciones'].verticalHeader().setVisible(False)
            for indice,fumigacion in enumerate(listado_fumigaciones):
                self.formulario_modificar_arbol.w['tabla_fumigaciones'].setItem(indice,0,QTableWidgetItem(str(fumigacion.id_fumigacion)))
                self.formulario_modificar_arbol.w['tabla_fumigaciones'].setItem(indice,1,QTableWidgetItem(fumigacion.fecha_fumigacion))
                self.formulario_modificar_arbol.w['tabla_fumigaciones'].setItem(indice,2,QTableWidgetItem(fumigacion.mezcla_fumigacion))
                self.formulario_modificar_arbol.w['tabla_fumigaciones'].setItem(indice,3,QTableWidgetItem(str(fumigacion.id_trabajador)))
                self.formulario_modificar_arbol.w['tabla_fumigaciones'].setItem(indice,4,QTableWidgetItem(str(fumigacion.id_arbol)))

        def handler_mostrar_nutriciones_arbol():
            fila = self.ventana_principal.w['tabla_arbol'].currentRow()
            id_arbol = int(self.ventana_principal.w['tabla_arbol'].item(fila, 0).text())
            arbol = ArbolVO(id_arbol=id_arbol, fecha_siembra=None)
            listado_nutriciones = NutricionDAO().mostrar_nutriciones_arbol(arbol)
        
            self.formulario_modificar_arbol.w['tabla_nutriciones'].setColumnCount(5)
            self.formulario_modificar_arbol.w['tabla_nutriciones'].setHorizontalHeaderLabels(['id_nutricion','fecha_nutricion','mezcla_nutricion','id_trabajador','id_arbol'])
            self.formulario_modificar_arbol.w['tabla_nutriciones'].setRowCount(len(listado_nutriciones))
            self.formulario_modificar_arbol.w['tabla_nutriciones'].verticalHeader().setVisible(False)
            for indice,nutricion in enumerate(listado_nutriciones):
                self.formulario_modificar_arbol.w['tabla_nutriciones'].setItem(indice,0,QTableWidgetItem(str(nutricion.id_nutricion)))
                self.formulario_modificar_arbol.w['tabla_nutriciones'].setItem(indice,1,QTableWidgetItem(nutricion.fecha_nutricion))
                self.formulario_modificar_arbol.w['tabla_nutriciones'].setItem(indice,2,QTableWidgetItem(nutricion.mezcla_nutricion))
                self.formulario_modificar_arbol.w['tabla_nutriciones'].setItem(indice,3,QTableWidgetItem(str(nutricion.id_trabajador)))
                self.formulario_modificar_arbol.w['tabla_nutriciones'].setItem(indice,4,QTableWidgetItem(str(nutricion.id_arbol)))

        def handler_mostrar_recolectas_arbol():
            fila = self.ventana_principal.w['tabla_arbol'].currentRow()
            id_arbol = int(self.ventana_principal.w['tabla_arbol'].item(fila, 0).text())
            arbol = ArbolVO(id_arbol=id_arbol, fecha_siembra=None)
            listado_recolectas = RecolectaDAO().mostrar_recolectas_arbol(arbol)
        
            self.formulario_modificar_arbol.w['tabla_recolectas'].setColumnCount(7)
            self.formulario_modificar_arbol.w['tabla_recolectas'].setHorizontalHeaderLabels(['id_recolecta','fecha_recolecta','calidad','peso','id_trabajador','id_arbol','id_produccion'])
            self.formulario_modificar_arbol.w['tabla_recolectas'].setRowCount(len(listado_recolectas))
            self.formulario_modificar_arbol.w['tabla_recolectas'].verticalHeader().setVisible(False)
            for indice,recolecta in enumerate(listado_recolectas):
                self.formulario_modificar_arbol.w['tabla_recolectas'].setItem(indice,0,QTableWidgetItem(str(recolecta.id_recolecta)))
                self.formulario_modificar_arbol.w['tabla_recolectas'].setItem(indice,1,QTableWidgetItem(recolecta.fecha_recolecta))
                self.formulario_modificar_arbol.w['tabla_recolectas'].setItem(indice,2,QTableWidgetItem(recolecta.calidad))
                self.formulario_modificar_arbol.w['tabla_recolectas'].setItem(indice,3,QTableWidgetItem(str(recolecta.peso)))
                self.formulario_modificar_arbol.w['tabla_recolectas'].setItem(indice,4,QTableWidgetItem(str(recolecta.id_trabajador)))
                self.formulario_modificar_arbol.w['tabla_recolectas'].setItem(indice,5,QTableWidgetItem(str(recolecta.id_arbol)))
                self.formulario_modificar_arbol.w['tabla_recolectas'].setItem(indice,6,QTableWidgetItem(str(recolecta.id_produccion)))

        def handler_mostrar_fumigaciones_trabajador():
            fila = self.ventana_principal.w['tabla_trabajador'].currentRow()
            id_trabajador = int(self.ventana_principal.w['tabla_trabajador'].item(fila, 0).text())
            trabajador = TrabajadorVO(id_trabajador=id_trabajador, nombre=None, telefono=None, EPS=None, ARL=None, fecha_creacion=None)
            listado_fumigaciones = FumigacionDAO().mostrar_fumigaciones_trabajador(trabajador)
        
            self.formulario_modificar_trabajador.w['tabla_fumigaciones'].setColumnCount(5)
            self.formulario_modificar_trabajador.w['tabla_fumigaciones'].setHorizontalHeaderLabels(['id_fumigacion','fecha_fumigacion','mezcla_fumigacion','id_trabajador','id_arbol'])
            self.formulario_modificar_trabajador.w['tabla_fumigaciones'].setRowCount(len(listado_fumigaciones))
            self.formulario_modificar_trabajador.w['tabla_fumigaciones'].verticalHeader().setVisible(False)
            for indice,fumigacion in enumerate(listado_fumigaciones):
                self.formulario_modificar_trabajador.w['tabla_fumigaciones'].setItem(indice,0,QTableWidgetItem(str(fumigacion.id_fumigacion)))
                self.formulario_modificar_trabajador.w['tabla_fumigaciones'].setItem(indice,1,QTableWidgetItem(fumigacion.fecha_fumigacion))
                self.formulario_modificar_trabajador.w['tabla_fumigaciones'].setItem(indice,2,QTableWidgetItem(fumigacion.mezcla_fumigacion))
                self.formulario_modificar_trabajador.w['tabla_fumigaciones'].setItem(indice,3,QTableWidgetItem(str(fumigacion.id_trabajador)))
                self.formulario_modificar_trabajador.w['tabla_fumigaciones'].setItem(indice,4,QTableWidgetItem(str(fumigacion.id_arbol)))

        def handler_mostrar_nutriciones_trabajador():
            fila = self.ventana_principal.w['tabla_trabajador'].currentRow()
            id_trabajador = int(self.ventana_principal.w['tabla_trabajador'].item(fila, 0).text())
            trabajador = TrabajadorVO(id_trabajador=id_trabajador, nombre=None, telefono=None, EPS=None, ARL=None, fecha_creacion=None)
            listado_nutriciones = NutricionDAO().mostrar_nutriciones_trabajador(trabajador)
        
            self.formulario_modificar_trabajador.w['tabla_nutriciones'].setColumnCount(5)
            self.formulario_modificar_trabajador.w['tabla_nutriciones'].setHorizontalHeaderLabels(['id_nutricion','fecha_nutricion','mezcla_nutricion','id_trabajador','id_arbol'])
            self.formulario_modificar_trabajador.w['tabla_nutriciones'].setRowCount(len(listado_nutriciones))
            self.formulario_modificar_trabajador.w['tabla_nutriciones'].verticalHeader().setVisible(False)
            for indice,nutricion in enumerate(listado_nutriciones):
                self.formulario_modificar_trabajador.w['tabla_nutriciones'].setItem(indice,0,QTableWidgetItem(str(nutricion.id_nutricion)))
                self.formulario_modificar_trabajador.w['tabla_nutriciones'].setItem(indice,1,QTableWidgetItem(nutricion.fecha_nutricion))
                self.formulario_modificar_trabajador.w['tabla_nutriciones'].setItem(indice,2,QTableWidgetItem(nutricion.mezcla_nutricion))
                self.formulario_modificar_trabajador.w['tabla_nutriciones'].setItem(indice,3,QTableWidgetItem(str(nutricion.id_trabajador)))
                self.formulario_modificar_trabajador.w['tabla_nutriciones'].setItem(indice,4,QTableWidgetItem(str(nutricion.id_arbol)))

        def handler_mostrar_recolectas_trabajador():
            fila = self.ventana_principal.w['tabla_trabajador'].currentRow()
            id_trabajador = int(self.ventana_principal.w['tabla_trabajador'].item(fila, 0).text())
            trabajador = TrabajadorVO(id_trabajador=id_trabajador, nombre=None, telefono=None, EPS=None, ARL=None, fecha_creacion=None)
            listado_recolectas = RecolectaDAO().mostrar_recolectas_trabajador(trabajador)
        
            self.formulario_modificar_trabajador.w['tabla_recolectas'].setColumnCount(7)
            self.formulario_modificar_trabajador.w['tabla_recolectas'].setHorizontalHeaderLabels(['id_recolecta','fecha_recolecta','calidad','peso','id_trabajador','id_arbol','id_produccion'])
            self.formulario_modificar_trabajador.w['tabla_recolectas'].setRowCount(len(listado_recolectas))
            self.formulario_modificar_trabajador.w['tabla_recolectas'].verticalHeader().setVisible(False)
            for indice,recolecta in enumerate(listado_recolectas):
                self.formulario_modificar_trabajador.w['tabla_recolectas'].setItem(indice,0,QTableWidgetItem(str(recolecta.id_recolecta)))
                self.formulario_modificar_trabajador.w['tabla_recolectas'].setItem(indice,1,QTableWidgetItem(recolecta.fecha_recolecta))
                self.formulario_modificar_trabajador.w['tabla_recolectas'].setItem(indice,2,QTableWidgetItem(recolecta.calidad))
                self.formulario_modificar_trabajador.w['tabla_recolectas'].setItem(indice,3,QTableWidgetItem(str(recolecta.peso)))
                self.formulario_modificar_trabajador.w['tabla_recolectas'].setItem(indice,4,QTableWidgetItem(str(recolecta.id_trabajador)))
                self.formulario_modificar_trabajador.w['tabla_recolectas'].setItem(indice,5,QTableWidgetItem(str(recolecta.id_arbol)))
                self.formulario_modificar_trabajador.w['tabla_recolectas'].setItem(indice,6,QTableWidgetItem(str(recolecta.id_produccion)))


        def handler_mostrar_diagnostico_arbol():
            fila = self.ventana_principal.w['tabla_arbol'].currentRow()
            id_arbol = int(self.ventana_principal.w['tabla_arbol'].item(fila, 0).text())
            arbol = ArbolVO(id_arbol=id_arbol, fecha_siembra=None)
            listado_diagnosticos = DiagnosticoDAO().mostrar_diagnostico_id_arbol(arbol)
        
            self.formulario_modificar_arbol.w['tabla_diagnosticos'].setColumnCount(7)
            self.formulario_modificar_arbol.w['tabla_diagnosticos'].setHorizontalHeaderLabels(['id_arbol','id_enfermedad','nombre_enfermedad','descripcion','causa','tratamiento','fecha_diagnostico'])
            self.formulario_modificar_arbol.w['tabla_diagnosticos'].setRowCount(len(listado_diagnosticos))
            self.formulario_modificar_arbol.w['tabla_diagnosticos'].verticalHeader().setVisible(False)
            for indice,diagnostico in enumerate(listado_diagnosticos):
                self.formulario_modificar_arbol.w['tabla_diagnosticos'].setItem(indice,0,QTableWidgetItem(str(diagnostico.id_arbol)))
                self.formulario_modificar_arbol.w['tabla_diagnosticos'].setItem(indice,1,QTableWidgetItem(str(diagnostico.id_enfermedad)))
                self.formulario_modificar_arbol.w['tabla_diagnosticos'].setItem(indice,2,QTableWidgetItem(diagnostico.nombre_enfermedad))
                self.formulario_modificar_arbol.w['tabla_diagnosticos'].setItem(indice,3,QTableWidgetItem(diagnostico.descripcion))
                self.formulario_modificar_arbol.w['tabla_diagnosticos'].setItem(indice,4,QTableWidgetItem(diagnostico.causa))
                self.formulario_modificar_arbol.w['tabla_diagnosticos'].setItem(indice,5,QTableWidgetItem(diagnostico.tratamiento))
                self.formulario_modificar_arbol.w['tabla_diagnosticos'].setItem(indice,6,QTableWidgetItem(diagnostico.fecha_diagnostico))

        def handler_nueva_enfermedad():
            self.formulario_enfermedad.limpiar_campos()
            self.formulario_enfermedad.show()

        def handler_formulario_guardar_enfermedad():
            
            nueva_enfermedad = EnfermedadVO(nombre_enfermedad=self.formulario_enfermedad.w['input_nombre_enfermedad'].text(), descripcion=self.formulario_enfermedad.w['input_descripcion'].text(),causa=self.formulario_enfermedad.w['input_causa'].text(),tratamiento=self.formulario_enfermedad.w['input_tratamiento'].text())
            
            EnfermedadDAO().adicionar_enfermedad(enfermedad = nueva_enfermedad)


        def handler_nuevo_trabajador():
            self.formulario_trabajador.limpiar_campos()
            self.formulario_trabajador.show()

        def handler_formulario_guardar_trabajador():
            
            nuevo_trabajador = TrabajadorVO(id_trabajador=self.formulario_trabajador.w['input_id'].text(), nombre=self.formulario_trabajador.w['input_nombre'].text(),telefono=self.formulario_trabajador.w['input_telefono'].text(),EPS=self.formulario_trabajador.w['input_EPS'].text(),ARL=self.formulario_trabajador.w['input_ARL'].text(), fecha_creacion=self.formulario_trabajador.w['input_fecha_creacion'].text())
            
            TrabajadorDAO().adicionar_trabajador(trabajador = nuevo_trabajador)

        def handler_nuevo_arbol():
            self.formulario_arbol.limpiar_campos()
            self.formulario_arbol.show()

        def handler_formulario_guardar_arbol():

            nuevo_arbol = ArbolVO(fecha_siembra=self.formulario_arbol.w['input_fecha_siembra'].text())
            
            ArbolDAO().adicionar_arbol(arbol = nuevo_arbol)


        def handler_modificacion_trabajador(fila:int, columna:int):             
            self.formulario_modificar_trabajador.id_trabajador_update = int(self.ventana_principal.w['tabla_trabajador'].item(fila,0).text())
            self.formulario_modificar_trabajador.fecha_creacion_update = self.ventana_principal.w['tabla_trabajador'].item(fila,5).text()
            self.formulario_modificar_trabajador.w['label_id'].setText(str(self.formulario_modificar_trabajador.id_trabajador_update))
            self.formulario_modificar_trabajador.w['label_fecha_creacion'].setText(self.formulario_modificar_trabajador.fecha_creacion_update)
            
            
            self.formulario_modificar_trabajador.w['input_nombre'].setText(
                self.ventana_principal.w['tabla_trabajador'].item(fila, 1).text()
            )
            self.formulario_modificar_trabajador.w['input_telefono'].setText(
                self.ventana_principal.w['tabla_trabajador'].item(fila, 2).text()
            )
            self.formulario_modificar_trabajador.w['input_EPS'].setText(
                self.ventana_principal.w['tabla_trabajador'].item(fila, 3).text()
            )
            self.formulario_modificar_trabajador.w['input_ARL'].setText(
                self.ventana_principal.w['tabla_trabajador'].item(fila, 4).text()
            )
            self.formulario_modificar_trabajador.show()

        def handler_guardar_trabajador_modificado():
            
            trabajador_modificado = TrabajadorVO(id_trabajador=int(self.formulario_modificar_trabajador.id_trabajador_update), nombre=self.formulario_modificar_trabajador.w['input_nombre'].text(), telefono=self.formulario_modificar_trabajador.w['input_telefono'].text(), EPS=self.formulario_modificar_trabajador.w['input_EPS'].text(), ARL=self.formulario_modificar_trabajador.w['input_ARL'].text(), fecha_creacion=self.formulario_modificar_trabajador.fecha_creacion_update)
            TrabajadorDAO().modificar_trabajador( trabajador= trabajador_modificado)

        def handler_modificacion_arbol(fila:int, columna:int):             
            self.formulario_modificar_arbol.id_arbol_update = int(self.ventana_principal.w['tabla_arbol'].item(fila,0).text())
            self.formulario_modificar_arbol.w['label_id'].setText(str(self.formulario_modificar_arbol.id_arbol_update))

            
            
            self.formulario_modificar_arbol.w['input_fecha_siembra'].setText(
                self.ventana_principal.w['tabla_arbol'].item(fila, 1).text()
            )
            self.formulario_modificar_arbol.show()

        def handler_guardar_arbol_modificado():

            
            arbol_modificado = ArbolVO(id_arbol=int(self.formulario_modificar_arbol.id_arbol_update), fecha_siembra=self.formulario_modificar_arbol.w['input_fecha_siembra'].text())
            ArbolDAO().modificar_arbol( arbol= arbol_modificado)

        

        def handler_nueva_fumigacion_arbol():
            self.formulario_fumigacion.limpiar_campos()
            self.formulario_fumigacion.w['input_id_arbol'].setText(
                str(self.formulario_modificar_arbol.id_arbol_update))
            
            self.formulario_fumigacion.w['input_id_arbol'].setEnabled(False)
            self.formulario_fumigacion.w['input_id_trabajador'].setEnabled(True)
            self.formulario_fumigacion.show()

        def handler_nueva_nutricion_arbol():
            self.formulario_nutricion.limpiar_campos()
            self.formulario_nutricion.w['input_id_arbol'].setText(
                str(self.formulario_modificar_arbol.id_arbol_update))
            
            self.formulario_nutricion.w['input_id_arbol'].setEnabled(False)
            self.formulario_nutricion.w['input_id_trabajador'].setEnabled(True)
            self.formulario_nutricion.show()

        def handler_nueva_recolecta_arbol():
            self.formulario_recolecta.limpiar_campos()
            self.formulario_recolecta.w['input_id_arbol'].setText(
                str(self.formulario_modificar_arbol.id_arbol_update))
            
            self.formulario_recolecta.w['input_id_arbol'].setEnabled(False)
            self.formulario_recolecta.w['input_id_trabajador'].setEnabled(True)
            self.formulario_recolecta.show()

        def handler_nuevo_diagnostico_arbol():
            self.formulario_diagnostico.limpiar_campos()
            self.formulario_diagnostico.w['input_id_arbol'].setText(
                str(self.formulario_modificar_arbol.id_arbol_update))
            self.formulario_diagnostico.w['input_id_arbol'].setEnabled(False)
            


            handler_llenar_tabla_enfermedades()
            self.formulario_diagnostico.show()

        def handler_nuevo_diagnostico():
            self.formulario_diagnostico.limpiar_campos()
            handler_llenar_tabla_enfermedades()
            self.formulario_diagnostico.show()

        def handler_seleccionar_enfermedad(fila, columna):
            id_enfermedad = self.formulario_diagnostico.w['tabla_enfermedades'].item(fila, 0).text()
            self.formulario_diagnostico.w['input_id_enfermedad'].setText(id_enfermedad)

        def handler_formulario_guardar_diagnostico():

            nuevo_arbol_enfermedad = Arbol_EnfermedadVO(
                id_arbol=self.formulario_diagnostico.w['input_id_arbol'].text(),
                id_enfermedad=self.formulario_diagnostico.w['input_id_enfermedad'].text(),
                fecha_diagnostico=self.formulario_diagnostico.w['input_fecha_diagnostico'].text()
            )
            Arbol_EnfermedadDAO().adicionar_Arbol_Enfermedad(Arbol_Enfermedad=nuevo_arbol_enfermedad)

        def handler_ventana_enfermedades():
            handler_tabla_consulta_enfermedades()
            self.ventana_enfermedades.show()

        def handler_formulario_guardar_fumigacion():
            
            nueva_fumigacion = FumigacionVO(fecha_fumigacion=self.formulario_fumigacion.w['input_fecha_fumigacion'].text(), mezcla_fumigacion=self.formulario_fumigacion.w['input_mezcla_fumigacion'].text(),id_trabajador=self.formulario_fumigacion.w['input_id_trabajador'].text(),id_arbol=self.formulario_fumigacion.w['input_id_arbol'].text())
            
            FumigacionDAO().adicionar_fumigacion(fumigacion = nueva_fumigacion)

        def handler_formulario_guardar_nutricion():
            
            nueva_nutricion = NutricionVO(fecha_nutricion=self.formulario_nutricion.w['input_fecha_nutricion'].text(), mezcla_nutricion=self.formulario_nutricion.w['input_mezcla_nutricion'].text(),id_trabajador=self.formulario_nutricion.w['input_id_trabajador'].text(),id_arbol=self.formulario_nutricion.w['input_id_arbol'].text())
            
            NutricionDAO().adicionar_nutricion(nutricion = nueva_nutricion)

        def handler_formulario_guardar_recoleca():
            
            nueva_recolecta = RecolectaVO(fecha_recolecta=self.formulario_recolecta.w['input_fecha_recolecta'].text(), calidad=self.formulario_recolecta.w['input_calidad'].text(),peso=self.formulario_recolecta.w['input_peso'].text(),id_trabajador=self.formulario_recolecta.w['input_id_trabajador'].text(), id_arbol=self.formulario_recolecta.w['input_id_arbol'].text(), id_produccion=self.formulario_recolecta.w['input_id_produccion'].text())
            
            RecolectaDAO().adicionar_recolecta(recolecta= nueva_recolecta)

        def handler_nueva_fumigacion_trabajador():
            self.formulario_fumigacion.limpiar_campos()
            self.formulario_fumigacion.w['input_id_trabajador'].setText(
                str(self.formulario_modificar_trabajador.id_trabajador_update))
            
            self.formulario_fumigacion.w['input_id_trabajador'].setEnabled(False)
            self.formulario_fumigacion.w['input_id_arbol'].setEnabled(True)
            self.formulario_fumigacion.show()

        def handler_nueva_nutricion_trabajador():
            self.formulario_nutricion.limpiar_campos()
            self.formulario_nutricion.w['input_id_trabajador'].setText(
                str(self.formulario_modificar_trabajador.id_trabajador_update))
            
            self.formulario_nutricion.w['input_id_trabajador'].setEnabled(False)
            self.formulario_nutricion.w['input_id_arbol'].setEnabled(True)
            self.formulario_nutricion.show()

        def handler_nueva_recolecta_trabajador():
            self.formulario_recolecta.limpiar_campos()
            self.formulario_recolecta.w['input_id_trabajador'].setText(
                str(self.formulario_modificar_trabajador.id_trabajador_update))
            
            self.formulario_recolecta.w['input_id_trabajador'].setEnabled(False)
            self.formulario_recolecta.w['input_id_arbol'].setEnabled(True)
            self.formulario_recolecta.show()

        def handler_modificacion_fumigacion_arbol(fila:int, columna:int):             
            self.formulario_modificar_fumigacion.id_fumigacion_update = int(self.formulario_modificar_arbol.w['tabla_fumigaciones'].item(fila,0).text())
            self.formulario_modificar_fumigacion.w['label_id'].setText(str(self.formulario_modificar_fumigacion.id_fumigacion_update))
            
            
            self.formulario_modificar_fumigacion.w['input_fecha_fumigacion'].setText(
                self.formulario_modificar_arbol.w['tabla_fumigaciones'].item(fila, 1).text()
            )
            self.formulario_modificar_fumigacion.w['input_mezcla_fumigacion'].setText(
                self.formulario_modificar_arbol.w['tabla_fumigaciones'].item(fila, 2).text()
            )
            self.formulario_modificar_fumigacion.w['input_id_trabajador'].setText(
                self.formulario_modificar_arbol.w['tabla_fumigaciones'].item(fila, 3).text()
            )
            self.formulario_modificar_fumigacion.w['input_id_arbol'].setText(
                self.formulario_modificar_arbol.w['tabla_fumigaciones'].item(fila, 4).text()
            )

            self.formulario_modificar_fumigacion.w['input_id_arbol'].setEnabled(False)
            self.formulario_modificar_fumigacion.w['input_id_trabajador'].setEnabled(True)
            self.formulario_modificar_fumigacion.show()

        def handler_modificacion_nutricion_arbol(fila:int, columna:int):             
            self.formulario_modificar_nutricion.id_nutricion_update = int(self.formulario_modificar_arbol.w['tabla_nutriciones'].item(fila,0).text())
            self.formulario_modificar_nutricion.w['label_id'].setText(str(self.formulario_modificar_nutricion.id_nutricion_update))
            
            
            self.formulario_modificar_nutricion.w['input_fecha_nutricion'].setText(
                self.formulario_modificar_arbol.w['tabla_nutriciones'].item(fila, 1).text()
            )
            self.formulario_modificar_nutricion.w['input_mezcla_nutricion'].setText(
                self.formulario_modificar_arbol.w['tabla_nutriciones'].item(fila, 2).text()
            )
            self.formulario_modificar_nutricion.w['input_id_trabajador'].setText(
                self.formulario_modificar_arbol.w['tabla_nutriciones'].item(fila, 3).text()
            )
            self.formulario_modificar_nutricion.w['input_id_arbol'].setText(
                self.formulario_modificar_arbol.w['tabla_nutriciones'].item(fila, 4).text()
            )

            self.formulario_modificar_nutricion.w['input_id_arbol'].setEnabled(False)
            self.formulario_nutricion.w['input_id_trabajador'].setEnabled(True)
            self.formulario_modificar_nutricion.show()

        def handler_modificacion_recolecta_arbol(fila:int, columna:int):             
            self.formulario_modificar_recolecta.id_recolecta_update = int(self.formulario_modificar_arbol.w['tabla_recolectas'].item(fila,0).text())
            self.formulario_modificar_recolecta.w['label_id'].setText(str(self.formulario_modificar_recolecta.id_recolecta_update))
            
            
            self.formulario_modificar_recolecta.w['input_fecha_recolecta'].setText(
                self.formulario_modificar_arbol.w['tabla_recolectas'].item(fila, 1).text()
            )
            self.formulario_modificar_recolecta.w['input_calidad'].setText(
                self.formulario_modificar_arbol.w['tabla_recolectas'].item(fila, 2).text()
            )
            self.formulario_modificar_recolecta.w['input_peso'].setText(
                self.formulario_modificar_arbol.w['tabla_recolectas'].item(fila, 3).text()
            )
            self.formulario_modificar_recolecta.w['input_id_trabajador'].setText(
                self.formulario_modificar_arbol.w['tabla_recolectas'].item(fila, 4).text()
            )
            self.formulario_modificar_recolecta.w['input_id_arbol'].setText(
                self.formulario_modificar_arbol.w['tabla_recolectas'].item(fila, 5).text()
            )
            self.formulario_modificar_recolecta.w['input_id_produccion'].setText(
                self.formulario_modificar_arbol.w['tabla_recolectas'].item(fila, 6).text()
            )

            self.formulario_modificar_recolecta.w['input_id_arbol'].setEnabled(False)
            self.formulario_modificar_recolecta.show()

        def handler_guardar_fumigacion_modificada():
            
            fumigacion_modificada = FumigacionVO(id_fumigacion=int(self.formulario_modificar_fumigacion.id_fumigacion_update), fecha_fumigacion=self.formulario_modificar_fumigacion.w['input_fecha_fumigacion'].text(), mezcla_fumigacion=self.formulario_modificar_fumigacion.w['input_mezcla_fumigacion'].text(), id_trabajador=self.formulario_modificar_fumigacion.w['input_id_trabajador'].text(), id_arbol=self.formulario_modificar_fumigacion.w['input_id_arbol'].text())
            FumigacionDAO().modificar_fumigacion( fumigacion= fumigacion_modificada)

        def handler_guardar_nutricion_modificada():
            
            nutricion_modificada = NutricionVO(id_nutricion=int(self.formulario_modificar_nutricion.id_nutricion_update), fecha_nutricion=self.formulario_modificar_nutricion.w['input_fecha_nutricion'].text(), mezcla_nutricion=self.formulario_modificar_nutricion.w['input_mezcla_nutricion'].text(), id_trabajador=self.formulario_modificar_nutricion.w['input_id_trabajador'].text(), id_arbol=self.formulario_modificar_nutricion.w['input_id_arbol'].text())
            NutricionDAO().modificar_nutricion( nutricion=nutricion_modificada)

        def handler_guardar_recolecta_modificada():
            
            recolecta_modificada = RecolectaVO(id_recolecta=int(self.formulario_modificar_recolecta.id_recolecta_update), fecha_recolecta=self.formulario_modificar_recolecta.w['input_fecha_recolecta'].text(), calidad=self.formulario_modificar_recolecta.w['input_calidad'].text(), peso=self.formulario_modificar_recolecta.w['input_peso'].text(), id_trabajador=self.formulario_modificar_recolecta.w['input_id_trabajador'].text(), id_arbol=self.formulario_modificar_recolecta.w['input_id_arbol'].text(), id_produccion=self.formulario_modificar_recolecta.w['input_id_produccion'].text())
            RecolectaDAO().modificar_recolecta( recolecta=recolecta_modificada)

        def handler_modificacion_fumigacion_trabajador(fila:int, columna:int):             
            self.formulario_modificar_fumigacion.id_fumigacion_update = int(self.formulario_modificar_trabajador.w['tabla_fumigaciones'].item(fila,0).text())
            self.formulario_modificar_fumigacion.w['label_id'].setText(str(self.formulario_modificar_fumigacion.id_fumigacion_update))
            
            
            self.formulario_modificar_fumigacion.w['input_fecha_fumigacion'].setText(
                self.formulario_modificar_trabajador.w['tabla_fumigaciones'].item(fila, 1).text()
            )
            self.formulario_modificar_fumigacion.w['input_mezcla_fumigacion'].setText(
                self.formulario_modificar_trabajador.w['tabla_fumigaciones'].item(fila, 2).text()
            )
            self.formulario_modificar_fumigacion.w['input_id_trabajador'].setText(
                self.formulario_modificar_trabajador.w['tabla_fumigaciones'].item(fila, 3).text()
            )
            self.formulario_modificar_fumigacion.w['input_id_arbol'].setText(
                self.formulario_modificar_trabajador.w['tabla_fumigaciones'].item(fila, 4).text()
            )

            self.formulario_modificar_fumigacion.w['input_id_trabajador'].setEnabled(False)
            self.formulario_modificar_fumigacion.show()

        def handler_modificacion_nutricion_trabajador(fila:int, columna:int):             
            self.formulario_modificar_nutricion.id_nutricion_update = int(self.formulario_modificar_trabajador.w['tabla_nutriciones'].item(fila,0).text())
            self.formulario_modificar_nutricion.w['label_id'].setText(str(self.formulario_modificar_nutricion.id_nutricion_update))
            
            
            self.formulario_modificar_nutricion.w['input_fecha_nutricion'].setText(
                self.formulario_modificar_trabajador.w['tabla_nutriciones'].item(fila, 1).text()
            )
            self.formulario_modificar_nutricion.w['input_mezcla_nutricion'].setText(
                self.formulario_modificar_trabajador.w['tabla_nutriciones'].item(fila, 2).text()
            )
            self.formulario_modificar_nutricion.w['input_id_trabajador'].setText(
                self.formulario_modificar_trabajador.w['tabla_nutriciones'].item(fila, 3).text()
            )
            self.formulario_modificar_nutricion.w['input_id_arbol'].setText(
                self.formulario_modificar_trabajador.w['tabla_nutriciones'].item(fila, 4).text()
            )

            self.formulario_modificar_nutricion.w['input_id_trabajador'].setEnabled(False)
            self.formulario_modificar_nutricion.show()

        def handler_modificacion_recolecta_trabajador(fila:int, columna:int):             
            self.formulario_modificar_recolecta.id_recolecta_update = int(self.formulario_modificar_trabajador.w['tabla_recolectas'].item(fila,0).text())
            self.formulario_modificar_recolecta.w['label_id'].setText(str(self.formulario_modificar_recolecta.id_recolecta_update))
            
            
            self.formulario_modificar_recolecta.w['input_fecha_recolecta'].setText(
                self.formulario_modificar_trabajador.w['tabla_recolectas'].item(fila, 1).text()
            )
            self.formulario_modificar_recolecta.w['input_calidad'].setText(
                self.formulario_modificar_trabajador.w['tabla_recolectas'].item(fila, 2).text()
            )
            self.formulario_modificar_recolecta.w['input_peso'].setText(
                self.formulario_modificar_trabajador.w['tabla_recolectas'].item(fila, 3).text()
            )
            self.formulario_modificar_recolecta.w['input_id_trabajador'].setText(
                self.formulario_modificar_trabajador.w['tabla_recolectas'].item(fila, 4).text()
            )
            self.formulario_modificar_recolecta.w['input_id_arbol'].setText(
                self.formulario_modificar_trabajador.w['tabla_recolectas'].item(fila, 5).text()
            )
            self.formulario_modificar_recolecta.w['input_id_produccion'].setText(
                self.formulario_modificar_trabajador.w['tabla_recolectas'].item(fila, 6).text()
            )
            self.formulario_modificar_recolecta.w['input_id_trabajador'].setEnabled(False)
            self.formulario_modificar_recolecta.show()

        def handler_modificacion_fumigacion(fila:int, columna:int):             
            self.formulario_modificar_fumigacion.id_fumigacion_update = int(self.ventana_principal.w['tabla_fumigacion'].item(fila,0).text())
            self.formulario_modificar_fumigacion.w['label_id'].setText(str(self.formulario_modificar_fumigacion.id_fumigacion_update))
            
            
            self.formulario_modificar_fumigacion.w['input_fecha_fumigacion'].setText(
                self.ventana_principal.w['tabla_fumigacion'].item(fila, 1).text()
            )
            self.formulario_modificar_fumigacion.w['input_mezcla_fumigacion'].setText(
                self.ventana_principal.w['tabla_fumigacion'].item(fila, 2).text()
            )
            self.formulario_modificar_fumigacion.w['input_id_trabajador'].setText(
                self.ventana_principal.w['tabla_fumigacion'].item(fila, 3).text()
            )
            self.formulario_modificar_fumigacion.w['input_id_arbol'].setText(
                self.ventana_principal.w['tabla_fumigacion'].item(fila, 4).text()
            )

            self.formulario_modificar_fumigacion.show()

        def handler_modificacion_nutricion(fila:int, columna:int):             
            self.formulario_modificar_nutricion.id_nutricion_update = int(self.ventana_principal.w['tabla_nutricion'].item(fila,0).text())
            self.formulario_modificar_nutricion.w['label_id'].setText(str(self.formulario_modificar_nutricion.id_nutricion_update))
            
            
            self.formulario_modificar_nutricion.w['input_fecha_nutricion'].setText(
                self.ventana_principal.w['tabla_nutricion'].item(fila, 1).text()
            )
            self.formulario_modificar_nutricion.w['input_mezcla_nutricion'].setText(
                self.ventana_principal.w['tabla_nutricion'].item(fila, 2).text()
            )
            self.formulario_modificar_nutricion.w['input_id_trabajador'].setText(
                self.ventana_principal.w['tabla_nutricion'].item(fila, 3).text()
            )
            self.formulario_modificar_nutricion.w['input_id_arbol'].setText(
                self.ventana_principal.w['tabla_nutricion'].item(fila, 4).text()
            )

            self.formulario_modificar_nutricion.show()

        def handler_modificacion_recolecta(fila:int, columna:int):             
            self.formulario_modificar_recolecta.id_recolecta_update = int(self.ventana_principal.w['tabla_recolecta'].item(fila,0).text())
            self.formulario_modificar_recolecta.w['label_id'].setText(str(self.formulario_modificar_recolecta.id_recolecta_update))
            
            
            self.formulario_modificar_recolecta.w['input_fecha_recolecta'].setText(
                self.ventana_principal.w['tabla_recolecta'].item(fila, 1).text()
            )
            self.formulario_modificar_recolecta.w['input_calidad'].setText(
                self.ventana_principal.w['tabla_recolecta'].item(fila, 2).text()
            )
            self.formulario_modificar_recolecta.w['input_peso'].setText(
                self.ventana_principal.w['tabla_recolecta'].item(fila, 3).text()
            )
            self.formulario_modificar_recolecta.w['input_id_trabajador'].setText(
                self.ventana_principal.w['tabla_recolecta'].item(fila, 4).text()
            )
            self.formulario_modificar_recolecta.w['input_id_arbol'].setText(
                self.ventana_principal.w['tabla_recolecta'].item(fila, 5).text()
            )
            self.formulario_modificar_recolecta.w['input_id_produccion'].setText(
                self.ventana_principal.w['tabla_recolecta'].item(fila, 6).text()
            )

            self.formulario_modificar_recolecta.show()

        def handler_modificacion_enfermedad(fila:int, columna:int):             
            self.formulario_modificar_enfermedad.id_enfermedad_update = int(self.ventana_enfermedades.w['tabla_enfermedades'].item(fila,0).text())
            self.formulario_modificar_enfermedad.w['label_id'].setText(str(self.formulario_modificar_enfermedad.id_enfermedad_update))
            
            
            self.formulario_modificar_enfermedad.w['input_nombre_enfermedad'].setText(
                self.ventana_enfermedades.w['tabla_enfermedades'].item(fila, 1).text()
            )
            self.formulario_modificar_enfermedad.w['input_descripcion'].setText(
                self.ventana_enfermedades.w['tabla_enfermedades'].item(fila, 2).text()
            )
            self.formulario_modificar_enfermedad.w['input_causa'].setText(
                self.ventana_enfermedades.w['tabla_enfermedades'].item(fila, 3).text()
            )
            self.formulario_modificar_enfermedad.w['input_tratamiento'].setText(
                self.ventana_enfermedades.w['tabla_enfermedades'].item(fila, 4).text()
            )

            self.formulario_modificar_enfermedad.show()

        def handler_modificacion_diagnostico(fila:int, columna:int):             
            self.formulario_modificar_diagnostico.id_Arbol_Enfermedad_update = int(self.ventana_principal.w['tabla_diagnostico'].item(fila,0).text())
            self.formulario_modificar_diagnostico.w['label_id'].setText(str(self.formulario_modificar_diagnostico.id_Arbol_Enfermedad_update))
            
            
            self.formulario_modificar_diagnostico.w['input_id_arbol'].setText(
                self.ventana_principal.w['tabla_diagnostico'].item(fila, 1).text()
            )
            self.formulario_modificar_diagnostico.w['input_id_enfermedad'].setText(
                self.ventana_principal.w['tabla_diagnostico'].item(fila, 2).text()
            )
            self.formulario_modificar_diagnostico.w['input_fecha_diagnostico'].setText(
                self.ventana_principal.w['tabla_diagnostico'].item(fila, 7).text()
            )

            self.formulario_modificar_diagnostico.show()

        def handler_modificacion_diagnostico_arbol(fila:int, columna:int):             
            self.formulario_modificar_diagnostico.id_Arbol_Enfermedad_update = int(self.formulario_modificar_arbol.w['tabla_diagnosticos'].item(fila,0).text())
            self.formulario_modificar_diagnostico.w['label_id'].setText(str(self.formulario_modificar_diagnostico.id_Arbol_Enfermedad_update))
            
            
            self.formulario_modificar_diagnostico.w['input_id_arbol'].setText(
                self.formulario_modificar_arbol.w['tabla_diagnosticos'].item(fila, 0).text()
            )
            self.formulario_modificar_diagnostico.w['input_id_enfermedad'].setText(
                self.formulario_modificar_arbol.w['tabla_diagnosticos'].item(fila, 1).text()
            )
            self.formulario_modificar_diagnostico.w['input_fecha_diagnostico'].setText(
                self.formulario_modificar_arbol.w['tabla_diagnosticos'].item(fila, 6).text()
            )

            self.formulario_modificar_diagnostico.show()

        def handler_guardar_diagnostico_modificado():
            
            diagnostico_modificado = Arbol_EnfermedadVO(id_Arbol_Enfermedad=int(self.formulario_modificar_diagnostico.id_Arbol_Enfermedad_update), id_arbol=self.formulario_modificar_diagnostico.w['input_id_arbol'].text(), id_enfermedad=self.formulario_modificar_diagnostico.w['input_id_enfermedad'].text(), fecha_diagnostico=self.formulario_modificar_diagnostico.w['input_fecha_diagnostico'].text())
            Arbol_EnfermedadDAO().modificar_arbol_enfermedad( arbol_enfermedad=diagnostico_modificado)

        def handler_guardar_enfermedad_modificado():
            
            enfermedad_modificada = EnfermedadVO(id_enfermedad=int(self.formulario_modificar_enfermedad.id_enfermedad_update), nombre_enfermedad=self.formulario_modificar_enfermedad.w['input_nombre_enfermedad'].text(), descripcion=self.formulario_modificar_enfermedad.w['input_descripcion'].text(), causa=self.formulario_modificar_enfermedad.w['input_causa'].text(),tratamiento=self.formulario_modificar_enfermedad.w['input_tratamiento'].text())
            EnfermedadDAO().modificar_enfermedad( enfermedad=enfermedad_modificada)
        
        def handler_nueva_fumigacion():
            self.formulario_fumigacion.limpiar_campos()
            self.formulario_fumigacion.show()

        def handler_nueva_nutricion():
            self.formulario_nutricion.limpiar_campos()
            self.formulario_nutricion.show()

        def handler_nueva_recolecta():
            self.formulario_recolecta.limpiar_campos()
            self.formulario_recolecta.show()


        def handler_top_10():
            self.ventana_top_10.limpiar_campos()
            self.ventana_top_10.show()

        def handler_llenar_tabla_top():
            fecha_referencia =self.ventana_top_10.w['input_fecha_referencia'].text()
            print(fecha_referencia)
            top10 = TopArbolesVO(id_arbol=None, fecha_siembra=None, calidad=None, total_por_calidad=None, total_general=None, fecha_referencia=fecha_referencia)
            listado_top = TopArbolesDAO().obtener_top_10_arboles_por_calidad(top10)
            print(listado_top)
            self.ventana_top_10.w['tabla_top10'].setColumnCount(5)
            self.ventana_top_10.w['tabla_top10'].setHorizontalHeaderLabels(['id_arbol','fecha_siembra','calidad','total_por_calidad','total_general'])
            self.ventana_top_10.w['tabla_top10'].setRowCount(len(listado_top))
            self.ventana_top_10.w['tabla_top10'].verticalHeader().setVisible(False)
            for indice,top in enumerate(listado_top):
                self.ventana_top_10.w['tabla_top10'].setItem(indice,0,QTableWidgetItem(str(top.id_arbol)))
                self.ventana_top_10.w['tabla_top10'].setItem(indice,1,QTableWidgetItem(top.fecha_siembra))
                self.ventana_top_10.w['tabla_top10'].setItem(indice,2,QTableWidgetItem(top.calidad))
                self.ventana_top_10.w['tabla_top10'].setItem(indice,3,QTableWidgetItem(str(top.total_por_calidad)))
                self.ventana_top_10.w['tabla_top10'].setItem(indice,4,QTableWidgetItem(str(top.total_general)))
        

        
                
        
        self.ventana_principal.w['btn_arboles'].clicked.connect(handler_llenar_tabla_arboles)
        self.ventana_principal.w['btn_nuevo_arbol'].clicked.connect(handler_nuevo_arbol)
        self.formulario_arbol.w['btn_guardar'].clicked.connect(handler_formulario_guardar_arbol)
        self.ventana_principal.w['tabla_arbol'].cellDoubleClicked.connect(handler_modificacion_arbol)
        self.formulario_modificar_arbol.w['btn_guardar'].clicked.connect(handler_guardar_arbol_modificado)




        self.ventana_principal.w['btn_trabajadores'].clicked.connect(handler_llenar_tabla_trabajadores)
        self.ventana_principal.w['btn_nuevo_trabajador'].clicked.connect(handler_nuevo_trabajador)
        self.formulario_trabajador.w['btn_guardar'].clicked.connect(handler_formulario_guardar_trabajador)
        self.ventana_principal.w['tabla_trabajador'].cellDoubleClicked.connect(handler_modificacion_trabajador)
        self.formulario_modificar_trabajador.w['btn_guardar'].clicked.connect(handler_guardar_trabajador_modificado)


        self.ventana_principal.w['btn_fumigacion'].clicked.connect(handler_llenar_tabla_fumigaciones)
        self.ventana_principal.w['btn_nueva_fumigacion'].clicked.connect(handler_nueva_fumigacion)
        self.ventana_principal.w['tabla_fumigacion'].cellDoubleClicked.connect(handler_modificacion_fumigacion)

        self.formulario_modificar_arbol.w['btn_fumigaciones'].clicked.connect(handler_mostrar_fumigaciones_arbol)
        self.formulario_modificar_arbol.w['btn_nueva_fumigacion'].clicked.connect(handler_nueva_fumigacion_arbol)
        self.formulario_fumigacion.w['btn_guardar'].clicked.connect(handler_formulario_guardar_fumigacion)
        self.formulario_modificar_arbol.w['tabla_fumigaciones'].cellDoubleClicked.connect(handler_modificacion_fumigacion_arbol)

 
        self.formulario_modificar_trabajador.w['btn_fumigaciones'].clicked.connect(handler_mostrar_fumigaciones_trabajador)
        self.formulario_modificar_trabajador.w['btn_nueva_fumigacion'].clicked.connect(handler_nueva_fumigacion_trabajador)
        self.formulario_modificar_fumigacion.w['btn_guardar'].clicked.connect(handler_guardar_fumigacion_modificada)
        self.formulario_modificar_trabajador.w['tabla_fumigaciones'].cellDoubleClicked.connect(handler_modificacion_fumigacion_trabajador)

        self.ventana_principal.w['btn_nutricion'].clicked.connect(handler_llenar_tabla_nutriciones)
        self.ventana_principal.w['btn_nueva_nutricion'].clicked.connect(handler_nueva_nutricion)
        self.ventana_principal.w['tabla_nutricion'].cellDoubleClicked.connect(handler_modificacion_nutricion)

        self.formulario_modificar_arbol.w['btn_nutriciones'].clicked.connect(handler_mostrar_nutriciones_arbol)
        self.formulario_modificar_arbol.w['btn_nueva_nutricion'].clicked.connect(handler_nueva_nutricion_arbol)
        self.formulario_nutricion.w['btn_guardar'].clicked.connect(handler_formulario_guardar_nutricion)
        self.formulario_modificar_arbol.w['tabla_nutriciones'].cellDoubleClicked.connect(handler_modificacion_nutricion_arbol)

        self.formulario_modificar_trabajador.w['btn_nutriciones'].clicked.connect(handler_mostrar_nutriciones_trabajador)
        self.formulario_modificar_trabajador.w['btn_nueva_nutricion'].clicked.connect(handler_nueva_nutricion_trabajador)
        self.formulario_modificar_nutricion.w['btn_guardar'].clicked.connect(handler_guardar_nutricion_modificada)
        self.formulario_modificar_trabajador.w['tabla_nutriciones'].cellDoubleClicked.connect(handler_modificacion_nutricion_trabajador)


        self.ventana_principal.w['btn_recolecta'].clicked.connect(handler_llenar_tabla_recolectas)
        self.ventana_principal.w['btn_nueva_recolecta'].clicked.connect(handler_nueva_recolecta)
        self.ventana_principal.w['tabla_recolecta'].cellDoubleClicked.connect(handler_modificacion_recolecta)

        self.formulario_modificar_arbol.w['btn_recolectas'].clicked.connect(handler_mostrar_recolectas_arbol)
        self.formulario_modificar_arbol.w['btn_nueva_recolecta'].clicked.connect(handler_nueva_recolecta_arbol)
        self.formulario_recolecta.w['btn_guardar'].clicked.connect(handler_formulario_guardar_recoleca)
        self.formulario_modificar_arbol.w['tabla_recolectas'].cellDoubleClicked.connect(handler_modificacion_recolecta_arbol)

        self.formulario_modificar_trabajador.w['btn_recolectas'].clicked.connect(handler_mostrar_recolectas_trabajador)
        self.formulario_modificar_trabajador.w['btn_nueva_recolecta'].clicked.connect(handler_nueva_recolecta_trabajador)
        self.formulario_modificar_recolecta.w['btn_guardar'].clicked.connect(handler_guardar_recolecta_modificada)
        self.formulario_modificar_trabajador.w['tabla_recolectas'].cellDoubleClicked.connect(handler_modificacion_recolecta_trabajador)

        self.ventana_principal.w['btn_diagnostico'].clicked.connect(handler_llenar_tabla_diagnosticos)
        self.formulario_modificar_arbol.w['btn_diagnosticos'].clicked.connect(handler_mostrar_diagnostico_arbol)
        self.ventana_principal.w['btn_nuevo_diagnostico'].clicked.connect(handler_nuevo_diagnostico)

        self.formulario_modificar_arbol.w['btn_nuevo_diagnostico'].clicked.connect(handler_nuevo_diagnostico_arbol)
        self.formulario_diagnostico.w['btn_guardar'].clicked.connect(handler_formulario_guardar_diagnostico)
        self.formulario_diagnostico.w['tabla_enfermedades'].cellClicked.connect(handler_seleccionar_enfermedad)
        self.ventana_principal.w['btn_enfermedades'].clicked.connect(handler_ventana_enfermedades)
        self.ventana_enfermedades.w['btn_agregar_enfermedad'].clicked.connect(handler_nueva_enfermedad)
        self.formulario_enfermedad.w['btn_guardar'].clicked.connect(handler_formulario_guardar_enfermedad)
        self.ventana_enfermedades.w['btn_actualizar'].clicked.connect(handler_tabla_consulta_enfermedades)
        self.ventana_principal.w['btn_top10'].clicked.connect(handler_top_10)
        self.ventana_top_10.w['btn_top10'].clicked.connect(handler_llenar_tabla_top)

        self.ventana_enfermedades.w['tabla_enfermedades'].cellDoubleClicked.connect(handler_modificacion_enfermedad)
        self.formulario_modificar_enfermedad.w['btn_guardar'].clicked.connect(handler_guardar_enfermedad_modificado)
        self.ventana_principal.w['tabla_diagnostico'].cellDoubleClicked.connect(handler_modificacion_diagnostico)
        self.formulario_modificar_diagnostico.w['btn_guardar'].clicked.connect(handler_guardar_diagnostico_modificado)
        self.formulario_modificar_arbol.w['tabla_diagnosticos'].cellDoubleClicked.connect(handler_modificacion_diagnostico_arbol)
        self.formulario_diagnostico.w['btn_guardar'].clicked.connect(handler_modificacion_diagnostico_arbol)



        


    def mainloop(self):        
        
        self.ventana_principal.show()
        self.app.exec_()

    
    
    
    