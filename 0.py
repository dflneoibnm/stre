import streamlit as st
import datetime

nom = st.text_input('Entre le nom')
date = st.time_input('Date',datetime)
heure = st.time_input('heure')

if st.button('Signer'): 
    f = open("demofile2.txt", "a")
    f.write(date, heure)
    f.close()
    st.title('Well done pour aujourdhui')
