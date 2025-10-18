import streamlit as st
import pandas as pd
import sqlite3

st.title("🏠 STEP AIRBNB Data Manager")

# Connect to your local database
conn = sqlite3.connect('airbnb.db')

# Load data
data = pd.read_sql_query("SELECT * FROM listings", conn)

# Show table
st.subheader("📊 All Listings")
st.dataframe(data)

# Stats
st.subheader("📈 Quick Stats")
st.write("Total Listings:", len(data))
st.write("Average Price:", round(data['price'].mean(), 2))
st.write("Most Expensive Listing:", data['price'].max())
st.write("Average Reviews:", round(data['reviews'].mean(), 1))

# Add new listing form
st.subheader("➕ Add New Listing")
with st.form("add_form"):
    name = st.text_input("Listing Name")
    price = st.number_input("Price", min_value=0.0)
    room_type = st.selectbox("Room Type", ["Entire home", "Private room", "Shared room"])
    reviews = st.number_input("Number of Reviews", min_value=0)
    submitted = st.form_submit_button("Add Listing")

    if submitted:
        conn.execute(
            "INSERT INTO listings (name, price, room_type, reviews) VALUES (?, ?, ?, ?)",
            (name, price, room_type, reviews)
        )
        conn.commit()
        st.success(f"✅ Added {name} successfully!")

conn.close()
