import sqlite3

# Connect to SQLite
connection = sqlite3.connect("student.db")

# Create a cursor object to insert records, create table
cursor = connection.cursor()

# Drop the table if it already exists
cursor.execute("DROP TABLE IF EXISTS STUDENT")

# Create the table with additional attributes
table_info = """
CREATE TABLE STUDENT(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT,
    AGE INT,
    EMAIL VARCHAR(50)
);
"""
cursor.execute(table_info)

# Insert some records
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, AGE, EMAIL) VALUES ('Krish', 'Data Science', 'A', 90, 22, 'krish@example.com')")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, AGE, EMAIL) VALUES ('Sudhanshu', 'Data Science', 'B', 100, 23, 'sudhanshu@example.com')")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, AGE, EMAIL) VALUES ('Darius', 'Data Science', 'A', 86, 24, 'darius@example.com')")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, AGE, EMAIL) VALUES ('Vikash', 'DEVOPS', 'A', 50, 21, 'vikash@example.com')")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, AGE, EMAIL) VALUES ('Dipesh', 'DEVOPS', 'A', 35, 22, 'dipesh@example.com')")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, AGE, EMAIL) VALUES ('Alice', 'AI', 'A', 95, 23, 'alice@example.com')")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, AGE, EMAIL) VALUES ('Bob', 'AI', 'B', 89, 22, 'bob@example.com')")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, AGE, EMAIL) VALUES ('Charlie', 'AI', 'A', 92, 24, 'charlie@example.com')")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, AGE, EMAIL) VALUES ('David', 'Web Development', 'A', 75, 21, 'david@example.com')")
cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS, AGE, EMAIL) VALUES ('Eva', 'Web Development', 'B', 80, 23, 'eva@example.com')")

# Display all the records
print("The inserted records are:")
data = cursor.execute("SELECT * FROM STUDENT")
for row in data:
    print(row)

# Commit your changes in the database
connection.commit()
connection.close()
