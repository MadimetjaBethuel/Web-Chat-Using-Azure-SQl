import textwrap
import pyodbc


server = 'tcp:webapplication.database.windows.net'
database = 'chatapp'
username = 'ApplicationAdmin'
password = 'Accounts@madimetja2021'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                      server+';DATABASE='+database+';UID='+username+';PWD=' + password)
cursor = cnxn.cursor()
