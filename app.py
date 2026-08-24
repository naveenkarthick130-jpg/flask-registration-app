from flask import Flask, render_template, request
import mysql.connector
import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash

load_dotenv()

app = Flask(__name__)

db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    ssl_verify_cert=False
)

print("Aiven MySQL connected successfully!")


@app.route("/")
def home():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register():

    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]
    hashed_password = generate_password_hash(password)
    phone = request.form["phone"]

    cursor = db.cursor()

    sql = """
    INSERT INTO users (name, email, password, phone)
    VALUES (%s, %s, %s, %s)
    """

    values = (name, email, hashed_password, phone)

    cursor.execute(sql, values)

    db.commit()

    cursor.close()

    return "Registration successful!"


if __name__ == "__main__":
    app.run(debug=True)