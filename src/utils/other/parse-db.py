import sqlite3
import re

# Connect to the SQLite3 database
conn = sqlite3.connect("runyankore.SQLite3")
cursor = conn.cursor()

# Define the SQL query to retrieve the required fields
query = "SELECT text, niv FROM verses"

# Execute the query
cursor.execute(query)

# Open the output files
with open("BIBLE.en-ru.en", "w", encoding="utf-8") as en_file, open(
    "BIBLE.en-ru.ru", "w", encoding="utf-8"
) as ru_file:

    # Fetch all rows from the query result
    rows = cursor.fetchall()

    for row in rows:
        runyankole_text = row[0]
        english_text = row[1]

        # Remove HTML tags from Runyankole text if present
        clean_runyankole_text = re.sub(r"<.*?>", "", runyankole_text)

        # Write to the files
        en_file.write(english_text + "\n")
        ru_file.write(clean_runyankole_text + "\n")

# Close the database connection
conn.close()
