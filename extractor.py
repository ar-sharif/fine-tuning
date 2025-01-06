import mysql.connector
import pandas as pd

# Connect to the database
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="secret",
    database="sample_db"
)

# Query the table
query = "SELECT previous_description, description FROM new_estates"
cursor = connection.cursor()
cursor.execute(query)

# Fetch the data and convert to a DataFrame
data = pd.DataFrame(cursor.fetchall(), columns=["previous_description", "description"])
cursor.close()
connection.close()

# Save to JSONL
data.to_json("training_data.jsonl", orient="records", lines=True, force_ascii=False)

