import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split

st.title("Titanic Decision Tree")

st.write("In Workshop 4, [Would You Survive the Titanic?](https://colab.research.google.com/drive/1S-oSuutZnL3EVctGE8SfitHl9B-cWG-2?usp=sharing), we created decision trees to predict whether or not a passenger would survive the Titanic.")
st.write("This page re-uses that code to create an interactive decision tree builder.")


st.header("Dataset Preview")

# Load the dataset and display it as a table using Streamlit's st.write() function
dataframe = pd.read_csv("titanic.csv", index_col=0)
st.write(dataframe)

st.header("Build a Decision Tree")

# Split the dataset into training and testing data
survived = dataframe["survived"] == 1
features = dataframe.drop(["survived"], axis=1)
features, features_test, survived, survived_test = train_test_split(features, survived, test_size = 0.3)

# Allow user to enter the tree depth
depth = st.number_input("max depth", min_value=1, max_value=5)

my_decision_tree = tree.DecisionTreeClassifier(max_depth=depth) # Create a decision tree
my_decision_tree.fit(features, survived) # Train the decision tree using the dataset

# Display the decision tree as a flow chart
st.write(f"This decision tree is {round(my_decision_tree.score(features_test, survived_test) * 100, 2)}% accurate")
f = plt.figure(figsize=(10,10))
tree.plot_tree(my_decision_tree, feature_names=features.columns, class_names=["died", "survived"], filled=True)
st.pyplot(f)

st.header("Predict your fate (YOU finish this part!)")

p_class = st.number_input("Passenger Class (1 = high, 2 = middle, 3 = low)", min_value=1, max_value=3)
sex = st.radio("Passenger sex", options=["Female", "Male"])
age = st.number_input("Passenger age", min_value=0, max_value=100)
num_siblings = st.number_input("Number of siblings", min_value=0, max_value=10)
num_children = st.number_input("Number of children", min_value=0, max_value=10)
fare = st.number_input("Fare", min_value=0.0, max_value=1000.0)

sex = 0 if "Female" else 1 # Convert `sex` from string to number

st.write(f"My decision tree predicts that you have a ?????? chance of survival.")