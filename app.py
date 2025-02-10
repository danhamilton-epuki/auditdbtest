from flask import Flask
import pyodbc

app = Flask(__name__)

# SQL Server connection details
server = 'corsqltst'
database = 'BPS_Custom'
username = 'bms_read'
password = 'TangoTabRipple4£'
driver = '{ODBC Driver 17 for SQL Server}'

@app.route('/')
def index():
    try:
        # Connect to the database
        conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')
        cursor = conn.cursor()
        
        # Execute a sample SQL query
        cursor.execute("SELECT TOP 1 name FROM sys.tables")
        row = cursor.fetchone()
        
        if row:
            return f"Connected! First table name: {row[0]}"
        else:
            return "Connected, but no tables found."

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(debug=True)
