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
streamlit.dataframe(my_fruit_list)
