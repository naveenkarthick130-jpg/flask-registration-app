import mysql.connector
import os
import mysql.connector
from dotenv import load_dotenv

try:
    db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    ssl_verify_cert=False
    )

    print("✅ Aiven MySQL connected successfully!")

    cursor = db.cursor()

    cursor.execute("SELECT DATABASE();")

    result = cursor.fetchone()

    print("Database:", result[0])

    cursor.close()
    db.close()

except Exception as e:
    print("❌ Connection failed")
    print(e)