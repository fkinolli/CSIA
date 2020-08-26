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

##https://www.youtube.com/watch?v=OTzL0oH-ZGI
##--++ Query Conditions with WHERE and Wildcards ++--

##Searching with conditions
#sql = "SELECT * FROM users WHERE name ='Fabio'"
#mycursor.execute(sql)
#myresult = mycursor.fetchall()
#
#for result in myresult:
#    print(result)

##Searaching with wildcards where the % sign is the wild card, in this case anything beginning with F would be displayed.
#sql = "SELECT * FROM users WHERE name LIKE 'F%'"
#mycursor.execute(sql)
#myresult = mycursor.fetchall()

#for result in myresult:
#    print(result)

##Always good to use placeholders("%s") and then passing in values as this is safer and more secure from sqlInjection attacks, need to be passed through a little different as seen in the execute command below.
#sql = "SELECT * FROM users WHERE name LIKE %s"
#mycursor.execute(sql, ('F%', ))
#myresult = mycursor.fetchall()
#
#for result in myresult:
#    print(result)

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
##--++ Template for automatic data insertion through inputted variables ++--

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
