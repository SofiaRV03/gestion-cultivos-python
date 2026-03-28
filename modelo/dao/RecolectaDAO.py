from __future__ import annotations
from modelo.vo.NutricionVO import NutricionVO
from modelo.vo.ArbolVO import ArbolVO
from modelo.vo.TrabajadorVO import TrabajadorVO
from modelo.vo.RecolectaVO import RecolectaVO
from typing import Optional, List
from db.conexion import crear_conexion, ubicacionBD


class RecolectaDAO:
    def __init__(self):        
        self.conector = crear_conexion(rutaBD=ubicacionBD)
        
    def get_all(self):        
        sql = "SELECT * FROM Recolecta order by id_recolecta desc;"        
        cursor = self.conector.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        recolectas = list()
        for registro in registros:
            recolectas.append(RecolectaVO(id_recolecta=registro[0], 
                                   fecha_recolecta=registro[1],
                                   calidad=registro[2],
                                   peso=registro[3],
                                   id_trabajador=registro[4],
                                   id_arbol=registro[5],
                                   id_produccion=registro[6],
                                   ))
            
            
        return recolectas
    
    def mostrar_recolectas_arbol(self,arbol:ArbolVO):        
        sql = f"SELECT * FROM Recolecta where id_arbol={arbol.id_arbol} order by id_recolecta desc;"        
        cursor = self.conector.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        recolectas = list()
        for registro in registros:
            recolectas.append(RecolectaVO(id_recolecta=registro[0], 
                                   fecha_recolecta=registro[1],
                                   calidad=registro[2],
                                   peso=registro[3],
                                   id_trabajador=registro[4],
                                   id_arbol=registro[5],
                                   id_produccion=registro[6],
                                   ))
            
            
        return recolectas
    
    def mostrar_recolectas_trabajador(self,trabajador:TrabajadorVO):        
        sql = f"SELECT * FROM Recolecta where id_trabajador={trabajador.id_trabajador} order by id_recolecta desc;"        
        cursor = self.conector.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        print(registros)
        recolectas = list()
        for registro in registros:
            recolectas.append(RecolectaVO(id_recolecta=registro[0], 
                                   fecha_recolecta=registro[1],
                                   calidad=registro[2],
                                   peso=registro[3],
                                   id_trabajador=registro[4],
                                   id_arbol=registro[5],
                                   id_produccion=registro[6],
                                   ))
            
            
        return recolectas
    

    def adicionar_recolecta(self, recolecta:RecolectaVO):
        sql = f"""
        INSERT INTO Recolecta (
            fecha_recolecta,
            calidad,
            peso,
            id_trabajador,
            id_arbol,
            id_produccion        
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
        cursor.execute(sql,(recolecta.fecha_recolecta,recolecta.calidad, recolecta.peso,recolecta.id_trabajador, recolecta.id_arbol, recolecta.id_produccion,))
        self.conector.commit()

    def modificar_recolecta(self,recolecta:RecolectaVO):
        sql = f"""
            UPDATE Recolecta
            SET fecha_recolecta = ?, calidad=?, peso=?, id_trabajador=?, id_arbol=?, id_produccion=?
            WHERE id_recolecta = ?;
            """ 
        cursor = self.conector.cursor()
        cursor.execute(sql,(recolecta.fecha_recolecta,recolecta.calidad, recolecta.peso,recolecta.id_trabajador, recolecta.id_arbol, recolecta.id_produccion,recolecta.id_recolecta))
        self.conector.commit()
    
    
