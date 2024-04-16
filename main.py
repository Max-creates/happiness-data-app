import streamlit as st
import plotly.express as px
import pandas as pd


st.header("In Search for Happiness")

df = pd.read_csv("happy.csv")

x_option = st.selectbox("Select the data for the X-axis: ", ("GDP",
                                                             "Happiness",
                                                             "Generosity"))
y_option = st.selectbox("Select the data for the Y-axis: ", ("GDP",
                                                             "Happiness",
                                                             "Generosity"))

st.subheader(f"{x_option} and {y_option}")
figure = px.scatter(x=df[x_option.lower()],
                    y=df[y_option.lower()],
                    labels={"x": x_option, "y": y_option})
st.plotly_chart(figure)