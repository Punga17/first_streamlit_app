import streamlit 
streamlit.title('My parents new Healthy dinner ')

streamlit.header('🥣 🥗 Breakfast Menu 🥑🍞')
streamlit.text('🥣idly🥣')
streamlit.text('🥗🥑🍞dosa 🥗🥑')
streamlit.text(' 🐔🍞chapathi🐔 🍞')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
