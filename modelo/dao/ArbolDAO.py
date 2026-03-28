from __future__ import annotations
from modelo.vo.ArbolVO import ArbolVO
from typing import Optional, List
from db.conexion import crear_conexion, ubicacionBD


class ArbolDAO:
    def __init__(self):        
        self.conector = crear_conexion(rutaBD=ubicacionBD)
        
    def get_all(self):        
        sql = "SELECT * FROM Arbol order by id_arbol desc;"        
        cursor = self.conector.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        arboles = list()
        for registro in registros:
            arboles.append(ArbolVO(id_arbol=registro[0], 
                                   fecha_siembra=registro[1]
                                   ))
            
            
        return arboles
        
    def adicionar_arbol(self, arbol:ArbolVO):
        sql = f"""
        INSERT INTO Arbol (
            fecha_siembra         
        )
        VALUES (
            ?          
        );        
        """ 
        cursor = self.conector.cursor()
        cursor.execute(sql,(arbol.fecha_siembra,))
        self.conector.commit()

    
    
    def modificar_arbol(self,arbol:ArbolVO):
        sql = f"""
            UPDATE Arbol
            SET fecha_siembra = ?
            WHERE id_arbol = ?;
            """ 
        cursor = self.conector.cursor()
        cursor.execute(sql,(arbol.fecha_siembra, arbol.id_arbol))
        self.conector.commit()
