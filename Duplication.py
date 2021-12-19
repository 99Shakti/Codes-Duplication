#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from functools import reduce
import streamlit as st
#upload=st.file_uploader("Choose a File")
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("url_goes_here")
    }
   .sidebar .sidebar-content {
        background: url("url_goes_here")
    }
    </style>
    """,
    unsafe_allow_html=True
)
#df=pd.read_csv(upload)
st.title("Hello Shakti")
st.header("Good Morning")
uploaded_file = st.file_uploader("Choose a file")
#uploaded_file1=uploaded_file.copy()
if uploaded_file is not None:
    uploaded_file.seek(0)
    df = pd.read_csv(uploaded_file)
df10=df.copy()

 #uploaded_file = st.file_uploader("Choose a file")
 #if uploaded_file is not None:
 #    uploaded_file.seek(0)
 #    df = pd.read_csv(uploaded_file, low_memory=False)
 #    #st.write(data.shape)
 #
def chars(df):
    #df=pd.read_excel("C:/Users/rash0007/Music/BIC BIC WET SHAVING PRODUCTS WSP CODE LIST.xlsx")
    df1=df[["value","code"]]
    df2= df1.drop_duplicates().reset_index(drop = True)
    df3=df2.drop('code', axis=1)
    sf=df3[df3["value"].duplicated() == True]
    v=sf.values.tolist()
    sl= [item for sublist in v for item in sublist]
    #sl = reduce(lambda x,y: x+y,v,1)
    #print(sl)
    df.set_index("value", inplace = True)  
    result = df.loc[sl]
    return result

result=chars(df)
def convert_df(result):
    result= result.to_csv().encode('utf-8')
    return result


csv=convert_df(result)

st.download_button(
   "Press to Download Description error",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)
#return result
#print(chars())
#rint(result)
 #uploader2=st.file_uploader("Choose a File")
df9=df10.copy()
def codes(df9):
    #df=pd.read_excel("C:/Users/rash0007/Music/BIC BIC WET SHAVING PRODUCTS WSP CODE LIST.xlsx")
    df1=df9[["value","code"]]
    df2= df1.drop_duplicates().reset_index(drop = True)
    df3=df2.drop('value', axis=1)
    sf=df3[df3["code"].duplicated() == True]
    v=sf.values.tolist()
    sl= [item for sublist in v for item in sublist]
    df9.set_index("code", inplace = True)
    result1 = df9.loc[sl]
    return result1
result1=codes(df9)
csv1=convert_df(result1)

st.download_button(
   "Press to Download Code Description error",
   csv1,
   "file.csv",
   "text/csv",
   key='download-csv'
)


