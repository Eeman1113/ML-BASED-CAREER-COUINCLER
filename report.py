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
    
    #RIP CUTIE CODE
    # a=['skill','skill','skill','skill','skill','skill','skill','sanndy','avi','sak']
    # r=round(len(a)/2)
    # img=Image.open("/Users/eemanmajumder/code_shit/ML-BASED-CAREER-COUINCLER/why_am_I_pain_hoing_crie_arra_fr/GPT_3_in_my_Ass/image/result1.png")
    # title_font = ImageFont.truetype('', 55)
    # x=1300.3
    # for i in range(0,5):
        
    #     title_text1 = (""+str(i+1)+". "+str(a[i])+"")
    #     image_editable = ImageDraw.Draw(img)
    #     image_editable.text((200,x),title_text1, (0,0,0), font=title_font)
    #     img.save("/Users/eemanmajumder/code_shit/ML-BASED-CAREER-COUINCLER/why_am_I_pain_hoing_crie_arra_fr/GPT_3_in_my_Ass/image/result2.png")
    #     x=x+70
    
    # y=1300.3
    # for i in range(6,len(a)):
        
    #     title_text1 = (""+str(i)+". "+str(a[i])+"")
    #     image_editable = ImageDraw.Draw(img)
    #     image_editable.text((700,y),title_text1, (0,0,0), font=title_font)
    #     img.save("/Users/eemanmajumder/code_shit/ML-BASED-CAREER-COUINCLER/why_am_I_pain_hoing_crie_arra_fr/GPT_3_in_my_Ass/image/final.png")
    #     y=y+70
    
    return "image/final.png"


