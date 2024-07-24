from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure GenAI Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function To Load Google Gemini Model and provide queries as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function To retrieve query from the database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

# Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL queries!
The SQL database has the name STUDENT and has the following columns - ID, NAME, CLASS, SECTION, MARKS, AGE, EMAIL.

For example,
Example 1 - How many entries of records are present?
The SQL command will be something like this:
SELECT COUNT(*) FROM STUDENT;

Example 2 - Tell me all the students studying in the Data Science class?
The SQL command will be something like this:
SELECT * FROM STUDENT WHERE CLASS="Data Science";

Example 3 - List the names and emails of students who scored more than 90 marks?
The SQL command will be something like this:
SELECT NAME, EMAIL FROM STUDENT WHERE MARKS > 90;

Example 4 - Retrieve the average marks of students in the AI class?
The SQL command will be something like this:
SELECT AVG(MARKS) FROM STUDENT WHERE CLASS="AI";

Also, the SQL code should not have ``` at the beginning or end and should not include the word SQL in the output.

    """
]

# Streamlit App
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# If submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    response = read_sql_query(response, "student.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)
