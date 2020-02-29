# POSTGRES WITH PYTHON


# To interact with Postgresql use the following package

import psycopg2

# Create a connection and cursor to the databases

def Connect():

    try:
        conn = psycopg2.connect("host= 192.168.1.1 dbname=Test user=admin password=admin ")
    except psycopg2.Error as e:
        print("couldnot connect")

    try:
        cur = conn.cursor()
    except psycopg2.Error as e:
        print("cursor failed")

    conn.set_session(autocommit=True)
    return conn,cur

#insert value into a created table music_store2

def insert_value(conn,cur):

    cur.execute("INSERT INTO music_store2 (transaction_id,customer_name,cashier_name,year,albums_purchased)\
                 VALUES (%s, %s, %s, %s, %s)",\
                 (1, "v1", "Sam", 2000, ["Rubber Soul", "Let it Be"]))

    # If data is in a Data Frame we can iterate over it and insert the rows

    DfQuery = ("""INSERT INTO music_store2 (transaction_id,customer_name,cashier_name,year,albums_purchased)
                 VALUES (%s, %s, %s, %s, %s)""")

    for i,rows in Df.iterrows():
        cur.execute(DfQuery,rows)
        conn.commit()

def main():
    conn,cur = connect()
    insert_value(conn,cur)
    conn.close()

if __name__ == "__main__":
    main()
