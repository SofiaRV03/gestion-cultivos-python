from __future__ import annotations
from modelo.vo.FumigacionVO import FumigacionVO
from modelo.vo.ArbolVO import ArbolVO
from modelo.vo.TrabajadorVO import TrabajadorVO
from modelo.vo.EnfermedadVO import EnfermedadVO
from typing import Optional, List
from db.conexion import crear_conexion, ubicacionBD


class EnfermedadDAO:
    def __init__(self):        
        self.conector = crear_conexion(rutaBD=ubicacionBD)    

    def get_all(self):
        sql = "SELECT * FROM Enfermedad"
        cursor = self.conector.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        enfermedades = list()
        for registro in registros:
            enfermedades.append(EnfermedadVO(
                id_enfermedad=registro[0],
                nombre_enfermedad=registro[1],
                descripcion=registro[2],
                causa=registro[3],
                tratamiento=registro[4]
            ))


        return enfermedades
    
    def adicionar_enfermedad(self, enfermedad:EnfermedadVO):
        sql = f"""
        INSERT INTO Enfermedad (
            nombre_enfermedad,
            descripcion,
            causa,
            tratamiento        
        )
        VALUES (
            ?,
            ?,
            ?,
            ?
                  
        );        
        """ 
        cursor = self.conector.cursor()
        cursor.execute(sql,(enfermedad.nombre_enfermedad,enfermedad.descripcion, enfermedad.causa, enfermedad.tratamiento,))
        self.conector.commit()


    def modificar_enfermedad(self,enfermedad:EnfermedadVO):
        sql = f"""
            UPDATE Enfermedad
            SET nombre_enfermedad = ?, descripcion=?, causa=?, tratamiento=?
            WHERE id_enfermedad = ?;
            """ 
        cursor = self.conector.cursor()
        cursor.execute(sql,(enfermedad.nombre_enfermedad, enfermedad.descripcion, enfermedad.causa, enfermedad.tratamiento, enfermedad.id_enfermedad))
        self.conector.commit()