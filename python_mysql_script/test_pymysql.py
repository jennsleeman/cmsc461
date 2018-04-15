#This is a test of pymysql
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='yourusername',
                             password='yourpassword',
                             db='yourdb')

try:



    with connection.cursor() as cursor:
        #create the table
        sql="CREATE table users (email varchar(500), password varchar(100))";
        cursor.execute(sql);
        # Create a new record
        sql = "INSERT INTO users (email, password) VALUES (%s, %s)"
        cursor.execute(sql, ('ilovesql@gmail.com', 'mypassword'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT password FROM users WHERE email=%s"
        cursor.execute(sql, ('ilovesql@gmail.com'))
        result = cursor.fetchone()
        print("Getting password: " + str(result[0]))


    with connection.cursor() as cursor:
        # Update record
	sql = "Update users set password = %s where email =%s"
	cursor.execute(sql, ('mybadpassword','ilovesql@gmail.com'))

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT password FROM users WHERE email=%s"
        cursor.execute(sql, ('ilovesql@gmail.com'))
        result = cursor.fetchone()
        print("New password is: " + str(result[0]))


    with connection.cursor() as cursor:
        #delete record
	sql = "delete from users where email =%s"
	cursor.execute(sql, ('ilovesql@gmail.com'))

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT password FROM users WHERE email=%s"
        cursor.execute(sql, ('ilovesql@gmail.com'))
        result = cursor.fetchone()
        print("This should be empty: " + str(result))



    with connection.cursor() as cursor:
        #drop the table so we can run this without error
        sql="drop table `users`";
        cursor.execute(sql);
    connection.commit()
finally:
    connection.close()
