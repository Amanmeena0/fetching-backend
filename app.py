# from flask import Flask, jsonify, request
# import mysql.connector
# from mysql.connector import Error

# app = Flask(__name__)

# # Database configuration
# db_config = {
#     'user': 'root',
#     'password': 'MySQLPassword@2004',
#     'host': 'localhost',
#     'database': 'crime'
# }

# def get_db_connection():
#     try:
#         connection = mysql.connector.connect(**db_config)
#         if connection.is_connected():
#             print("Connected to the database")
#         return connection
#     except Error as e:
#         print(f"Error connecting to MySQL: {e}")
#         return None

# # Endpoint to get all data from the specific table
# @app.route('/api/data', methods=['GET'])
# def get_data():
#     conn = get_db_connection()
#     if conn:
#         try:
#             cursor = conn.cursor(dictionary=True)
#             cursor.execute('SELECT * FROM crime_data')
#             results = cursor.fetchall()
#             cursor.close()
#             conn.close()
#             return jsonify(results)
#         except Error as e:
#             print(f"Error fetching data from MySQL: {e}")
#             return jsonify({'error': 'Error fetching data'}), 500
#     else:
#         return jsonify({'error': 'Error connecting to database'}), 500


# @app.route('/api/search', methods=['GET'])
# def search_data():
#     search_column = request.args.get('column', '')
#     search_query = request.args.get('query', '')

#     valid_columns = [
#         'state_ut', 'district', 'year', 'murder', 'attempt_to_murder', 
#         'culpable_homicide_not_amounting_to_murder', 'rape', 'custodial_rape', 
#         'other_rape', 'kidnapping_abduction', 'kidnapping_and_abduction_of_women_and_girls', 
#         'kidnapping_and_abduction_of_others', 'dacoity', 'preparation_and_assembly_for_dacoity', 
#         'robbery', 'burglary', 'theft', 'auto_theft', 'other_theft', 'riots', 
#         'criminal_breach_of_trust', 'cheating', 'counterfeiting', 'arson', 'hurt_grevious_hurt', 
#         'dowry_deaths', 'assault_on_women_with_intent_to_outrage_her_modesty', 'insult_to_modesty_of_women', 
#         'cruelty_by_husband_or_his_relatives', 'importation_of_girls_from_foreign_countries', 
#         'causing_death_by_negligence', 'other_ipc_crimes', 'total_ipc_crimes'
#     ]

#     if search_column not in valid_columns:
#         return jsonify({"error": "Invalid column specified"}), 400

#     conn = get_db_connection()
#     if conn:
#         try:
#             query = f"SELECT * FROM crime_data WHERE {search_column} LIKE %s"
#             cursor = conn.cursor(dictionary=True)
#             cursor.execute(query, (f'%{search_query}%',))
#             data = cursor.fetchall()
#             cursor.close()
#             conn.close()
#             return jsonify(data)
#         except Error as e:
#             print(f"Error executing search query: {e}")
#             return jsonify({'error': 'Error executing search query'}), 500
#     else:
#         return jsonify({'error': 'Error connecting to database'}), 500
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'MySQLPassword@2004',
    'database': 'crime'
}

# Function to get data from the database
def get_data(query, params):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query, params)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

@app.route('/search', methods=['GET'])
def search():
    state_ut = request.args.get('state_ut', '')
    query = "SELECT * FROM crime_data WHERE state_ut LIKE %s"
    params = (f'%{state_ut}%',)
    data = get_data(query, params)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
