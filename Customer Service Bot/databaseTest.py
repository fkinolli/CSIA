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







#-------------------------------------------------------------------------------

##https://www.youtube.com/watch?v=jA1GO6g_Rw0
##--++ Selecting and Getting Data ++--
##selects specific column to be displayed
#mycursor.execute("SELECT name FROM users")

##selects all columns to be displayed
#mycursor.execute("SELECT * FROM users")

##fetches all entrys
#myresult = mycursor.fetchall()

##fetches one entry, usually first row
#myresult = mycursor.fetchone()

##printing fetched data
#for row in myresult:
#    print(row)

#-------------------------------------------------------------------------------

##https://www.youtube.com/watch?v=BfXhZDNlXy8
##--++ Template for automatic data insertion through inputted variables
##takes in user credentials
#name = input("Name: ")
#password = input("Password: ")
#email = input("Email: ")

##is the command for inputting data into database
#mycursor = mydb.cursor()
#sqlformula = "INSERT INTO users (name, password, email) VALUES (%s, %s, %s)"
#user = (name, password, email)

##executes both sqlformula and user in order to send data to database
#mycursor.execute(sqlformula, user)

##needed to finalize entry, similar to commiting on github,etc.
#mydb.commit()

#-------------------------------------------------------------------------------

##https://www.youtube.com/watch?v=BfXhZDNlXy8
##--++ Template for inserting data ++--
#sqlformula = "INSERT INTO users (name, password, email) VALUES (%s, %s, %s)"

##manualling inserting data, needs to be replaced with variables user inputs
#user1 = ("Jeff", "jeff2002", "jeff@gmail.com")

##executes both sqlformula and user1 in order to send data to database
#mycursor.execute(sqlformula, user1)

##needed to finalize entry, similar to commiting on github,etc.
#mydb.commit()

#-------------------------------------------------------------------------------

##--++ For printing out all db's ++--
#for db in mycursor:
#    print(db)

# For Checking Db Connection
#print(db)
