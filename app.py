import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv('vehicles_us.csv')

st.header('Vehicle Sales Advertisements')


fig1 = px.histogram(df, x="model_year")
fig1.update_layout(
    title_text='Histogram of Car Model Years',
    xaxis_title_text='Model Year', 
    yaxis_title_text='Count', 
    bargap=0.2, 
    bargroupgap=0.1 
)


fig2 = px.scatter(df, x="odometer", y="price")
fig2.update_layout(
    title_text='Odometer Readings vs Car Prices',
    xaxis_title_text='Odometer Reading', 
    yaxis_title_text='Price' 
)


if st.checkbox('Toggle Figure'):
    st.plotly_chart(fig2)
else:
    st.plotly_chart(fig1)