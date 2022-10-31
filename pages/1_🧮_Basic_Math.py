import streamlit as st

st.title("Basic Math")

number = st.slider("Select a value", 0, 100)

st.write("The number you entered is", number)

number2 = st.number_input("Enter another number")

st.write("The sum of the two numbers is", number + number2)
