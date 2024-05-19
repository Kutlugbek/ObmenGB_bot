import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

def sql_create_tables():
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                contact TEXT
    )""")
    
    conn.commit()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                operator TEXT,
                gb_amount INTEGER,
                price INTEGER,
                status TEXT DEFAULT 'Active'
    )""")

    conn.commit()

def sql_insert_user(user_id, username):
    # Insert new user or ignore if user already exists
    cur.execute(f"INSERT OR IGNORE INTO users (user_id, username) VALUES ({user_id}, '{username}')")
    conn.commit()

def sql_insert_order(user_id, operator, gb_amount, price):
    cur.execute(f"INSERT INTO orders (user_id, operator, gb_amount, price) VALUES ({user_id}, '{operator}', {gb_amount}, {price})")
    conn.commit()

def sql_update_contact(user_id, contact):
    cur.execute(f"UPDATE users SET contact = '{contact}' WHERE user_id = {user_id}")
    conn.commit()

def get_orders(operator):
    # Get orders' or operator by price increasing order if those orders active
    cur.execute(f"SELECT * FROM orders WHERE operator = '{operator}' AND status = 'Active' ORDER BY price ASC")
    rows = cur.fetchall()
    
    return rows

def get_username(user_id):
    cur.execute(f"SELECT username FROM users WHERE user_id = {user_id}")
    try:
        return (cur.fetchone())[0]
    except:
        return ''

def get_contact(user_id):
    cur.execute(f"SELECT contact FROM users WHERE user_id = {user_id}")
    return (cur.fetchone())[0]

def sql_get_orders_by_user(user_id):
    cur.execute(f"SELECT * FROM orders WHERE user_id = {user_id} AND status = 'Active'")
    return cur.fetchall()

def sql_change_order_status(order_id):
    cur.execute(f"UPDATE orders SET status = ? WHERE order_id = ?", ('Inactive', order_id))
    conn.commit()

sql_create_tables()