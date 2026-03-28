from PyQt5.QtWidgets import (QPushButton, 
                             QVBoxLayout,
                             QHBoxLayout,
                             QTableWidget,
                             QApplication,
                             QMainWindow,
                             QSizePolicy,

                             QTableWidgetItem,
                             QSlider,
                             QLabel,
                             QWidget,
                             QDialog,
                             QLineEdit)
from PyQt5.QtGui import QGuiApplication

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Sistema Arboles Finca")
        pantalla = QGuiApplication.primaryScreen().availableGeometry()
        self.setGeometry(pantalla)  # ocupa toda la pantalla disponible


        self.w = dict()

    
        self.w['btn_arboles'] = QPushButton("Arboles")
        self.w['btn_arboles'].setObjectName("BotonArboles")
        self.w['btn_nuevo_arbol'] = QPushButton("Agregar Arbol")
        self.w['btn_nuevo_arbol'].setObjectName("BotonNuevoArbol")
        self.w['tabla_arbol'] = QTableWidget()
        


        self.w['btn_trabajadores'] = QPushButton("Trabajadores") 
        self.w['btn_trabajadores'].setObjectName("BotonTrabajadores")
        self.w['btn_nuevo_trabajador'] = QPushButton("Agregar Trabajador")
        self.w['btn_nuevo_trabajador'].setObjectName("BotonNuevoTrabajador")
        self.w['tabla_trabajador'] = QTableWidget()

        self.w['btn_fumigacion']=QPushButton("Fumigaciones")
        self.w['btn_fumigacion'].setObjectName("Boton_fumigacion")
        self.w['btn_nueva_fumigacion'] = QPushButton("Agregar Fumigacion")
        self.w['btn_nueva_fumigacion'].setObjectName("Boton_nueva_fumigacion")
        self.w['tabla_fumigacion'] = QTableWidget()

        self.w['btn_nutricion']=QPushButton("Nutriciones")
        self.w['btn_nutricion'].setObjectName("boton_nutriciones")
        self.w['btn_nueva_nutricion'] = QPushButton("Agregar Nutricion")
        self.w['btn_nueva_nutricion'].setObjectName("boton_agregar_nutricion")
        self.w['tabla_nutricion'] = QTableWidget()

        self.w['btn_recolecta']=QPushButton("Recolectas")
        self.w['btn_recolecta'].setObjectName("boton_recolectas")
        self.w['btn_nueva_recolecta'] = QPushButton("Agregar Recolecta")
        self.w['btn_nueva_recolecta'].setObjectName("boton_agregar_recolecta")
        self.w['tabla_recolecta'] = QTableWidget()

        self.w['btn_diagnostico']=QPushButton("Diagnostico")
        self.w['btn_diagnostico'].setObjectName("boton_diagnostico")
        self.w['btn_nuevo_diagnostico'] = QPushButton("Agregar Diagnostico")
        self.w['btn_nuevo_diagnostico'].setObjectName("boton_agregar_diagnostico")
        self.w['tabla_diagnostico'] = QTableWidget()

        self.w['btn_enfermedades']=QPushButton("Consultar enfermedades")
        self.w['btn_enfermedades'].setObjectName("boton_enfermedades")
        self.w['btn_top10']=QPushButton("Top 10 produccion de arboles")
        self.w['btn_top10'].setObjectName("botonTop10")

        self.layout_principal = QVBoxLayout()

        fila1 = QHBoxLayout()
        col_trabajadores = QVBoxLayout()
        col_arboles = QVBoxLayout()

        col_trabajadores.addWidget(self.w['btn_trabajadores'])
        col_trabajadores.addWidget(self.w['tabla_trabajador'])

        
        col_arboles.addWidget(self.w['btn_arboles'])
        col_arboles.addWidget(self.w['tabla_arbol'])

        fila1.addLayout(col_trabajadores)
        fila1.addLayout(col_arboles)
        self.layout_principal.addLayout(fila1)

        fila2 = QHBoxLayout()
        col_fumigaciones = QVBoxLayout()
        col_nutriciones = QVBoxLayout()

        
        col_fumigaciones.addWidget(self.w['btn_fumigacion'])
        col_fumigaciones.addWidget(self.w['tabla_fumigacion'])

        
        col_nutriciones.addWidget(self.w['btn_nutricion'])
        col_nutriciones.addWidget(self.w['tabla_nutricion'])

        fila2.addLayout(col_fumigaciones)
        fila2.addLayout(col_nutriciones)
        self.layout_principal.addLayout(fila2)




        fila3 = QHBoxLayout()
        col_recolectas = QVBoxLayout()
        col_diagnosticos = QVBoxLayout()

        
        col_recolectas.addWidget(self.w['btn_recolecta'])
        col_recolectas.addWidget(self.w['tabla_recolecta'])

        
        col_diagnosticos.addWidget(self.w['btn_diagnostico'])
        col_diagnosticos.addWidget(self.w['tabla_diagnostico'])

        fila3.addLayout(col_recolectas)
        fila3.addLayout(col_diagnosticos)
        self.layout_principal.addLayout(fila3)

        layout_botones_nuevos = QHBoxLayout()
        layout_botones_nuevos.addWidget(self.w['btn_nuevo_arbol'])
        layout_botones_nuevos.addWidget(self.w['btn_nuevo_trabajador'])
        layout_botones_nuevos.addWidget(self.w['btn_nueva_fumigacion'])
        layout_botones_nuevos.addWidget(self.w['btn_nueva_nutricion'])
        layout_botones_nuevos.addWidget(self.w['btn_nueva_recolecta'])
        layout_botones_nuevos.addWidget(self.w['btn_nuevo_diagnostico'])





        layout_abajo = QVBoxLayout()

        layout_abajo.addLayout(layout_botones_nuevos)

        layout_botones_finales = QHBoxLayout()
        layout_botones_finales.addWidget(self.w['btn_enfermedades'])
        layout_botones_finales.addWidget(self.w['btn_top10'])

        layout_abajo.addLayout(layout_botones_finales)
        self.layout_principal.addLayout(layout_abajo)





        


        
        
        # for key_w, w in self.w.items():
        #     self.layout_principal.addWidget(w)
            
        self.setLayout(self.layout_principal) 

        
        #Establacer la hoja de estilos de la ventana CSS->QSS
        self.setStyleSheet("""
                           #BotonArboles{
                                background-color: #b7e4c7;
                                font-weight:bold;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 20px;

                           }
                           #BotonArboles:hover {
                                background-color:#74c69d;
                                color:papayawhip;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 20px;
                           
                           }
                           #BotonTrabajadores{
                                background-color: #b7e4c7;
                                font-weight:bold;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 20px;
                           }
                            #BotonTrabajadores:hover{
                                background-color: #74c69d;
                                color:papayawhip;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 20px;
                           }

                           #BotonNuevoTrabajador{
                                background-color: #a8d5e2;
                                font-weight:bold;
                                border-radius:15px;
                                padding: 5px 15px;
                                max-width:200px;
                                min-width:200px;
                                font-size: 20px;
                           }
                            #BotonNuevoTrabajador:hover{
                                background-color: #3D9DB8;
                                color:papayawhip;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 20px;
                           }
                           #BotonNuevoArbol{
                                background-color: #a8d5e2;
                                font-weight:bold;
                                border-radius:15px;
                                padding: 5px 15px;
                                max-width:200px;
                                min-width:200px;
                                font-size: 20px;
                           
                           }
                            #BotonNuevoArbol:hover{
                                background-color: #3D9DB8;
                                color:papayawhip;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 20px;
                           }

                            #Boton_fumigacion{
                                background-color: #b7e4c7;
                                font-weight:bold;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 20px;
                           }

                           #Boton_fumigacion:hover{
                                background-color: #74c69d;
                                color:papayawhip;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 20px;
                           }

                            #Boton_nueva_fumigacion{
                                background-color: #a8d5e2;
                                font-weight:bold;
                                border-radius:15px;
                                padding: 5px 15px;
                                max-width:220px;
                                min-width:220px;
                                font-size: 20px;
                           }
                           #Boton_nueva_fumigacion:hover{
                                background-color: #3D9DB8;
                                color:papayawhip;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 20px;
                           }

                            #boton_nutriciones{
                                background-color: #b7e4c7;
                                font-weight:bold;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 20px;
                           }
                           #boton_nutriciones:hover{
                                background-color: #74c69d;
                                color:papayawhip;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 20px;
                           }

                            #boton_agregar_nutricion{
                                background-color: #a8d5e2;
                                font-weight:bold;
                                border-radius:15px;
                                padding: 5px 15px;
                                max-width:200px;
                                min-width:200px;
                                font-size: 20px;
                           }
                           #boton_agregar_nutricion:hover{
                                background-color: #3D9DB8;
                                color:papayawhip;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 20px;
                           }

                            #boton_recolectas{
                                background-color: #b7e4c7;
                                font-weight:bold;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 20px;
                           }
                           #boton_recolectas:hover{
                                background-color: #74c69d;
                                color:papayawhip;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 20px;
                           }

                            #boton_agregar_recolecta{
                                   background-color: #a8d5e2;
                                   font-weight:bold;
                                   border-radius:15px;
                                   padding: 5px 15px;
                                   max-width:200px;
                                   min-width:200px;
                                   font-size: 20px;
                              }
                              #boton_agregar_recolecta:hover{
                                   background-color: #3D9DB8;
                                color:papayawhip;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 20px;
                              }
                           
                              #boton_diagnostico{
                                   background-color: #b7e4c7;
                                   font-weight:bold;
                                   padding: 5px 15px;
                                   border-radius:15px;
                                   font-size: 20px;
                              }
                              #boton_diagnostico:hover{
                                   background-color: #74c69d;
                                color:papayawhip;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 20px;
                              }
                           
                               #boton_agregar_diagnostico{
                                   background-color: #a8d5e2;
                                   font-weight:bold;
                                   border-radius:15px;
                                   padding: 5px 15px;
                                   max-width:220px;
                                   min-width:220px;
                                   font-size: 20px;
                           }
                              #boton_agregar_diagnostico:hover{
                                   background-color: #3D9DB8;
                                color:papayawhip;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 20px;
                              }
                           
                             #boton_enfermedades {
                                background-color: #E3D1C9  ;
                                font-weight: bold;
                                border-radius:15px;
                                padding: 5px 200px;
                                max-width:265px;
                                min-width:265px;
                                font-size: 20px;
                            }
                            
                            
                            #boton_enfermedades:hover{
                                 background-color: #AA8B7E;
                                color:papayawhip;
                                border-radius:15px;
                                padding: 5px 200px;
                                max-width:265px;
                                min-width:265px;
                                font-size: 20px;

                            }
                           
                            #botonTop10{
                                 background-color: #E3D1C9;
                                 font-weight:bold;
                                border-radius:15px;
                                padding: 5px 200px;
                                max-width:300px;
                                min-width:300px;
                                font-size: 20px;
                            }
                            #botonTop10:hover{
                                 background-color: #AA8B7E;
                                color:papayawhip;
                                border-radius:15px;
                                padding: 5px 200px;
                                max-width:300px;
                                min-width:300px;
                                font-size: 20px;
                            }
                           
                            QTableWidget {

                                gridline-color: #999999;
                                font-size: 14px;
                            }
                            QHeaderView::section {
                                background-color: #E3D1C9;
                                color: black;
                                padding: 4px;
                                font-weight: bold;
                            }
                            QTableWidget::item:selected {
                                background-color: #AA8B7E;
                                color: white;
                            }
                                        

                                            """)

        

