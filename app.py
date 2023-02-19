import openai
import streamlit as st
import pandas as pd
from report import make_report

def clicks(prompt,name,skills):
    openai.api_key = st.secrets['open_api']

    response = openai.Completion.create(
        engine="text-curie-001",
        prompt=prompt,
        temperature=0.7 ,
        max_tokens=2000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    b=response
    # st.write(st.markdown())
    st.write(response.choices[0].text)
    st.balloons()
    return response.choices[0].text
    



def se():
    x=True



st.markdown("<h1 style='text-align: center; '>Career Coupler ㊫</h1>", unsafe_allow_html=True)
name=st.text_input("Enter Your Name")
st.text_input("What Region Do You Live In")
st.date_input("Enter Date Of Birth")
df=pd.read_csv("skills.csv")
a=df['skills']
skills=st.multiselect("What are you good at?",a)
st.write('You selected:', skills)

prompt="Suggest me 10 Jobs Positions based on my skils and describe all the careers suggested.\n My Skills are: "+str(skills)

print(type(skills))
r=st.button("Unfuse Me")
while r==True:
    resp=clicks(prompt,name,skills)
    print(name)
    print(skills)
    print(resp)
    st.image(make_report(name=name,skills=skills,output=resp))
    print("Die eeamn die")

    r=False

