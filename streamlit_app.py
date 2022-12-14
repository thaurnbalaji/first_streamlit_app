import streamlit

streamlit.title("My Mom's New Healthy Diner")
streamlit.header('Breakfast Favourites')
streamlit.text('omega3 and blueberry oatmeal')
streamlit.text('Kale, spinach and rocket smoothie')
streamlit.text('Hard-boiled-free-range-egg')
streamlit.text('Avacado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

#Let's put a pick list here so they can pick the fruit they want to include
streamlit.multiselect("pick some fruits:", list(my_fruit_list.index))
#display the table on the page
streamlit.dataframe(my_fruit_list)

#lets put a picklist here so that they can pick the fruit they want to include
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
