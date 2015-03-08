## 
import cx_Oracle,csv
conn=cx_Oracle.connect('','','dm01-scan.prod.lan:7381/oraprod')
curs=conn.cursor()
curs.execute("alter session set nls_date_format='DD-MON-YYYY'")
entities=curs.execute("select eno, geom from a.entities where entity_type='DRILLHOLE'").fetchall()
duplicates = list()
for entity in entities:
    geom = entity[1]
    if geom is not None:
        search = to_sdo_string(geom)
        stmt = "select * from a.entities e where sdo_equal(e.geom,{0})=\'TRUE\'".format(search)
        results=curs.execute(stmt).fetchall()
        if results.__len__() > 1:
            duplicates.append(results)
            print results
    
def to_sdo_string(geom):
    if geom is None:
        return "NULL"
    if geom.type.__str__() == '<cx_Oracle.ObjectType MDSYS.SDO_GEOMETRY>':
        gtype = geom.SDO_GTYPE.__int__()
        point = to_sdo_string(geom.SDO_POINT)
        srid = geom.SDO_SRID.__int__()
        element_info = to_sdo_string(geom.SDO_ELEM_INFO)
        ordinates = to_sdo_string(geom.SDO_ORDINATES)
        return 'SDO_GEOMETRY({0},{1},{2},{3},{4})'.format(gtype,srid,point,element_info,ordinates)
    if geom.type.__str__() == '<cx_Oracle.ObjectType MDSYS.SDO_POINT_TYPE>':
        if geom.Z is None:
            return "SDO_POINT_TYPE({0},{1},NULL)".format(geom.X,geom.Y)
        else:
            return "SDO_POINT_TYPE({0},{1},{2})".format(geom.X,geom.Y,geom.Z)
    
    
        
