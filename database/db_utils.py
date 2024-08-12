import mysql.connector
from config import DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME

def connect_to_db():
    """Connects to the MySQL database."""
    try:
        conn = mysql.connector.connect(
            host=DATABASE_HOST,
            user=DATABASE_USER,
            password=DATABASE_PASSWORD,
            database=DATABASE_NAME
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        return None
    

def execute_query(query, data=None):
    """Executes a SQL query and returns the results."""
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            if data:
                cursor.execute(query, data)
            else:
                cursor.execute(query)
            
            if cursor.with_rows:
                results = cursor.fetchall()
            else:
                results = None
            
            conn.commit()
            return results  # Return the fetched results directly
            
        except mysql.connector.Error as err:
            print(f"Error executing query: {err}")
            return None
        finally:
            if cursor:
                cursor.close()  # Ensure the cursor is closed
            if conn:
                conn.close()    # Ensure the connection is closed
    else:
        print("No connection available to execute query.")
        return None