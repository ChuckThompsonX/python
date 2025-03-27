import psycopg2

# pip install psycopg2-binary

try:
    # set up the connection
    connection = psycopg2.connect(
        host="localhost",
        database="ecommerce",
        user="postgres",
        password="xxxxxxxxx"
    )
    
    # cursor enabling traversal and manipulation of records
    cursor = connection.cursor()
    print("Connection successful!")
    
    # get database version
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"PostgreSQL version: {db_version}")    

    # sample query
    cursor.execute("SELECT product_id, description, price, product_name FROM public.products;")
    rows = cursor.fetchall()

    # display data
    for row in rows:
        print(row)    

except psycopg2.Error as e:
    print(f"Error connecting to PostgreSQL: {e}")

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
