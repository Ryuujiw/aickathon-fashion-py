import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  auth_plugin='mysql_native_password',
  
)

print(mydb)