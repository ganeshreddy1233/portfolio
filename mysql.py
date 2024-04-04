import pymysql
mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="8985854588",
    db="gani"
)

# Create a cursor
mycursor = mydb.cursor()

# Define the SQL query
sql = "INSERT INTO peoples (name, age) VALUES (%s, %s)"
val = ("John", "34")

# Execute the query
mycursor.execute(sql, val)

# Commit the changes
mydb.commit()

print(f"{mycursor.rowcount} record inserted.")