class FormularioNuevoTrabajador(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('FormularioTrabajador')
        self.setGeometry(100,100,400,300)
        self.w = dict()
        self.w['label_id'] = QLabel('Documento de identidad: ')
        self.w['input_id'] = QLineEdit()
        self.w['label_nombre'] = QLabel('Nombre: ')
        self.w['input_nombre'] = QLineEdit()
        self.w['label_telefono'] = QLabel('Telefono:')
        self.w['input_telefono'] = QLineEdit()
        self.w['label_EPS'] = QLabel('EPS:')
        self.w['input_EPS'] = QLineEdit()
        self.w['label_ARL'] = QLabel('ARL:')
        self.w['input_ARL'] = QLineEdit()
        self.w['label_fecha_creacion'] = QLabel('Fecha creación:')
        self.w['input_fecha_creacion'] = QLineEdit()
        self.w['btn_guardar'] = QPushButton('Guardar')
        self.w['btn_guardar'].setObjectName("boton_guardar")

        
        self.layout_principal = QVBoxLayout()
       
        for w in self.w.values():
           self.layout_principal.addWidget(w)

        self.setLayout(self.layout_principal)

        self.w['btn_guardar'].clicked.connect(self.accept)

        self.setStyleSheet("""
                           #boton_guardar{
                                background-color: #E3D1C9;
                                font-weight:bold;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;

                           }
                           #boton_guardar:hover {
                                background-color:#AA8B7E;
                                color:papayawhip;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;
                           }
                            """)
    def limpiar_campos(self):
        self.w['input_id'].clear()
        self.w['input_nombre'].clear()
        self.w['input_telefono'].clear()
        self.w['input_EPS'].clear()
        self.w['input_ARL'].clear()
        self.w['input_fecha_creacion'].clear()

           
class FormularioNuevoArbol(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('FormularioArbol')
        self.setGeometry(100,100,200,150)
        self.w = dict()

        self.w['label_fecha_siembra'] = QLabel('Fecha Siembra : ')
        self.w['input_fecha_siembra'] = QLineEdit()

        self.w['btn_guardar'] = QPushButton('Guardar')
        self.w['btn_guardar'].setObjectName("boton_guardar")

        self.layout_principal = QVBoxLayout()
       
        for w in self.w.values():
           self.layout_principal.addWidget(w)

        self.setLayout(self.layout_principal)

        self.w['btn_guardar'].clicked.connect(self.accept)

        self.setStyleSheet("""
                           #boton_guardar{
                                background-color: #E3D1C9;
                                font-weight:bold;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;

                           }
                           #boton_guardar:hover {
                                background-color:#AA8B7E;
                                color:papayawhip;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;
                           }
                            """)

    def limpiar_campos(self):
        self.w['input_fecha_siembra'].clear()
                             
                    
class FormularioModificarTrabajador(QDialog):
    def __init__(self):
        super().__init__()
        
        self.id_trabajador_update:int
        self.fecha_creacion_update:str
        
        self.setWindowTitle('FormularioModificarTrabajador')
        self.setGeometry(100,100,1000,1000)
        self.w = dict()
        self.w['label_id'] = QLabel("")
        self.w['label_fecha_creacion'] = QLabel("")        
        self.w['label_nombre'] = QLabel('Nuevo Nombre: ')
        self.w['input_nombre'] = QLineEdit()
        self.w['label_telefono'] = QLabel('Nuevo Telefono:')
        self.w['input_telefono'] = QLineEdit()
        self.w['label_EPS'] = QLabel('Nueva EPS:')
        self.w['input_EPS'] = QLineEdit()
        self.w['label_ARL'] = QLabel('Nueva ARL:')
        self.w['input_ARL'] = QLineEdit()
        self.w['btn_guardar'] = QPushButton('Guardar')
        self.w['btn_guardar'].setObjectName("boton_guardar")


        self.w['btn_fumigaciones'] = QPushButton("Listar fumigaciones")
        self.w['btn_fumigaciones'].setObjectName("BotonFumigaciones")
        self.w['btn_nueva_fumigacion'] = QPushButton("Agregar fumigacion")
        self.w['btn_nueva_fumigacion'].setObjectName("boton_nueva_fumigacion")
        self.w['tabla_fumigaciones'] = QTableWidget()


        self.w['btn_nutriciones'] = QPushButton("Listar nutriciones")
        self.w['btn_nutriciones'].setObjectName("BotonNutriciones")
        self.w['btn_nueva_nutricion'] = QPushButton("Agregar nutricion")
        self.w['btn_nueva_nutricion'].setObjectName("boton_nueva_nutricion")
        self.w['tabla_nutriciones'] = QTableWidget()


        self.w['btn_recolectas'] = QPushButton("Listar recolectas")
        self.w['btn_recolectas'].setObjectName("BotonRecolectas")
        self.w['btn_nueva_recolecta'] = QPushButton("Agregar recolecta")
        self.w['btn_nueva_recolecta'].setObjectName("boton_nueva_recolecta")
        self.w['tabla_recolectas'] = QTableWidget()


        self.layout_principal = QVBoxLayout()


        self.layout_principal.addWidget( self.w['label_id'])
        self.layout_principal.addWidget(self.w['label_fecha_creacion'])
        self.layout_principal.addWidget( self.w['label_nombre'])
        self.layout_principal.addWidget(self.w['input_nombre'])
        self.layout_principal.addWidget(self.w['label_telefono'])
        self.layout_principal.addWidget( self.w['input_telefono'])
        self.layout_principal.addWidget(self.w['label_EPS'])
        self.layout_principal.addWidget( self.w['input_EPS'])
        self.layout_principal.addWidget(self.w['label_ARL'])
        self.layout_principal.addWidget(self.w['input_ARL']) 
        self.layout_principal.addWidget(self.w['btn_guardar'])   

        


        layout_fumigaciones_botones = QHBoxLayout()
        layout_fumigaciones_botones.addWidget(self.w['btn_fumigaciones'])
        layout_fumigaciones_botones.addWidget(self.w['btn_nueva_fumigacion'])
        self.layout_principal.addLayout(layout_fumigaciones_botones)
        self.layout_principal.addWidget(self.w['tabla_fumigaciones'])

        layout_nutriciones_botones = QHBoxLayout()
        layout_nutriciones_botones.addWidget(self.w['btn_nutriciones'])
        layout_nutriciones_botones.addWidget(self.w['btn_nueva_nutricion'])
        self.layout_principal.addLayout(layout_nutriciones_botones)
        self.layout_principal.addWidget(self.w['tabla_nutriciones'])

        layout_recolectas_botones = QHBoxLayout()
        layout_recolectas_botones.addWidget(self.w['btn_recolectas'])
        layout_recolectas_botones.addWidget(self.w['btn_nueva_recolecta'])
        self.layout_principal.addLayout(layout_recolectas_botones)
        self.layout_principal.addWidget(self.w['tabla_recolectas'])
       


        self.setLayout(self.layout_principal)

        self.w['btn_guardar'].clicked.connect(self.accept)

        self.setStyleSheet("""
                           #boton_guardar{
                                background-color: #E3D1C9;
                                font-weight:bold;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;

                           }
                           #boton_guardar:hover {
                                background-color:#AA8B7E;
                                color:papayawhip;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;
                           }
                           


                            #BotonFumigaciones{
                                background-color: #b7e4c7;
                                font-weight:bold;
                                padding: 5px 10px;
                                border-radius:10px;
                                font-size: 15px;
                           }

                           #BotonFumigaciones:hover{
                                background-color: #74c69d;
                                color:papayawhip;
                                padding: 5px 10px;
                                border-radius:10px;
                                font-size: 15px;
                           }

                            #boton_nueva_fumigacion{
                                background-color: #a8d5e2;
                                font-weight:bold;
                                border-radius:10px;
                                padding: 5px 10px;
                                max-width:220px;
                                min-width:220px;
                                font-size: 15px;
                           }
                           #boton_nueva_fumigacion:hover{
                                background-color: #3D9DB8;
                                color:papayawhip;
                                padding: 5px 10px;
                                border-radius:10px;
                                font-size: 15px;
                           }

                            #BotonNutriciones{
                                background-color: #b7e4c7;
                                font-weight:bold;
                                padding: 5px 10px;
                                border-radius:10px;
                                font-size: 15px;
                           }
                           #BotonNutriciones:hover{
                                background-color: #74c69d;
                                color:papayawhip;
                                padding: 5px 10px;
                                border-radius:10px;
                                font-size: 15px;
                           }

                            #boton_nueva_nutricion{
                                background-color: #a8d5e2;
                                font-weight:bold;
                                border-radius:10px;
                                padding: 5px 10px;
                                max-width:200px;
                                min-width:200px;
                                font-size: 15px;
                           }
                           #boton_nueva_nutricion:hover{
                                background-color: #3D9DB8;
                                color:papayawhip;
                                padding: 5px 10px;
                                border-radius:10px;
                                font-size: 15px;
                           }

                            #BotonRecolectas{
                                background-color: #b7e4c7;
                                font-weight:bold;
                                padding: 5px 10px;
                                border-radius:10px;
                                font-size: 15px;
                           }
                           #BotonRecolectas:hover{
                                background-color: #74c69d;
                                color:papayawhip;
                                padding: 5px 10px;
                                border-radius:10px;
                                font-size: 15px;
                           }

                            #boton_nueva_recolecta{
                                   background-color: #a8d5e2;
                                   font-weight:bold;
                                   border-radius:10px;
                                   padding: 5px 10px;
                                   max-width:200px;
                                   min-width:200px;
                                   font-size: 15px;
                              }
                              #boton_nueva_recolecta:hover{
                                   background-color: #3D9DB8;
                                color:papayawhip;
                                padding: 5px 10px;
                                border-radius:10px;
                                font-size: 15px;
                           

                              }
                           
                            QTableWidget {

                                gridline-color: #999999;
                                font-size: 14px;
                            }
                            QHeaderView::section {
                                background-color: #E3D1C9;
                                color: black;
                                padding: 4px;
                                font-weight: bold;
                            }
                            QTableWidget::item:selected {
                                background-color: #AA8B7E;
                                color: white;
                            }
                    
                           

                            """)

    def closeEvent(self, event):
        self.w['tabla_fumigaciones'].clear()
        self.w['tabla_fumigaciones'].setRowCount(0)
        self.w['tabla_fumigaciones'].setColumnCount(0)
        self.w['tabla_nutriciones'].clear()
        self.w['tabla_nutriciones'].setRowCount(0)
        self.w['tabla_nutriciones'].setColumnCount(0)
        self.w['tabla_recolectas'].clear()
        self.w['tabla_recolectas'].setRowCount(0)
        self.w['tabla_recolectas'].setColumnCount(0)
        event.accept()

class FormularioNuevaFumigacion(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('FormularioFumigacion')
        self.setGeometry(100,100,400,300)
        self.w = dict()
        self.w['label_fecha_fumigacion'] = QLabel('Fecha: ')
        self.w['input_fecha_fumigacion'] = QLineEdit()
        self.w['label_mezcla_fumigacion'] = QLabel('Mezcla: ')
        self.w['input_mezcla_fumigacion'] = QLineEdit()
        self.w['label_id_trabajador'] = QLabel('Identidad Trabajador:')
        self.w['input_id_trabajador'] = QLineEdit()
        self.w['label_id_arbol'] = QLabel('Arbol:')
        self.w['input_id_arbol'] = QLineEdit()
        self.w['btn_guardar'] = QPushButton('Guardar')
        self.w['btn_guardar'].setObjectName("boton_guardar")
        self.layout_principal = QVBoxLayout()
       
        for w in self.w.values():
           self.layout_principal.addWidget(w)

        self.setLayout(self.layout_principal)

        self.w['btn_guardar'].clicked.connect(self.accept)

        self.setStyleSheet("""
                           #boton_guardar{
                                background-color: #E3D1C9;
                                font-weight:bold;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;

                           }
                           #boton_guardar:hover {
                                background-color:#AA8B7E;
                                color:papayawhip;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;
                           }
                            """)
        
    def limpiar_campos(self):
        self.w['input_fecha_fumigacion'].clear()
        self.w['input_mezcla_fumigacion'].clear()
        self.w['input_id_trabajador'].clear()
        self.w['input_id_arbol'].clear()

    

class FormularioNuevaNutricion(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('FormularioNutricion')
        self.setGeometry(100,100,400,300)
        self.w = dict()
        self.w['label_fecha_nutricion'] = QLabel('Fecha: ')
        self.w['input_fecha_nutricion'] = QLineEdit()
        self.w['label_mezcla_nutricion'] = QLabel('Mezcla: ')
        self.w['input_mezcla_nutricion'] = QLineEdit()
        self.w['label_id_trabajador'] = QLabel('Identidad Trabajador:')
        self.w['input_id_trabajador'] = QLineEdit()
        self.w['label_id_arbol'] = QLabel('Arbol:')
        self.w['input_id_arbol'] = QLineEdit()
        self.w['btn_guardar'] = QPushButton('Guardar')
        self.w['btn_guardar'].setObjectName("boton_guardar")
        self.layout_principal = QVBoxLayout()
       
        for w in self.w.values():
           self.layout_principal.addWidget(w)

        self.setLayout(self.layout_principal)

        self.w['btn_guardar'].clicked.connect(self.accept)

        self.setStyleSheet("""
                           #boton_guardar{
                                background-color: #E3D1C9;
                                font-weight:bold;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;

                           }
                           #boton_guardar:hover {
                                background-color:#AA8B7E;
                                color:papayawhip;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;
                           }
                            """)
        
    def limpiar_campos(self):
        self.w['input_fecha_nutricion'].clear()
        self.w['input_mezcla_nutricion'].clear()
        self.w['input_id_trabajador'].clear()
        self.w['input_id_arbol'].clear()

class FormularioNuevaRecolecta(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('FormularioRecolecta')
        self.setGeometry(100,100,400,300)
        self.w = dict()
        self.w['label_fecha_recolecta'] = QLabel('Fecha: ')
        self.w['input_fecha_recolecta'] = QLineEdit()
        self.w['label_calidad'] = QLabel('Calidad: ')
        self.w['input_calidad'] = QLineEdit()
        self.w['label_peso'] = QLabel('Peso:')
        self.w['input_peso'] = QLineEdit()
        self.w['label_id_trabajador'] = QLabel('id Trabajador:')
        self.w['input_id_trabajador'] = QLineEdit()
        self.w['label_id_arbol'] = QLabel('id Arbol:')
        self.w['input_id_arbol'] = QLineEdit()
        self.w['label_id_produccion'] = QLabel('id produccion:')
        self.w['input_id_produccion'] = QLineEdit()

        self.w['btn_guardar'] = QPushButton('Guardar')
        self.w['btn_guardar'].setObjectName("boton_guardar")
        self.layout_principal = QVBoxLayout()
       
        for w in self.w.values():
           self.layout_principal.addWidget(w)

        self.setLayout(self.layout_principal)

        self.w['btn_guardar'].clicked.connect(self.accept)

        self.setStyleSheet("""
                           #boton_guardar{
                                background-color: #E3D1C9;
                                font-weight:bold;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;

                           }
                           #boton_guardar:hover {
                                background-color:#AA8B7E;
                                color:papayawhip;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;
                           }
                            """)
        
    def limpiar_campos(self):
        self.w['input_fecha_recolecta'].clear()
        self.w['input_calidad'].clear()
        self.w['input_peso'].clear()
        self.w['input_id_trabajador'].clear()
        self.w['input_id_arbol'].clear()
        self.w['input_id_produccion'].clear()

class FormularioModificarArbol(QDialog):
    def __init__(self):
        super().__init__()
        
        self.id_arbol_update:int
        
        self.setWindowTitle('FormularioModificarArbol')
        self.setGeometry(100,100,800,300)
        self.w = dict()
        self.w['label_id'] = QLabel("")      
        self.w['label_fecha_siembra'] = QLabel('Nueva fecha siembra: ')
        self.w['input_fecha_siembra'] = QLineEdit()
        self.w['btn_guardar'] = QPushButton('Guardar')

        self.w['btn_guardar'].setObjectName("boton_guardar")


        self.w['btn_fumigaciones'] = QPushButton("Listar fumigaciones")
        self.w['btn_fumigaciones'].setObjectName("BotonFumigaciones")
        self.w['btn_nueva_fumigacion'] = QPushButton("Agregar fumigacion")
        self.w['btn_nueva_fumigacion'].setObjectName("boton_nueva_fumigacion")
        self.w['tabla_fumigaciones'] = QTableWidget()


        self.w['btn_nutriciones'] = QPushButton("Listar nutriciones")
        self.w['btn_nutriciones'].setObjectName("BotonNutriciones")
        self.w['btn_nueva_nutricion'] = QPushButton("Agregar nutricion")
        self.w['btn_nueva_nutricion'].setObjectName("boton_nueva_nutricion")
        self.w['tabla_nutriciones'] = QTableWidget()


        self.w['btn_recolectas'] = QPushButton("Listar recolectas")
        self.w['btn_recolectas'].setObjectName("BotonRecolectas")
        self.w['btn_nueva_recolecta'] = QPushButton("Agregar recolecta")
        self.w['btn_nueva_recolecta'].setObjectName("boton_nueva_recolecta")
        self.w['tabla_recolectas'] = QTableWidget()

        self.w['btn_diagnosticos'] = QPushButton("Listar Diagnosticos")
        self.w['btn_diagnosticos'].setObjectName("BotonDiagnosticos")
        self.w['btn_nuevo_diagnostico'] = QPushButton("Agregar diagnostico")
        self.w['btn_nuevo_diagnostico'].setObjectName("nuevo_diagnostico")
        self.w['tabla_diagnosticos'] = QTableWidget()

        self.layout_principal = QVBoxLayout()

        self.layout_principal.addWidget( self.w['label_id'])
        self.layout_principal.addWidget(self.w['label_fecha_siembra'])
        self.layout_principal.addWidget( self.w['input_fecha_siembra'])
        self.layout_principal.addWidget(self.w['btn_guardar'])

        layout_fumigaciones_botones = QHBoxLayout()
        layout_fumigaciones_botones.addWidget(self.w['btn_fumigaciones'])
        layout_fumigaciones_botones.addWidget(self.w['btn_nueva_fumigacion'])
        self.layout_principal.addLayout(layout_fumigaciones_botones)
        self.layout_principal.addWidget(self.w['tabla_fumigaciones'])

        layout_nutriciones_botones = QHBoxLayout()
        layout_nutriciones_botones.addWidget(self.w['btn_nutriciones'])
        layout_nutriciones_botones.addWidget(self.w['btn_nueva_nutricion'])
        self.layout_principal.addLayout(layout_nutriciones_botones)
        self.layout_principal.addWidget(self.w['tabla_nutriciones'])

        layout_recolectas_botones = QHBoxLayout()
        layout_recolectas_botones.addWidget(self.w['btn_recolectas'])
        layout_recolectas_botones.addWidget(self.w['btn_nueva_recolecta'])
        self.layout_principal.addLayout(layout_recolectas_botones)
        self.layout_principal.addWidget(self.w['tabla_recolectas'])

        layout_diagnosticos_botones = QHBoxLayout()
        layout_diagnosticos_botones.addWidget(self.w['btn_diagnosticos'])
        layout_diagnosticos_botones.addWidget(self.w['btn_nuevo_diagnostico'])
        self.layout_principal.addLayout(layout_diagnosticos_botones)
        self.layout_principal.addWidget(self.w['tabla_diagnosticos'])
       


        self.setLayout(self.layout_principal)

        self.w['btn_guardar'].clicked.connect(self.accept)

        self.setStyleSheet("""
                           #boton_guardar{
                                background-color: #E3D1C9;
                                font-weight:bold;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;

                           }
                           #boton_guardar:hover {
                                background-color:#AA8B7E;
                                color:papayawhip;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;
                           }
                           


                            #BotonFumigaciones{
                                background-color: #b7e4c7;
                                font-weight:bold;
                                padding: 5px 10px;
                                border-radius:10px;
                                font-size: 15px;
                           }

                           #BotonFumigaciones:hover{
                                background-color: #74c69d;
                                color:papayawhip;
                                padding: 5px 10px;
                                border-radius:10px;
                                font-size: 15px;
                           }

                            #boton_nueva_fumigacion{
                                background-color: #a8d5e2;
                                font-weight:bold;
                                border-radius:10px;
                                padding: 5px 10px;
                                max-width:220px;
                                min-width:220px;
                                font-size: 15px;
                           }
                           #boton_nueva_fumigacion:hover{
                                background-color: #3D9DB8;
                                color:papayawhip;
                                padding: 5px 10px;
                                border-radius:10px;
                                font-size: 15px;
                           }

                            #BotonNutriciones{
                                background-color: #b7e4c7;
                                font-weight:bold;
                                padding: 5px 10px;
                                border-radius:10px;
                                font-size: 15px;
                           }
                           #BotonNutriciones:hover{
                                background-color: #74c69d;
                                color:papayawhip;
                                padding: 5px 10px;
                                border-radius:10px;
                                font-size: 15px;
                           }

                            #boton_nueva_nutricion{
                                background-color: #a8d5e2;
                                font-weight:bold;
                                border-radius:10px;
                                padding: 5px 10px;
                                max-width:200px;
                                min-width:200px;
                                font-size: 15px;
                           }
                           #boton_nueva_nutricion:hover{
                                background-color: #3D9DB8;
                                color:papayawhip;
                                padding: 5px 10px;
                                border-radius:10px;
                                font-size: 15px;
                           }

                            #BotonRecolectas{
                                background-color: #b7e4c7;
                                font-weight:bold;
                                padding: 5px 10px;
                                border-radius:10px;
                                font-size: 15px;
                           }
                           #BotonRecolectas:hover{
                                background-color: #74c69d;
                                color:papayawhip;
                                padding: 5px 10px;
                                border-radius:10px;
                                font-size: 15px;
                           }

                            #boton_nueva_recolecta{
                                   background-color: #a8d5e2;
                                   font-weight:bold;
                                   border-radius:10px;
                                   padding: 5px 10px;
                                   max-width:200px;
                                   min-width:200px;
                                   font-size: 15px;
                              }
                              #boton_nueva_recolecta:hover{
                                   background-color: #3D9DB8;
                                color:papayawhip;
                                padding: 5px 10px;
                                border-radius:10px;
                                font-size: 15px;
                              }
                           
                            #BotonDiagnosticos{
                                background-color: #b7e4c7;
                                font-weight:bold;
                                padding: 5px 10px;
                                border-radius:10px;
                                font-size: 15px;
                           }
                           #BotonDiagnosticos:hover{
                                background-color: #74c69d;
                                color:papayawhip;
                                padding: 5px 10px;
                                border-radius:10px;
                                font-size: 15px;
                           }

                            #nuevo_diagnostico{
                                   background-color: #a8d5e2;
                                   font-weight:bold;
                                   border-radius:10px;
                                   padding: 5px 10px;
                                   max-width:200px;
                                   min-width:200px;
                                   font-size: 15px;
                              }
                            #nuevo_rdiagnostico:hover{
                                   background-color: #3D9DB8;
                                color:papayawhip;
                                padding: 5px 10px;
                                border-radius:10px;
                                font-size: 15px;
                              }
                           
                           QTableWidget {

                                gridline-color: #999999;
                                font-size: 14px;
                            }
                            QHeaderView::section {
                                background-color: #E3D1C9;
                                color: black;
                                padding: 4px;
                                font-weight: bold;
                            }
                            QTableWidget::item:selected {
                                background-color: #AA8B7E;
                                color: white;
                            }

                    
                           

                            """)

    def closeEvent(self, event):
        self.w['tabla_fumigaciones'].clear()
        self.w['tabla_fumigaciones'].setRowCount(0)
        self.w['tabla_fumigaciones'].setColumnCount(0)
        self.w['tabla_nutriciones'].clear()
        self.w['tabla_nutriciones'].setRowCount(0)
        self.w['tabla_nutriciones'].setColumnCount(0)
        self.w['tabla_recolectas'].clear()
        self.w['tabla_recolectas'].setRowCount(0)
        self.w['tabla_recolectas'].setColumnCount(0)
        self.w['tabla_diagnosticos'].clear()
        self.w['tabla_diagnosticos'].setRowCount(0)
        self.w['tabla_diagnosticos'].setColumnCount(0)
        event.accept()

        
class FormularioModificarFumigacion(QDialog):
    def __init__(self):
        super().__init__()
        
        self.id_fumigacion_update:int

        
        self.setWindowTitle('FormularioModificarFumigacion')
        self.setGeometry(100,100,400,300)
        self.w = dict()
        self.w['label_id'] = QLabel("")      
        self.w['label_fecha_fumigacion'] = QLabel('Nueva fecha: ')
        self.w['input_fecha_fumigacion'] = QLineEdit()
        self.w['label_mezcla_fumigacion'] = QLabel('Nueva Mezcla:')
        self.w['input_mezcla_fumigacion'] = QLineEdit()
        self.w['label_id_trabajador'] = QLabel('Nuevo trabajador:')
        self.w['input_id_trabajador'] = QLineEdit()
        self.w['label_id_arbol'] = QLabel('id arbol:')
        self.w['input_id_arbol'] = QLineEdit()
        self.w['btn_guardar'] = QPushButton('Guardar')
        self.w['btn_guardar'].setObjectName("boton_guardar")

        self.layout_principal = QVBoxLayout()
       
        for w in self.w.values():
           self.layout_principal.addWidget(w)

        self.setLayout(self.layout_principal)

        self.w['btn_guardar'].clicked.connect(self.accept)

        self.setStyleSheet("""
                           #boton_guardar{
                                background-color: #E3D1C9;
                                font-weight:bold;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;

                           }
                           #boton_guardar:hover {
                                background-color:#AA8B7E;
                                color:papayawhip;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;
                           }
                            """)

class FormularioModificarNutricion(QDialog):
    def __init__(self):
        super().__init__()
        
        self.id_nutricion_update:int

        
        self.setWindowTitle('FormularioModificarNutricion')
        self.setGeometry(100,100,400,300)
        self.w = dict()
        self.w['label_id'] = QLabel("")      
        self.w['label_fecha_nutricion'] = QLabel('Nueva fecha: ')
        self.w['input_fecha_nutricion'] = QLineEdit()
        self.w['label_mezcla_nutricion'] = QLabel('Nueva Mezcla:')
        self.w['input_mezcla_nutricion'] = QLineEdit()
        self.w['label_id_trabajador'] = QLabel('Nuevo trabajador:')
        self.w['input_id_trabajador'] = QLineEdit()
        self.w['label_id_arbol'] = QLabel('id arbol:')
        self.w['input_id_arbol'] = QLineEdit()
        self.w['btn_guardar'] = QPushButton('Guardar')
        self.w['btn_guardar'].setObjectName("boton_guardar")
        self.layout_principal = QVBoxLayout()
       
        for w in self.w.values():
           self.layout_principal.addWidget(w)

        self.setLayout(self.layout_principal)

        self.w['btn_guardar'].clicked.connect(self.accept)
        self.setStyleSheet("""
                           #boton_guardar{
                                background-color: #E3D1C9;
                                font-weight:bold;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;

                           }
                           #boton_guardar:hover {
                                background-color:#AA8B7E;
                                color:papayawhip;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;
                           }
                            """)

class FormularioModificarRecolecta(QDialog):
    def __init__(self):
        super().__init__()
        
        self.id_recolecta_update:int

        
        self.setWindowTitle('FormularioModificarRecolecta')
        self.setGeometry(100,100,400,300)
        self.w = dict()
        self.w['label_id'] = QLabel("")      
        self.w['label_fecha_recolecta'] = QLabel('Nueva fecha: ')
        self.w['input_fecha_recolecta'] = QLineEdit()
        self.w['label_calidad'] = QLabel('Nueva calidad:')
        self.w['input_calidad'] = QLineEdit()
        self.w['label_peso'] = QLabel('Nuevo peso:')
        self.w['input_peso'] = QLineEdit()
        self.w['label_id_trabajador'] = QLabel('id trabajador:')
        self.w['input_id_trabajador'] = QLineEdit()
        self.w['label_id_arbol'] = QLabel('id arbol:')
        self.w['input_id_arbol'] = QLineEdit()
        self.w['label_id_produccion'] = QLabel('id produccion:')
        self.w['input_id_produccion'] = QLineEdit()

        self.w['btn_guardar'] = QPushButton('Guardar')
        self.w['btn_guardar'].setObjectName("boton_guardar")
        self.layout_principal = QVBoxLayout()
       
        for w in self.w.values():
           self.layout_principal.addWidget(w)

        self.setLayout(self.layout_principal)

        self.w['btn_guardar'].clicked.connect(self.accept)

        self.setStyleSheet("""
                           #boton_guardar{
                                background-color: #E3D1C9;
                                font-weight:bold;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;

                           }
                           #boton_guardar:hover {
                                background-color:#AA8B7E;
                                color:papayawhip;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;
                           }
                            """)


class FormularioNuevoDiagnostico(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('FormularioDiagnostico')
        self.setGeometry(100,100,800,800)
        self.w = dict()
        self.w['label_id_arbol'] = QLabel('Arbol: ')
        self.w['input_id_arbol'] = QLineEdit()
        self.w['label_id_enfermedad'] = QLabel('Id Enfermedad: ')
        self.w['input_id_enfermedad'] = QLineEdit()
        self.w['label_fecha_diagnostico'] = QLabel('Fecha Diagnostico:')
        self.w['input_fecha_diagnostico'] = QLineEdit()

        self.w['label_enfermedades'] = QLabel('Enfermedades Disponibles (haz clic para seleccionar):')
        self.w['tabla_enfermedades'] = QTableWidget()


        self.w['btn_guardar'] = QPushButton('Guardar')
        self.w['btn_guardar'].setObjectName("boton_guardar")
        self.layout_principal = QVBoxLayout()
       
        for w in self.w.values():
           self.layout_principal.addWidget(w)

        self.setLayout(self.layout_principal)

        self.w['btn_guardar'].clicked.connect(self.accept)

        self.setStyleSheet("""
                           #boton_guardar{
                                background-color: #E3D1C9;
                                font-weight:bold;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;

                           }
                           #boton_guardar:hover {
                                background-color:#AA8B7E;
                                color:papayawhip;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;
                           }
                            """)

        
    def limpiar_campos(self):
        self.w['input_id_arbol'].clear()
        self.w['input_id_enfermedad'].clear()
        self.w['input_fecha_diagnostico'].clear()
        self.w['tabla_enfermedades'].clear()
        self.w['tabla_enfermedades'].setRowCount(0)
        self.w['tabla_enfermedades'].setColumnCount(0)



class VentanaEnfermedades(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('VentanaEnfermedades')
        self.setGeometry(100,100,900,900)
        self.w = dict()

        self.w['tabla_enfermedades'] = QTableWidget()

        self.w['btn_agregar_enfermedad']=QPushButton('Agregar enfermedad')
        self.w['btn_agregar_enfermedad'].setObjectName("boton_nueva_enfermedad")


        self.w['btn_actualizar'] = QPushButton('Actualizar')
        self.w['btn_actualizar'].setObjectName("boton_actualizar")

        self.layout_principal = QVBoxLayout()
       
        for w in self.w.values():
           self.layout_principal.addWidget(w)

        self.setLayout(self.layout_principal)

        self.setStyleSheet("""
                           #boton_actualizar{
                                background-color: #E3D1C9;
                                font-weight:bold;
                                padding: 5px 10px;
                                border-radius:10px;
                                font-size: 15px;

                           }
                           #boton_actualizar:hover {
                                background-color:#AA8B7E;
                                color:papayawhip;
                                padding: 5px 10px;
                                border-radius:10px;
                                font-size: 15px;
                           }

                           #boton_nueva_enfermedad{
                                   background-color: #a8d5e2;
                                   font-weight:bold;
                                   border-radius:10px;
                                   padding: 5px 10px;
                                   font-size: 15px;
                              }
                              #boton_nueva_enfermedad:hover{
                                   background-color: #3D9DB8;
                                color:papayawhip;
                                padding: 5px 10px;
                                border-radius:10px;
                                font-size: 15px;
                              }
                           
                           QTableWidget {

                                gridline-color: #999999;
                                font-size: 14px;
                            }
                            QHeaderView::section {
                                background-color: #E3D1C9;
                                color: black;
                                padding: 4px;
                                font-weight: bold;
                            }
                            QTableWidget::item:selected {
                                background-color: #AA8B7E;
                                color: white;
                            }
                            """)


        
class FormularioNuevaEnfermedad(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('FormularioEnfermedad')
        self.setGeometry(100,100,400,300)
        self.w = dict()
        self.w['label_nombre_enfermedad'] = QLabel('Nombre: ')
        self.w['input_nombre_enfermedad'] = QLineEdit()
        self.w['label_descripcion'] = QLabel('Descripcion: ')
        self.w['input_descripcion'] = QLineEdit()
        self.w['label_causa'] = QLabel('Causa: ')
        self.w['input_causa'] = QLineEdit()
        self.w['label_tratamiento'] = QLabel('Tratamiento: ')
        self.w['input_tratamiento'] = QLineEdit()


        self.w['btn_guardar'] = QPushButton('Guardar')
        self.w['btn_guardar'].setObjectName("boton_guardar")
        self.layout_principal = QVBoxLayout()
       
        for w in self.w.values():
           self.layout_principal.addWidget(w)

        self.setLayout(self.layout_principal)

        self.w['btn_guardar'].clicked.connect(self.accept)

        self.setStyleSheet("""
                           #boton_guardar{
                                background-color: #E3D1C9;
                                font-weight:bold;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;

                           }
                           #boton_guardar:hover {
                                background-color:#AA8B7E;
                                color:papayawhip;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;
                           }
                            """)
        
    def limpiar_campos(self):
        self.w['input_nombre_enfermedad'].clear()
        self.w['input_descripcion'].clear()
        self.w['input_causa'].clear()
        self.w['input_tratamiento'].clear()

class FormularioTop10(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Top10')
        self.setGeometry(400,400,700,600)
        self.w = dict()

        
        self.w['label_fecha_referencia'] = QLabel('Fecha: ')
        self.w['input_fecha_referencia'] = QLineEdit()

        self.w['btn_top10']=QPushButton("Top 10")
        self.w['btn_top10'].setObjectName("boton_top_10")

        self.w['tabla_top10'] = QTableWidget()

        self.layout_principal = QVBoxLayout()
       
        for w in self.w.values():
           self.layout_principal.addWidget(w)

        self.setLayout(self.layout_principal)

        self.setStyleSheet("""
                            #boton_top_10{
                                background-color: #b7e4c7;
                                font-weight:bold;
                                padding: 5px 10px;
                                border-radius:10px;
                                font-size: 15px;
                           }

                           #boton_top_10:hover{
                                background-color: #74c69d;
                                color:papayawhip;
                                padding: 5px 10px;
                                border-radius:10px;
                                font-size: 15px;
                           }

                           QTableWidget {

                                gridline-color: #999999;
                                font-size: 14px;
                            }
                            QHeaderView::section {
                                background-color: #E3D1C9;
                                color: black;
                                padding: 4px;
                                font-weight: bold;
                            }
                            QTableWidget::item:selected {
                                background-color: #AA8B7E;
                                color: white;
                            }
                           
                            """)
        
    def limpiar_campos(self):
        self.w['input_fecha_referencia'].clear()

    def closeEvent(self, event):
        self.w['tabla_top10'].clear()
        self.w['tabla_top10'].setRowCount(0)
        self.w['tabla_top10'].setColumnCount(0)
        event.accept()

class FormularioModificarEnfermedad(QDialog):
    def __init__(self):
        super().__init__()
        
        self.id_enfermedad_update:int

        
        self.setWindowTitle('FormularioModificarEnfermedad')
        self.setGeometry(100,100,400,300)
        self.w = dict()
        self.w['label_id'] = QLabel("")      
        self.w['label_nombre_enfermedad'] = QLabel('Nuevo nombre: ')
        self.w['input_nombre_enfermedad'] = QLineEdit()
        self.w['label_descripcion'] = QLabel('Nueva descripcion:')
        self.w['input_descripcion'] = QLineEdit()
        self.w['label_causa'] = QLabel('Nueva causa:')
        self.w['input_causa'] = QLineEdit()
        self.w['label_tratamiento'] = QLabel('Nuevo tratamiento:')
        self.w['input_tratamiento'] = QLineEdit()


        self.w['btn_guardar'] = QPushButton('Guardar')
        self.w['btn_guardar'].setObjectName("boton_guardar")
        self.layout_principal = QVBoxLayout()
       
        for w in self.w.values():
           self.layout_principal.addWidget(w)

        self.setLayout(self.layout_principal)

        self.w['btn_guardar'].clicked.connect(self.accept)

        self.setStyleSheet("""
                           #boton_guardar{
                                background-color: #E3D1C9;
                                font-weight:bold;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;

                           }
                           #boton_guardar:hover {
                                background-color:#AA8B7E;
                                color:papayawhip;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;
                           }
                            """)
        
class FormularioModificarDiagnostico(QDialog):
    def __init__(self):
        super().__init__()
        
        self.id_Arbol_Enfermedad_update:int

        
        self.setWindowTitle('FormularioModificarDiagnostico')
        self.setGeometry(100,100,400,300)
        self.w = dict()
        self.w['label_id'] = QLabel("")      
        self.w['label_id_arbol'] = QLabel('Nuevo id arbol: ')
        self.w['input_id_arbol'] = QLineEdit()
        self.w['label_id_enfermedad'] = QLabel('Nuevo id enfermedad:')
        self.w['input_id_enfermedad'] = QLineEdit()
        self.w['label_fecha_diagnostico'] = QLabel('Nueva fecha:')
        self.w['input_fecha_diagnostico'] = QLineEdit()



        self.w['btn_guardar'] = QPushButton('Guardar')
        self.w['btn_guardar'].setObjectName("boton_guardar")
        self.layout_principal = QVBoxLayout()
       
        for w in self.w.values():
           self.layout_principal.addWidget(w)

        self.setLayout(self.layout_principal)

        self.w['btn_guardar'].clicked.connect(self.accept)

        self.setStyleSheet("""
                           #boton_guardar{
                                background-color: #E3D1C9;
                                font-weight:bold;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;

                           }
                           #boton_guardar:hover {
                                background-color:#AA8B7E;
                                color:papayawhip;
                                padding: 5px 15px;
                                border-radius:15px;
                                font-size: 15px;
                           }
                            """)
        