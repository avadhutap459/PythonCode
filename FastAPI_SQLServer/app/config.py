from urllib.parse import quote_plus

connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    r"SERVER=(localdb)\MSSQLLocalDB;"
    "DATABASE=FastAPIDB;"
    "Trusted_Connection=yes;"
    "Encrypt=no;"
)


DATABASE_URL = (
    "mssql+pyodbc:///?odbc_connect="
    + quote_plus(connection_string)
)
