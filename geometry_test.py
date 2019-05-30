import cx_Oracle,csv
conn=cx_Oracle.connect('','','dm01-scan.prod.lan:7381/oraprod')
curs=conn.cursor()
curs.execute("alter session set nls_date_format='DD-MON-YYYY'")
enos=curs.execute("select eno from a.entities").fetchall()
with open("geometry_test.csv","wb") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["ENO", "ENTITYID", "ENTITY_TYPE", "enteredby", "entrydate","validated"])
    for eno in enos:
        x=curs.execute('select  eno, entityid, entity_type, enteredby, sdo_geom.validate_geometry(e.geom,0.0000000001) from a.entities e where eno = :arg',arg=eno[0]).fetchall()
        csv_writer.writerows(x)
 
#
