import mysql.connector
import hvac
from flask import Flask, render_template_string

app = Flask(__name__)

# Initialize OpenBAO client
client = hvac.Client(url='http://127.0.0.1:8200', token='myroot')

# Fetch database credentials from OpenBAO
def get_db_credentials():
    try:
        secret = client.kv.v2.read_secret_version(path='testvault-db', mount_point='secret')
        return secret['data']['data']
    except Exception as e:
        return f"Error fetching credentials: {e}"

@app.route('/')
def display_books():
    try:
        # Get credentials from OpenBAO
        db_config = get_db_credentials()
        if isinstance(db_config, str):
            return db_config  # Return error if credential fetch fails
        
        # Connect to MariaDB
        conn = mysql.connector.connect(
            host=db_config['host'],
            port=int(db_config['port']),
            user=db_config['user'],
            password=db_config['password'],
            database=db_config['database']
        )
        cursor = conn.cursor()
        
        # Query the livre table
        cursor.execute("SELECT id, titre FROM livre")
        books = cursor.fetchall()
        
        # Close connection
        cursor.close()
        conn.close()
        
        # HTML template
        html = """
        <h1>Books in Database</h1>
        <table border='1'>
            <tr><th>ID</th><th>Title</th></tr>
            {% for book in books %}
            <tr><td>{{ book[0] }}</td><td>{{ book[1] }}</td></tr>
            {% endfor %}
        </table>
        """
        return render_template_string(html, books=books)
    except mysql.connector.Error as err:
        return f"Error: {err}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)