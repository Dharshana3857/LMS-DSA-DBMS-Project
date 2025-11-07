import mysql.connector

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',       # your MySQL username
    'password': '',       # your MySQL password if set
    'database': 'lms_db'
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)
