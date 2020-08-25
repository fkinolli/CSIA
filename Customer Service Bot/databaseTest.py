# Library for connecting
import mysql.connector

# Connecting to the Database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="CSIA"
)

mycursor = mydb.cursor()



# For printing out all db's
#for db in mycursor:
#    print(db)

# For Checking Db Connection
#print(db)
