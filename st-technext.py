import streamlit as st
import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
  host="bdsoegedkrvbr5lsf8ww-mysql.services.clever-cloud.com",
  user="ugcpyivtje9ou9u5",
  password="ZukNS59AoGd13X9HTD8d",
  database="bdsoegedkrvbr5lsf8ww"
)
def some_function(user_text):
    patent_id = []
    patent_text = []

    for index, row in df.iterrows():
        if user_text in row['patent_text']:
            patent_id.append(row["patent_id"])
            patent_text.append(row["patent_text"])
    list_of_tuples = list(zip(patent_id,patent_text))
    result = pd.DataFrame(list_of_tuples, columns=['Patent ID', 'Patent Text'])

    if result.empty:
        st.write("NO RESULTS FOUND, SORRY, TRY AGAIN!")
    else:
        st.write(result)

mycursor = mydb.cursor()

st.title('Search some patents')

page = st.sidebar.selectbox(
    'Select a page:',
    ('About', 'Search Patents')
)
if page == 'About':
    st.write('This page is made by Jose M Teodosio-Meza')
    st.write('Here you can search')
    st.write("for a patent's ID and info by writing a word")

if page == 'Search Patents':
    st.write('''Input any word''')

    user_text = st.text_input('Please input some text:')
    st.write(f'Your results')

    mycursor.execute("SELECT * FROM patents")
    myresult = mycursor.fetchall()
    df = pd.DataFrame(myresult, columns=['patent_id', 'patent_text'])

    some_function(user_text)
