import pickle
import streamlit as st

with open("model.pickle",'br') as file:
    model = pickle.load(file)


st.title("Salary Prediction App")

yoe = st.text_input('Years of Experience')

if st.button("Submit"):
    y_pred = model.predict([[int(yoe)]])
    st.write(f"The expected salary is {y_pred[0]}")