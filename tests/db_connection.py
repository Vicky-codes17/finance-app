import psycopg2

DB_name = "finance_app"
DB_user = "postgres"
DB_password = "07042006"
DB_host = "localhost"
DB_port = "5432"

try:
    conn = psycopg2.connect(
        dbname= finance_app,
        user= postgresql,
        password= 07042006,
        host= postgresql,
        port= 5432
    )
    print("Connection established")
except psycopg2.Error as e:
    print(e)
finally:    
    if conn:
        conn.close()
        print("Connection closed")