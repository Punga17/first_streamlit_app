import streamlit 
streamlit.title('My parents new Healthy dinner ')

streamlit.header('🥣 🥗 Breakfast Menu 🥑🍞')
streamlit.text('🥣idly🥣')
streamlit.text('🥗🥑🍞dosa 🥗🥑')
streamlit.text(' 🐔🍞chapathi🐔 🍞')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index) ,['Apple' ,'Banana'] )

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
