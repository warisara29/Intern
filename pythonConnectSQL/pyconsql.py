import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'localhost\SQLEXPRESS' 
database = 'dbTest' 
username = 'admin' 
password = 'admin12345' 
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()

#create table
cursor.execute('DROP TABLE IF EXISTS series') #check if there is already had data table delete it
cursor.execute('create table series (name TEXT, age Integer)')
conn.commit()

#insert data to table
cursor.execute('insert into data(name, age)values(?,?)', ('Dora', 17))
conn.commit()

#select data from table
cursor.execute('select * from data')
for row in cursor:
    print("data from table are" , row)
conn.close()
