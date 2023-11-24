#!/usr/bin/env python
# coding: utf-8

# In[13]:


import streamlit as st
import plotly.express as px
import pandas as pd
from openai import OpenAI


# In[14]:


st.title("Data Alchemy 🪄")

with st.sidebar:
        st.write("Inorder to access the app please enter your OpenAI API key first in the text box below: ")
        openai_api_key = st.text_input("Enter Your OpenAI API key")
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"


# In[15]:


if openai_api_key:
    
    openai.api_key = openai_api_key

    uploaded_file = st.file_uploader("Upload CSV file", type="csv")
    
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write(data.head())

        available_columns = data.columns
    
        st.write("Descriptive Statistics:")
        st.write(data.describe())

        most_informative_variable = data.describe().loc['std'].idxmax()
    
        st.write(f"The variable '{most_informative_variable}' might offer significant insights.")

        x_variable = st.selectbox("Select X variable", options=available_columns, index=0)
        y_variable = st.selectbox("Select Y variable", options=available_columns, index=1)

        fig = px.scatter(data, x=x_variable, y=y_variable)
        st.plotly_chart(fig)
    

    
        st.subheader("Why this variable?:")
        user_question = st.text_input("Ask a question")
        if user_question:
            st.subheader("Answer:")
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=f"I want insights on the variable '{most_informative_variable}'. User's question: '{user_question}'",
                max_tokens=100,
                api_key=openai_api_key
            )
            st.write(response.choices[0].text)


# In[ ]:





# In[ ]:




