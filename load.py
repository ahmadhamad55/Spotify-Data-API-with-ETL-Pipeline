import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def load_data(df):
    # Create a connection to the PostgreSQL database
    conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres"
)

    cur = conn.cursor()
    
    # Create a table to store the song data if it doesn't already exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS songs (
            song_name VARCHAR(255),
            album_name VARCHAR(255)
        )
    """)
    
    # Insert the song data into the database
    for index, row in df.iterrows():
        cur.execute("INSERT INTO songs (song_name, album_name) VALUES (%s, %s)", (row["song_name"], row["album_name"]))
    
    conn.commit()
    cur.close()
    conn.close()
