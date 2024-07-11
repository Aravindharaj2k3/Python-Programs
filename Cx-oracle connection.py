import cx_Oracle

# Establish the database connection

dsn_tns= 'orcl-aws.c8sefhobaih4.ap-south-1.rds.amazonaws.com'
port_no = '1521'
service_name ='orcl'
user_name='team25_aravind'
password ='team25_aravind'

dsn_tns = cx_Oracle.makedsn(dsn_tns,port_no, service_name = service_name)
conn = cx_Oracle.connect(user=user_name, password=password, dsn=dsn_tns)

# Create a cursor
cur = conn.cursor()

# Execute a query
cur.execute('SELECT * FROM product')

# Fetch the results
rows = cur.fetchall()

# Print the results
for row in rows:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()
