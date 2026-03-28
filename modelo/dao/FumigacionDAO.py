from __future__ import annotations
from modelo.vo.FumigacionVO import FumigacionVO
from modelo.vo.ArbolVO import ArbolVO
from modelo.vo.TrabajadorVO import TrabajadorVO
from typing import Optional, List
from db.conexion import crear_conexion, ubicacionBD


class FumigacionDAO:
    def __init__(self):        
        self.conector = crear_conexion(rutaBD=ubicacionBD)
        
    def get_all(self):        
        sql = "SELECT * FROM Fumigacion order by id_fumigacion desc;"        
        cursor = self.conector.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        fumigaciones = list()
        for registro in registros:
            fumigaciones.append(FumigacionVO(id_fumigacion=registro[0], 
                                   fecha_fumigacion=registro[1],
                                   mezcla_fumigacion=registro[2],
                                   id_trabajador=registro[3],
                                   id_arbol=registro[4]
                                   ))
            
            
        return fumigaciones
    
    def mostrar_fumigaciones_arbol(self,arbol:ArbolVO):        
        sql = f"SELECT * FROM Fumigacion where id_arbol={arbol.id_arbol} order by id_fumigacion desc;"        
        cursor = self.conector.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        fumigaciones = list()
        for registro in registros:
            fumigaciones.append(FumigacionVO(id_fumigacion=registro[0], 
                                   fecha_fumigacion=registro[1],
                                   mezcla_fumigacion=registro[2],
                                   id_trabajador=registro[3],
                                   id_arbol=registro[4]
                                   ))
            
            
        return fumigaciones
    
    def mostrar_fumigaciones_trabajador(self,trabajador:TrabajadorVO):        
        sql = f"SELECT * FROM Fumigacion where id_trabajador={trabajador.id_trabajador} order by id_fumigacion desc;"        
        cursor = self.conector.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        fumigaciones = list()
        for registro in registros:
            fumigaciones.append(FumigacionVO(id_fumigacion=registro[0], 
                                   fecha_fumigacion=registro[1],
                                   mezcla_fumigacion=registro[2],
                                   id_trabajador=registro[3],
                                   id_arbol=registro[4]
                                   ))
            
            
        return fumigaciones
    

    def adicionar_fumigacion(self, fumigacion:FumigacionVO):
        sql = f"""
        INSERT INTO Fumigacion (
            fecha_fumigacion,
            mezcla_fumigacion,
            id_trabajador,
            id_arbol        
        )
        VALUES (
            ?,
            ?,
            ?,
            ?
                  
        );        
        """ 
        cursor = self.conector.cursor()
        cursor.execute(sql,(fumigacion.fecha_fumigacion,fumigacion.mezcla_fumigacion, fumigacion.id_trabajador, fumigacion.id_arbol,))
        self.conector.commit()

    def modificar_fumigacion(self,fumigacion:FumigacionVO):
        sql = f"""
            UPDATE Fumigacion
            SET fecha_fumigacion = ?, mezcla_fumigacion=?, id_trabajador=?, id_arbol=?
            WHERE id_fumigacion = ?;
            """ 
        cursor = self.conector.cursor()
        cursor.execute(sql,(fumigacion.fecha_fumigacion, fumigacion.mezcla_fumigacion, fumigacion.id_trabajador, fumigacion.id_arbol, fumigacion.id_fumigacion))
        self.conector.commit()
    
    
