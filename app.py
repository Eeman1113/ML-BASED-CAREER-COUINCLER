import openai
import streamlit as st
import pandas as pd
import openai
def clicks(prompt):
    openai.api_key = "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"

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

def se():
    x=True



st.markdown("<h1 style='text-align: center; '>Career Coupler ㊫</h1>", unsafe_allow_html=True)
st.text_input("Enter Your Name")
st.text_input("What Region Do You Live In")
st.date_input("Enter Date Of Birth")
df=pd.read_csv("/Users/eemanmajumder/code_shit/ML-BASED-CAREER-COUINCLER/why_am_I_pain_hoing_crie_arra_fr/GPT_3_in_my_Ass/skills.csv")
a=df['skills']
skills=st.multiselect("What are you good at?",a)
st.write('You selected:', skills)

prompt="Suggest me 10 Jobs Positions based on my skils and describe all the careers suggested.\n My Skills are: "+str(skills)

r=st.button("Unfuse Me")
while r==True:
    clicks(prompt)
    r=False

