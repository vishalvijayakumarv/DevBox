import psycopg2

def test_postgres():
    try:
        conn = psycopg2.connect(
            dbname="testdb",
            user="admin",
            password="password",
            host="localhost",
            port=5432
        )
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, data TEXT);")
        cursor.execute("INSERT INTO test_table (data) VALUES ('Hello, PostgreSQL!');")
        conn.commit()
        cursor.execute("SELECT * FROM test_table;")
        for row in cursor.fetchall():
            print(f"Row: {row}")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"PostgreSQL error: {e}")

if __name__ == "__main__":
    test_postgres()