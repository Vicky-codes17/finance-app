import psycopg2

DB_name = "finance_app"
DB_user = "postgres"
DB_password = "07042006"
DB_host = "localhost"
DB_port = "5432"

try:
    conn = psycopg2.connect(
        dbname=DB_name,
        user=DB_user,
        password=DB_password,
        host=DB_host,
        port=DB_port
    )
    print("Connection established")
except psycopg2.Error as e:
    print(e)
finally:    
    if conn:
        conn.close()
        print("Connection closed")