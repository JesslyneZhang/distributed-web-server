import os
import pymysql
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

SERVER_NAME = os.getenv("SERVER_NAME", "Backend Server")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "distributed_server_db")


def get_db_connection():
    return pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor,
        connect_timeout=3
    )


@app.route("/")
def index():
    db_status = "Disconnected"
    messages = []

    try:
        connection = get_db_connection()

        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT id, content, created_at FROM messages ORDER BY id DESC"
            )
            messages = cursor.fetchall()

        connection.close()
        db_status = "Connected"

    except Exception as error:
        print(f"Database error: {error}")

    return render_template(
        "index.html",
        server_name=SERVER_NAME,
        db_status=db_status,
        messages=messages
    )


@app.route("/messages", methods=["POST"])
def add_message():
    content = request.form.get("content", "").strip()

    if content:
        try:
            connection = get_db_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO messages (content) VALUES (%s)",
                    (content,)
                )

            connection.commit()
            connection.close()

        except Exception as error:
            print(f"Insert error: {error}")

    return redirect(url_for("index"))


@app.route("/health")
def health():
    return {"status": "healthy", "server": SERVER_NAME}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)