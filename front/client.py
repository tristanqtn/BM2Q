import streamlit as st
import requests

st.title("BM2Q")
st.write("")
st.write("Select the number of players")
number_of_player = st.slider("Number of player", 2, 10,1)



if st.button('Create'):
    res = requests.post(url=f"http://192.168.1.138:3000/game?number_of_players={str(number_of_player)}")
    st.subheader(f"Reponse from API = {res.text}")
    
