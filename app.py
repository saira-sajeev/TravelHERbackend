import mysql.connector
from config import Config
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config.from_object(Config)

# Establish MySQL connection
def get_db_connection():
    connection = mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )
    return connection

# Example route to test MySQL connection
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    FirstName = data['first_name']
    LastName = data['last_name']
    PersonEmail = data['email']
    

    # Insert user data into MySQL database
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s, %s, %s, %s)",
                   (FirstName, LastName, PersonEmail))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'message': 'User added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=True)



