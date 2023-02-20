#____________________________________________________________________________________________________________________________________________________
import openai
import streamlit as st
import pandas as pd
# from report import make_report
#____________________________________________________________________________________________________________________________________________________
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
#____________________________________________________________________________________________________________________________________________________

def make_report(name,skills,output):
    #Name
    from PIL import Image, ImageFont, ImageDraw 
    img=Image.open("image/Hello!.png")
    title_font = ImageFont.truetype('font/KgThisIsNotGoodbye-opGV.ttf', 150)
    title_text = str(name)

    W,H = img.size
    image_editable = ImageDraw.Draw(img)
    _, _, w, h = image_editable.textbbox((0, 0), title_text, font=title_font)
    image_editable.text(((W-w)/2, 375), title_text, font=title_font, fill=(0,0,0))
    # image_editable.text((400,375), title_text, (0,0,0), font=title_font)
    img.save("image/result.png")


    #Skills
    a=skills
    r=round(len(a)/2)
    img=Image.open("image/result.png")
    title_font = ImageFont.truetype('font/Lora-VariableFont_wght.ttf', 55)
    title_text1 = str(a[:r])
    title_text2 = str(a[r:])
    image_editable = ImageDraw.Draw(img)
    image_editable.text((200,850.3),title_text1, (0,0,0), font=title_font)
    image_editable.text((200,950.3),title_text2, (0,0,0), font=title_font)
    img.save("image/result1.png")

    

    #Suggestions
    a=output
    img=Image.open("image/result1.png")
    title_font = ImageFont.truetype('font/Lora-VariableFont_wght.ttf', 40)
    image_editable = ImageDraw.Draw(img)
    image_editable.text((200,1250),a, (0,0,0), font=title_font)
    img.save("image/final.png")
#____________________________________________________________________________________________________________________________________________________

def se():
    x=True
#____________________________________________________________________________________________________________________________________________________


st.markdown("<h1 style='text-align: center; '>Career Coupler ㊫</h1>", unsafe_allow_html=True)
name=st.text_input("Enter Your Name")
st.text_input("What Region Do You Live In")
st.date_input("Enter Date Of Birth")
df=pd.read_csv("skills.csv")
a=df['skills']
skills=st.multiselect("What are you good at?",a)
st.write('You selected:', skills)
#____________________________________________________________________________________________________________________________________________________

prompt="Suggest me 10 Jobs Positions based on my skils and describe all the careers suggested.\n My Skills are: "+str(skills)

#____________________________________________________________________________________________________________________________________________________

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

#____________________________________________________________________________end_of_project_____________________________________________________________________
