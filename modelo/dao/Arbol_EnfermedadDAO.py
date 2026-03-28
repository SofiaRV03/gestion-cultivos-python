from __future__ import annotations
from modelo.vo.Arbol_EnfermedadVO import Arbol_EnfermedadVO
from typing import Optional, List
from db.conexion import crear_conexion, ubicacionBD


class Arbol_EnfermedadDAO:
    def __init__(self):        
        self.conector = crear_conexion(rutaBD=ubicacionBD)   

    def adicionar_Arbol_Enfermedad(self, Arbol_Enfermedad:Arbol_EnfermedadVO):
        sql = f"""
        INSERT INTO Arbol_Enfermedad (
            id_arbol,
            id_enfermedad,
            fecha_diagnostico   
        )
        VALUES (
            ?,
            ?,
            ?     
        );        
        """ 
        cursor = self.conector.cursor()
        cursor.execute(sql,(Arbol_Enfermedad.id_arbol,Arbol_Enfermedad.id_enfermedad, Arbol_Enfermedad.fecha_diagnostico,))
        self.conector.commit()

    def modificar_arbol_enfermedad(self,arbol_enfermedad:Arbol_EnfermedadVO):
        sql = f"""
            UPDATE Arbol_Enfermedad
            SET id_arbol = ?, id_enfermedad=?, fecha_diagnostico=?
            WHERE id_Arbol_Enfermedad = ?;
            """ 
        cursor = self.conector.cursor()
        cursor.execute(sql,(arbol_enfermedad.id_arbol,arbol_enfermedad.id_enfermedad, arbol_enfermedad.fecha_diagnostico, arbol_enfermedad.id_Arbol_Enfermedad))
        self.conector.commit()