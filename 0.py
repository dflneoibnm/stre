import streamlit as st
import datetime

nom = st.text_input('Entre le nom')
date = st.date_input('Date', format = "DD/MM/YYYY")
heure = st.time_input('heure')

if st.button('Signer'): 
    f = open("demofile2.txt", "a")
    f.write(str(date))
    f.close()
    st.title('Well done pour aujourdhui')
