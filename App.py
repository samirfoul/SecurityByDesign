import mysql.connector
from flask import Flask, render_template_string

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'testvault',
    'password': 'vaultpassword',
    'database': 'testvault'
}

@app.route('/')
def display_books():
    try:
        # Connect to MariaDB
        conn = mysql.connector.connect(**db_config)
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