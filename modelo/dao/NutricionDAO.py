from __future__ import annotations
from modelo.vo.NutricionVO import NutricionVO
from modelo.vo.ArbolVO import ArbolVO
from modelo.vo.TrabajadorVO import TrabajadorVO
from typing import Optional, List
from db.conexion import crear_conexion, ubicacionBD


class NutricionDAO:
    def __init__(self):        
        self.conector = crear_conexion(rutaBD=ubicacionBD)
        
    def get_all(self):        
        sql = "SELECT * FROM Nutricion order by id_nutricion desc;"        
        cursor = self.conector.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        nutriciones = list()
        for registro in registros:
            nutriciones.append(NutricionVO(id_nutricion=registro[0], 
                                   fecha_nutricion=registro[1],
                                   mezcla_nutricion=registro[2],
                                   id_trabajador=registro[3],
                                   id_arbol=registro[4]
                                   ))
            
            
        return nutriciones
    
    def mostrar_nutriciones_arbol(self,arbol:ArbolVO):        
        sql = f"SELECT * FROM Nutricion where id_arbol={arbol.id_arbol} order by id_nutricion desc;"        
        cursor = self.conector.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        nutriciones = list()
        for registro in registros:
            nutriciones.append(NutricionVO(id_nutricion=registro[0], 
                                   fecha_nutricion=registro[1],
                                   mezcla_nutricion=registro[2],
                                   id_trabajador=registro[3],
                                   id_arbol=registro[4]
                                   ))
            
            
        return nutriciones
    
    def mostrar_nutriciones_trabajador(self,trabajador:TrabajadorVO):        
        sql = f"SELECT * FROM Nutricion where id_trabajador={trabajador.id_trabajador} order by id_nutricion desc;"        
        cursor = self.conector.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        nutriciones = list()
        for registro in registros:
            nutriciones.append(NutricionVO(id_nutricion=registro[0], 
                                   fecha_nutricion=registro[1],
                                   mezcla_nutricion=registro[2],
                                   id_trabajador=registro[3],
                                   id_arbol=registro[4]
                                   ))
            
            
        return nutriciones
    

    def adicionar_nutricion(self, nutricion:NutricionVO):
        sql = f"""
        INSERT INTO Nutricion (
            fecha_nutricion,
            mezcla_nutricion,
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
        cursor.execute(sql,(nutricion.fecha_nutricion,nutricion.mezcla_nutricion, nutricion.id_trabajador, nutricion.id_arbol,))
        self.conector.commit()

    def modificar_nutricion(self,nutricion:NutricionVO):
        sql = f"""
            UPDATE Nutricion
            SET fecha_nutricion = ?, mezcla_nutricion=?, id_trabajador=?, id_arbol=?
            WHERE id_nutricion = ?;
            """ 
        cursor = self.conector.cursor()
        cursor.execute(sql,(nutricion.fecha_nutricion, nutricion.mezcla_nutricion, nutricion.id_trabajador, nutricion.id_arbol, nutricion.id_nutricion))
        self.conector.commit()
    
    
