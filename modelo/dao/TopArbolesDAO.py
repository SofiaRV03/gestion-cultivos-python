from __future__ import annotations
from modelo.vo.FumigacionVO import FumigacionVO
from modelo.vo.ArbolVO import ArbolVO
from modelo.vo.TrabajadorVO import TrabajadorVO
from modelo.vo.EnfermedadVO import EnfermedadVO
from typing import Optional, List
from db.conexion import crear_conexion, ubicacionBD
from modelo.vo.TopArbolesVO import TopArbolesVO


class TopArbolesDAO:
    def __init__(self):        
        self.conector = crear_conexion(rutaBD=ubicacionBD)    

    def obtener_top_10_arboles_por_calidad(self,top_arboles:TopArbolesVO):
        sql = f"""SELECT 
                    Arbol.id_arbol,
                    Arbol.fecha_siembra,
                    Recolecta.calidad,
                    SUM(Recolecta.peso) AS produccion_por_calidad,
                    (
                        SELECT SUM(Recolecta_sub.peso)
                        FROM Recolecta AS Recolecta_sub
                        JOIN Produccion AS Produccion_sub 
                            ON Recolecta_sub.id_produccion = Produccion_sub.id_produccion
                        WHERE Recolecta_sub.id_arbol = Arbol.id_arbol
                    ) AS produccion_total
                FROM Arbol
                JOIN Recolecta 
                    ON Arbol.id_arbol = Recolecta.id_arbol
                JOIN Produccion 
                    ON Recolecta.id_produccion = Produccion.id_produccion
                WHERE Arbol.fecha_siembra BETWEEN DATE('{top_arboles.fecha_referencia}', '-5 years') AND '{top_arboles.fecha_referencia}'
                AND Arbol.id_arbol IN (
                        SELECT id_arbol
                        FROM (
                            SELECT 
                                Arbol.id_arbol,
                                SUM(Recolecta.peso) AS produccion_total
                            FROM Arbol
                            JOIN Recolecta 
                                ON Arbol.id_arbol = Recolecta.id_arbol
                            JOIN Produccion 
                                ON Recolecta.id_produccion = Produccion.id_produccion
                            WHERE Arbol.fecha_siembra BETWEEN DATE('{top_arboles.fecha_referencia}', '-5 years') AND '{top_arboles.fecha_referencia}'
                            GROUP BY Arbol.id_arbol
                            ORDER BY produccion_total DESC
                            LIMIT 10
                        )
                    )
                GROUP BY Arbol.id_arbol, Recolecta.calidad
                ORDER BY produccion_total DESC, produccion_por_calidad DESC;


        """
        cursor = self.conector.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        top = list()
        for registro in registros:
            top.append(TopArbolesVO(
                id_arbol=registro[0],
                fecha_siembra=registro[1],
                calidad=registro[2],
                total_por_calidad=registro[3],
                total_general=registro[4]
            ))

        return top


