import mysql.connector                   # brings in the driver 

# This code reads from an already created database called practice_databases.
# conn = mysql.connector.connect(          # create new object using connector and parameters
#     host = "localhost",
#     database = "practice_databases",
#     user ="root",
#     password = "password")


# cursor = conn.cursor()                    # connector has cursor method
# cursor.execute("SELECT * FROM children")  # use SELECT and FROM sql commands

# for row in cursor:
#     print(row)


# # CREATE NEW DATABASE
# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "password"
# )

# mycursor = mydb.cursor()

# # mycursor.execute("Create database dbPractice") # create a database

# mycursor.execute('Show databases')  # displays all the databases on my computer mysql workbench

# for db in mycursor:
#     print(db)


# ADD COLUMNS TO ALREADY CREATED TABLE
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "dbPractice"
)

mycursor = mydb.cursor()

# mycursor.execute("Create table Books(name varchar(200), author varchar(200), pages int(20))")
# mycursor.execute("Show tables")

# for tb in mycursor:
#     print(tb)


# # LEARN TO INSERT INFO INTO COLUMNS ON TABLE
# sqlform = "Insert into books(name,author,pages) values(%s,%s,%s)"

# books = [("Pride and Prejudice", "Jane Austin", 380), ("1984", "George Orwell", 328), ("Atomic Habits", "James Clear", 320), ]

# mycursor.executemany(sqlform, books)      # if just "execute" is used it will only do one, but we want multiple so use "executemany"

# mydb.commit()



# sqlform = """INSERT INTO books(name, author, pages) VALUES("Scooby Doo", "Shaggy", 12)"""
# mycursor.execute(sqlform)
# mydb.commit()



# # DISPLAY TABLE CONTENTS
# mycursor.execute("SELECT * FROM books")  # use SELECT and FROM sql commands

# for row in mycursor:
#     print(row)

# GET ONE NAME 
# mycursor.execute("Select name from books") 

# myresult = mycursor.fetchone()   # fetch one value 

# for row in myresult:
#     print(row)

## GET ALL THE INFO FROM TABLE
# mycursor.execute("Select * from books")

# myresult = mycursor.fetchall()

# for row in myresult:
#     print(row)


# # LEARN UPDATE
# sql = "UPDATE books SET author='James Clear' WHERE name='Atomic Habits'"
# mycursor.execute(sql)

# mydb.commit()


# # # LEARN DELETE
# sql = "DELETE FROM books WHERE name = 'scooby doo'"
# mycursor.execute(sql)
# mydb.commit()


# mycursor.execute("Select * from books")
# myresult = mycursor.fetchall()

# for row in myresult:
#     print(row)


''' Display menu options for editing database.'''
def menu():
    print("Choose an option: ")
    print("\tD - Display Contents of Database")
    print("\tA - Add a Book to Database")
    print("\tE - Edit a Book in the Database")
    print("\tQ - Quit")

''' Menu Option: Display contents of database.'''
def display():
    mycursor.execute("Select * from books")
    myresult = mycursor.fetchall()

    for row in myresult:
        print(row)

''' Menu Option: Add a book to the database.'''
def add():
    title = input("Title: ")
    author = input("Author: ")
    num_pages = int(input("Number of Pages: "))
    values = (title, author, num_pages)

    mycursor.executemany("INSERT INTO books(name, author, pages) VALUES(%s, %s, %s)", (values,))
    mydb.commit()


''' Menu Option: Edit/Delete a book in the database.'''
def edit():
    title = input("Title: ")
    val = (title)
    # sql = "DELETE FROM books WHERE name=(%s)", ()
    # mycursor.execute("DELETE FROM books(name) VALUE(%s)", (val,))
    mycursor.execute("DELETE FROM books WHERE name = (%s)", (val,))
    mydb.commit()

''' Menu Option: Quit/Exit database.'''
def quit():
    return True

done = False
while not done:
    menu()
    user_input = input('\t> ')
    user_input = user_input.upper()

    if (user_input == "D"):
        display()
    elif (user_input == "A"):
        add()
    elif (user_input == "E"):
        edit()
    elif (user_input == "Q"):
        done = True






















