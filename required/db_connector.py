import sqlite3
import os
from dotenv import load_dotenv
from required.logger import get_logger

load_dotenv()

# Fixed 'name' to '__name__'
logger = get_logger(__name__)

DB_NAME = os.getenv("DB_NAME", "test_framework.db")
# Fixed 'file' to '__file__'
DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', DB_NAME))

def get_connection():
    try:
        conn = sqlite3.connect(DB_PATH)
        # row_factory allows accessing columns by name like a dictionary
        conn.row_factory = sqlite3.Row
        logger.info(f"Database connection established: {DB_PATH}")
        return conn
    except sqlite3.Error as e:
        logger.error(f"Database connection failed: {e}")
        raise

def create_users_table():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                username TEXT,
                email TEXT NOT NULL,
                phone TEXT,
                website TEXT
            )
        """)
        conn.commit()
        logger.info("Users table created or already exists")
    except sqlite3.Error as e:
        logger.error(f"Error creating table: {e}")
        raise
    finally:
        conn.close()

def insert_user(user_data):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO users (id, name, username, email, phone, website)
            VALUES (:id, :name, :username, :email, :phone, :website)
        """, {
            "id": user_data.get("id"),
            "name": user_data.get("name"),
            "username": user_data.get("username"),
            "email": user_data.get("email"),
            "phone": user_data.get("phone"),
            "website": user_data.get("website")
        })
        conn.commit()
        logger.info(f"User inserted into database: id={user_data.get('id')}, name={user_data.get('name')}")
    except sqlite3.Error as e:
        logger.error(f"Error inserting user: {e}")
        raise
    finally:
        conn.close()

def verify_user_exists(user_id):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        if row:
            logger.info(f"Database verification passed: user id={user_id} exists")
            return dict(row)
        else:
            logger.warning(f"Database verification failed: user id={user_id} not found")
            return None
    except sqlite3.Error as e:
        logger.error(f"Error querying user: {e}")
        raise
    finally:
        conn.close()

def verify_user_deleted(user_id):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        if row is None:
            logger.info(f"Database verification passed: user id={user_id} correctly deleted")
            return True
        else:
            logger.warning(f"Database verification failed: user id={user_id} still exists")
            return False
    except sqlite3.Error as e:
        logger.error(f"Error verifying deletion: {e}")
        raise
    finally:
        conn.close()

def get_all_users_from_db():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        logger.info(f"Retrieved {len(rows)} users from database")
        return [dict(row) for row in rows]
    except sqlite3.Error as e:
        logger.error(f"Error retrieving users: {e}")
        raise
    finally:
        conn.close()

def delete_user_from_db(user_id):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        logger.info(f"User id={user_id} deleted from database")
    except sqlite3.Error as e:
        logger.error(f"Error deleting user: {e}")
        raise
    finally:
        conn.close()

def clear_all_users():
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users")
        conn.commit()
        logger.info("All users cleared from database")
    except sqlite3.Error as e:
        logger.error(f"Error clearing users: {e}")
        raise
    finally:
        conn.close()