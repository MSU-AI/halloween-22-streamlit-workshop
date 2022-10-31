import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

st.title("Fancy Math")

st.header("Choose two numbers")

a = st.number_input("Choose a:", min_value=1, max_value=5, step=1, value=2)
b = st.number_input("Choose b:", min_value=1, max_value=5, step=1, value=3)

# Streamlit makes it easy to display fancy math equations using st.latex()
st.header("Your equation is...")
st.latex(f"\sin({a}x) x^{{{b}}}")

# Create graph and display it using matplotlib
st.write("And here is a nice graph (created using numpy and matplotlib):")

x = np.arange(0, 3, 0.1)
y = np.sin(a*x) * np.power(x, b)

fig = plt.figure()
plt.plot(x, y)

st.pyplot(fig)