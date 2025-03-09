import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


st.title("Hello World 🐙")
st.markdown(
    """ 
    This is a :blue[**Streamlit**] app.

    You can use it to build and share beautiful web apps for your data science projects.

    **There's :rainbow[so much] you can build!**
  
    Gathering some examples to showcase what Streamlit can do.
    """
)

if st.button("Send balloons!"):
    st.balloons()



# streamlit bar chart
# Create a sample dataframe
data = pd.DataFrame({
  'Fruits': ['Apples', 'Oranges', 'Bananas', 'Grapes'],
  'Quantity': [15, 25, 35, 45]
})
 
# Create a bar chart
st.bar_chart(data)



# streamlit line chart
# Create a sample dataframe
data = pd.DataFrame({
  'Year': [2018, 2019, 2020, 2021],
  'Sales': [350, 480, 550, 680]
})
 
# Create a line chart
st.line_chart(data)



# streamlit pie chart
# Data to plot
labels = 'Python', 'Java', 'C++', 'JavaScript'
sizes = [215, 130, 245, 210]

# Create a pie chart with explicit figure
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')

# Display the plot in Streamlit with the figure argument
st.pyplot(fig)




# Create a 3D scatter plot
fig = px.scatter_3d(x=[1, 2, 3, 4], y=[4, 3, 2, 1], z=[1, 4, 2, 3])
st.plotly_chart(fig)