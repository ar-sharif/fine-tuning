import mysql.connector
import json

# MySQL connection configuration
config = {
    'host': '127.0.0.1',  # Replace with your MySQL host
    'user': 'root',  # Replace with your MySQL username
    'password': 'secret',  # Replace with your MySQL password
    'database': 'sample3'  # Replace with your database name
}

# Connect to the MySQL database
try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor(dictionary=True)

    # Fetch data from the table
    query = "SELECT id, previous_description, description FROM new_estates;"
    cursor.execute(query)
    rows = cursor.fetchall()

    # Create dataset
    prompt = f"""
        You are an estate adviser intelligent assistant that changes text formatting and tone of description estates.
        Transform the entered text into a more friendly and professional format while retaining all essential details.

        ### Instructions:
        - Identify the core information in the input text.
        - Reformat it into a more professional, summarized, structured, and friendly style.
        - Use bulleted lists for clarity when needed.
        - Change the original tone to enhance readability and friendliness.
        - Avoid adding additional content.
        - Output language is PERSIAN.
    """

    with open('dataset3.jsonl', 'w') as file:
        for row in rows:
            record = {
                "messages": [
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": row['previous_description']},
                    {"role": "assistant", "content": row['description']}
                ]
            }
            # Write each record as a single JSON line
            file.write(json.dumps(record, ensure_ascii=False) + '\n')

    print("Dataset created and saved as 'dataset.jsonl'.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
