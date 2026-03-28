from __future__ import annotations
from modelo.vo.FumigacionVO import FumigacionVO
from modelo.vo.ArbolVO import ArbolVO
from modelo.vo.TrabajadorVO import TrabajadorVO
from modelo.vo.DiagnosticoVO import DiagnosticoVO
from typing import Optional, List
from db.conexion import crear_conexion, ubicacionBD


class DiagnosticoDAO:
    def __init__(self):        
        self.conector = crear_conexion(rutaBD=ubicacionBD)
        
    def get_all(self):        
        sql = "SELECT Arbol_Enfermedad.id_Arbol_Enfermedad, Arbol.id_arbol, Enfermedad.id_enfermedad, Enfermedad.nombre_enfermedad, Enfermedad.descripcion, Enfermedad.causa, Enfermedad.tratamiento, Arbol_Enfermedad.fecha_diagnostico FROM Arbol join Arbol_Enfermedad on Arbol.id_arbol=Arbol_Enfermedad.id_arbol join Enfermedad on Arbol_Enfermedad.id_enfermedad=Enfermedad.id_enfermedad;"        
        cursor = self.conector.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        diagnosticos = list()
        for registro in registros:
            diagnosticos.append(DiagnosticoVO(id_Arbol_Enfermedad=registro[0],
                                    id_arbol=registro[1], 
                                   id_enfermedad=registro[2],
                                   nombre_enfermedad=registro[3],
                                   descripcion=registro[4],
                                   causa=registro[5],
                                   tratamiento=registro[6],
                                   fecha_diagnostico=registro[7]

                                   ))
            
            
        return diagnosticos
    

    def mostrar_diagnostico_id_arbol(self,arbol:ArbolVO): 
        sql = f"SELECT Arbol_Enfermedad.id_Arbol_Enfermedad, Arbol.id_arbol, Enfermedad.id_enfermedad, Enfermedad.nombre_enfermedad, Enfermedad.descripcion, Enfermedad.causa, Enfermedad.tratamiento, Arbol_Enfermedad.fecha_diagnostico FROM Arbol join Arbol_Enfermedad on Arbol.id_arbol=Arbol_Enfermedad.id_arbol join Enfermedad on Arbol_Enfermedad.id_enfermedad=Enfermedad.id_enfermedad where Arbol.id_arbol={arbol.id_arbol};"               
        cursor = self.conector.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        print(registros)
        diagnosticos = list()
        for registro in registros:
            diagnosticos.append(DiagnosticoVO(id_Arbol_Enfermedad=registro[0],
                                    id_arbol=registro[1], 
                                   id_enfermedad=registro[2],
                                   nombre_enfermedad=registro[3],
                                   descripcion=registro[4],
                                   causa=registro[5],
                                   tratamiento=registro[6],
                                   fecha_diagnostico=registro[7]

                                   ))
            
            
        return diagnosticos
    


    
    



    
    
