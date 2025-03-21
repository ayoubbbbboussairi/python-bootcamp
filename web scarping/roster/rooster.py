import json
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('roster.sqlite')
cur = conn.cursor()

# Drop tables if they exist
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;
''')

# Create tables
cur.executescript('''
CREATE TABLE User (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Course (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title   TEXT UNIQUE
);

CREATE TABLE Member (
    user_id  INTEGER,
    course_id  INTEGER,
    role    INTEGER,
    PRIMARY KEY (user_id, course_id)
);
''')

# Read the JSON data from the file
filename = 'roster_data.json'
with open(filename) as f:
    data = json.load(f)

# Populate the tables with data from the JSON file
for entry in data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    # Insert or ignore user
    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]

    # Insert or ignore course
    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0]

    # Insert or replace member
    cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role) 
                   VALUES (?, ?, ?)''', (user_id, course_id, role))

# Commit changes to the database
conn.commit()

# Run the specified SQL query to get the output
cur.execute('''SELECT User.name, Course.title, Member.role FROM 
                User JOIN Member JOIN Course 
                ON User.id = Member.user_id AND Member.course_id = Course.id
                ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;''')

# Print the query results
print("Query 1 Results:")
for row in cur:
    print(row)

# Run the specified SQL query to generate the unique code
cur.execute('''SELECT 'XYZZY' || hex(User.name || Course.title || Member.role) AS X FROM 
                User JOIN Member JOIN Course 
                ON User.id = Member.user_id AND Member.course_id = Course.id
                ORDER BY X LIMIT 1;''')

# Get the unique code
code = cur.fetchone()[0]

# Print the unique code
print("\nUnique Code:")
print(code)

# Close the cursor and connection
cur.close()
conn.close()
