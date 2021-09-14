import MySQLdb

# Conexión a Base de Datos
hostname = 'pre-production.clojpf4eargq.us-east-2.rds.amazonaws.com'
username = 'yapp_evelyn'
password = 'Em36Y22p'
database = 'yapp_pap'

# Correr query:

def doQuery( conn ) :
    cur = conn.cursor()

    cur.execute( "select id, name from yapp_pap.product where id = 3" )

    for id, name  in cur.fetchall() :
        print( id, name )

print( "Using mysqlclient (MySQLdb):" )

myConnection = MySQLdb.connect( host=hostname, user=username, passwd=password, db=database )
doQuery( myConnection )

print(myConnection)
myConnection.close()
print(myConnection)