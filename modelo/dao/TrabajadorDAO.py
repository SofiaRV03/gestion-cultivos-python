from __future__ import annotations
from modelo.vo.TrabajadorVO import TrabajadorVO
from typing import Optional, List
from db.conexion import crear_conexion, ubicacionBD


class TrabajadorDAO:
    def __init__(self):        
        self.conector = crear_conexion(rutaBD=ubicacionBD)
        
    def get_all(self):        
        sql = "SELECT * FROM Trabajador order by fecha_creacion desc;"        
        cursor = self.conector.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        trabajadores = list()
        for registro in registros:
            trabajadores.append(TrabajadorVO(id_trabajador=registro[0], 
                                   nombre=registro[1],
                                   telefono=registro[2],
                                   EPS=registro[3],
                                   ARL=registro[4],
                                   fecha_creacion=registro[5]
                                   ))
            
            
        return trabajadores
    
    def adicionar_trabajador(self, trabajador:TrabajadorVO):
        sql = f"""
            INSERT INTO Trabajador (
                id_trabajador,
                nombre,           
                Telefono,          
                EPS,                          
                ARL,
                fecha_creacion
            )
            VALUES (
                ?,
                ?,           
                ?,          
                ?,                   
                ?,
                ?     
            );        
            """ 
        cursor = self.conector.cursor()
        cursor.execute(sql,(trabajador.id_trabajador,trabajador.nombre, trabajador.telefono, trabajador.EPS, trabajador.ARL, trabajador.fecha_creacion))
        self.conector.commit()

    def modificar_trabajador(self,trabajador:TrabajadorVO):
        sql = f"""
            UPDATE Trabajador
            SET nombre = ?, telefono=?, EPS=?, ARL=?, fecha_creacion=?
            WHERE id_trabajador = ?;
            """ 
        cursor = self.conector.cursor()
        cursor.execute(sql,(trabajador.nombre, trabajador.telefono, trabajador.EPS, trabajador.ARL,trabajador.fecha_creacion,trabajador.id_trabajador))
        self.conector.commit()

        

    