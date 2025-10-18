import sqlite3

# Connect to (or create) the database
conn = sqlite3.connect('airbnb.db')
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS listings (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL,
    room_type TEXT,
    reviews INTEGER
)
''')

# Optional: add some sample data
data = [
    ("Cozy Apartment", 75, "Entire home", 120),
    ("Beach Room", 55, "Private room", 80),
    ("Mountain View", 90, "Entire home", 150),
    ("Downtown Studio", 65, "Shared room", 40)
]

cursor.executemany("INSERT INTO listings (name, price, room_type, reviews) VALUES (?, ?, ?, ?)", data)
conn.commit()
conn.close()

print("✅ Database and table created successfully!")
