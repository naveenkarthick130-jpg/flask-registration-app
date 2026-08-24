import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    ssl_verify_cert=False
)

print("Connected successfully!")


cursor = db.cursor()

cursor.execute("SELECT * FROM users")


users = cursor.fetchall()

for user in users:
    print(user)

for table in cursor:
    print(table)

cursor.close()
db.close()
