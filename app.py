import os
import psycopg2
from flask import Flask
from dotenv import load_dotenv  # Імпортуємо бібліотеку

load_dotenv()

app = Flask(__name__)

DB_NAME = os.getenv('POSTGRES_DB')
DB_USER = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_HOST = os.getenv('DB_HOST')

@app.route('/')
def default():
    return "<h1>My 7th individual work</h1>"

@app.route('/db')
def db_test():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=5432
        )
        cursor = conn.cursor()
        cursor.execute("SELECT content FROM messages;")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        messages_html = "".join([f"<li>{row[0]}</li>" for row in rows])

        return f"<h1>Messages from DB:</h1><ul>{messages_html}</ul>"
    except Exception as e:
        return f"<h1>Error:</h1><p>{str(e)}</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)