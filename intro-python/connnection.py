import MySQLdb

# Conexión a Base de Datos
hostname = '34.70.106.43'
username = 'root'
password = 'instance_1'
database = 'ddbb_1'

# Correr query:

def doQuery( conn ) :
    cur = conn.cursor()

    cur.execute( "SELECT id, name FROM ddbb_1.developer d " )

    for id, name  in cur.fetchall() :
        print(id, name)


print( "Using mysqlclient (MySQLdb):" )
myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
print(myConnection)

print( "Executing Query:" )
doQuery( myConnection )

myConnection.close()
print(myConnection)