import streamlit
import pandas

streamlit.title('My Streamlit App')
streamlit.header('Breakfast menu')
streamlit.text('🍳 Eggs')
streamlit.text('🥗 Veggies')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.dataframe(my_fruit_list)
