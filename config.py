import textwrap
import pyodbc


server = 'your server name'
database = 'database name'
username = 'username'
password = 'password'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                      server+';DATABASE='+database+';UID='+username+';PWD=' + password)
cursor = cnxn.cursor()
