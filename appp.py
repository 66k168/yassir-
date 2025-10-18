import sqlite3
import pandas as pd
import streamlit as st

st.title("🏠 Airbnb Listings")

# Connect to (or create) the database in the current session
conn = sqlite3.connect('airbnb.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS listings (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL,
    room_type TEXT,
    reviews INTEGER
)
''')

# Insert sample data only if table is empty
cursor.execute("SELECT COUNT(*) FROM listings")
if cursor.fetchone()[0] == 0:
    data = [
        ("Cozy Apartment", 75, "Entire home", 120),
        ("Beach Room", 55, "Private room", 80),
        ("Mountain View", 90, "Entire home", 150),
        ("Downtown Studio", 65, "Shared room", 40)
    ]
    cursor.executemany("INSERT INTO listings (name, price, room_type, reviews) VALUES (?, ?, ?, ?)", data)
    conn.commit()

# Read data from database
df = pd.read_sql_query("SELECT * FROM listings", conn)
conn.close()

# Display the data in Streamlit
st.dataframe(df)
