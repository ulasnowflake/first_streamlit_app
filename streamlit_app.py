import streamlit
import pandas

streamlit.title('My Streamlit Diner')
streamlit.header('Breakfast menu')
streamlit.text('🍳 Eggs')
streamlit.text('🥗 Veggies')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Strawberries','Banana'])
streamlit.dataframe(my_fruit_list)
