import mysql.connector
#from flask import Flask, render_template, request, redirect, url_for
log = 0

def check_user(email):
    # Connect to the MySQL database
    cnx = mysql.connector.connect(user='test', password='happyhappyhappy',
                                host='127.0.0.1', database='ztravel')
    cursor = cnx.cursor()

    # Check if the user is already registered
    query = 'SELECT COUNT(*) FROM users WHERE email = %s'
    values = (email,)
    cursor.execute(query, values)
    result = cursor.fetchone()

    # Print the result
    if result[0] > 0:
        return True # User is already registered
    else:
        return False # User is not registered

    # Close the cursor and connection
    cursor.close()
    cnx.close()

def register_user(name, email, password):
    if check_user(email):
        print(" User already registered")
    else:
        # Connect to the MySQL database
        cnx = mysql.connector.connect(user='test', password='happyhappyhappy',
                                    host='127.0.0.1', database='ztravel')
        cursor = cnx.cursor()

        # Insert the user into the users table
        query = 'INSERT INTO users (name, email, password) VALUES (%s, %s, %s)'
        values = (name, email, password)
        cursor.execute(query, values)

        # Commit the transaction
        cnx.commit()

        # Close the cursor and connection
        cursor.close()
        cnx.close()

def check_status(email):
    # Connect to the MySQL database
    cnx = mysql.connector.connect(user='test', password='happyhappyhappy',
                                host='127.0.0.1', database='ztravel')
    cursor = cnx.cursor()

    # Check if the user is already logged in
    query = 'SELECT COUNT(*) FROM status WHERE email = %s'
    values = (email,)
    cursor.execute(query, values)
    result = cursor.fetchone()

    # Print the result
    if result[0] > 0:
        return True # User is already logged in
    else:
        return False # User is not logged in

    # Close the cursor and connection
    cursor.close()
    cnx.close()

def login(email, password):
    if check_status(email):
        print(" User already logged in")
    else:
        # Connect to the MySQL database
        cnx = mysql.connector.connect(user='test', password='happyhappyhappy',
                                    host='127.0.0.1', database='ztravel')
        cursor = cnx.cursor()

        # Check if the email and password match a registered user
        query = 'SELECT COUNT(*) FROM users WHERE email = %s AND password = %s'
        values = (email, password)
        cursor.execute(query, values)
        result = cursor.fetchone()

        # Update the status table
        if result[0] > 0:
            query = 'INSERT INTO status (email) VALUES (%s)'
            values = (email,)
            cursor.execute(query, values)
            # Commit the transaction
            cnx.commit()
        else:
            print('Login failed')

        # Close the cursor and connection
        cursor.close()
        cnx.close()

def logout(email):
    if check_status(email):
        # Connect to the MySQL database
        cnx = mysql.connector.connect(user='test', password='happyhappyhappy', host='127.0.0.1', database='ztravel')

        cursor = cnx.cursor()

        # Delete current user from status table
        query = 'DELETE FROM status WHERE email = %s'
        values = (email,)
        cursor.execute(query, values)

        # Commit the transaction
        cnx.commit()

        # Close the cursor and connection
        cursor.close()
        cnx.close()
    else:
        print(" User not logged in")


def register_flight(id, name, dep, dest, price):
        # Connect to the MySQL database
        cnx = mysql.connector.connect(user='test', password='happyhappyhappy',
                                    host='127.0.0.1', database='ztravel')
        cursor = cnx.cursor()

        # Insert the data into the flights table
        query = 'INSERT INTO flights (id, name, departure, destination, price) VALUES (%s, %s, %s, %s, %s)'
        values = (id, name, dep, dest, price)
        cursor.execute(query, values)

        # Commit the transaction
        cnx.commit()

        # Close the cursor and connection
        cursor.close()
        cnx.close()

def register_tours(id, name, day, night, price):
            # Connect to the MySQL database
        cnx = mysql.connector.connect(user='test', password='happyhappyhappy',
                                    host='127.0.0.1', database='ztravel')
        cursor = cnx.cursor()

        # Insert the data into the flights table
        query = 'INSERT INTO tours (id, name, days, nights, price) VALUES (%s, %s, %s, %s, %s)'
        values = (id, name, day, night, price)
        cursor.execute(query, values)

        # Commit the transaction
        cnx.commit()

        # Close the cursor and connection
        cursor.close()
        cnx.close()

def main():

    print("\n ----------------------------------------------------\n Welcome to ZTravel Admin! \n ----------------------------------------------------")
    print("1. Register")
    print("2. Login")
    print("3. Logout")
    print("4. Register Flight")
    print("5. Register Tour")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        register_user(name, email, password)
    elif choice == 2:
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        login(email, password)
    elif choice == 3:
        email = input("Enter your email: ")
        logout(email)
    elif choice == 4:
        id = input("Enter flight id: ")
        name = input("Enter flight name: ")
        dep = input("Enter departure: ")
        dest = input("Enter destination: ")
        price = input("Enter price: ")
        register_flight(id, name, dep, dest, price)
    elif choice == 5:
        id = input("Enter tour id: ")
        name = input("Enter tour name: ")
        day = input("Enter days: ")
        night = input("Enter nights: ")
        price = input("Enter price: ")
        register_tours(id, name, day, night, price)
    elif choice == 6:
        exit()
    else:
        print("Invalid choice")




if __name__ == '__main__':
        while True:
            main() # Run the main function
