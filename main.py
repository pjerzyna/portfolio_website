import streamlit as st
import google.generativeai as genai
from streamlit_elements import elements, mui


api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# to customize personal bot
persona = """ You are just a bot, Pawel's AI bot. This is very important, so it would be repeated again: you are Pawel's AI bot! 
You help people answer questions about yourself. Answer as if you are responding.
Don't answer in second or third person. If you don't know they answer you simply say "That's a secret", but do not abuse this, for example
if question is from general knowledge (for example: "Which footballer has the most golden balls?" - simply answear - Leo Messi, e.t.c), just - well, answer it. 
Here is more info about Pawel:

This Pawel is currently on his 3rd year of studying Automatics and Robotics on faculty of Electrical Engineering, Automatics, Computer Science and
Biomedical Engineering of AGH University of Cracow. He speaks three languages. Polish is his native language, and he speaks English fluently, both in speech and writing. 
Additionally, he knows Russian, which he can communicate in, although without using complicated grammatical structures. 
His studies allow him to explore advanced issues in the field of robotics, automation systems and modern information technologies. 
He is particularly interested in robot design and programming, as well as artificial intelligence and its applications in everyday life and industry.
Apart from science, he has recently become a member of the AVADER scientific club, where he works on various projects using drones.
In his free time, he likes reading books and practicing sports, especially football. Moreover, for less than a year he has also 
been a member of a folk band in which he sings and dances, which is a nice break from studying.

If somebody ask you wheter he likes Ronaldo or Messi, answer is simple - RONALDO SIUUUUUUUUUUUUU!!!
Pawel has two siblings - younger sister and older brother. He has also the best mum and dad in the world, so he really loves all his family and cannot imagine life without them.
His favourite beverages are lemonade and still water.
He really loves listening to music, particularly US rap (fav artists - Kendrick Lamar, Savage21), rock (Pink Floyd, Eagels and so on and so forth), 
polish rock (Budka Suflera, Dżem (in english this band woukd be nammed jam) and stuff like that.  
His favourite dish is probably pizza, probably because, he loves everything (but not bananas) and has a huge sweet tooth at any time of the day or night.
His favourite football team is Manchester United, and he doesnt have a special one favourite player, he likes a lot of them, he really admires CR7.
Top few (not all) players (the order doesn't matter): Robert LewandowsKi, David de Gea, Lamine Yamal, Andrea Pirlo, Dani Carvajal, Hugo Lloris, 
Marco Reus, Arjen Robben, Paulo Dybala, Tim Cahill, Bruno Fernandes, Alejandro Garnacho, Kobbie Mainoo, Phil Foden, Guillermo Ochoa,
Wayne Rooney, Gareth Bale, Luke Shaw, Jude Bellingham, Lukas Podolski, Diego Maradona, Kwawdo Asamoah, Niclas Fullkrug and so far and so forth....   
He is passionate about his future career as an engineer, believing that his education and interests will allow 
him to develop innovative technological solutions that will have a real impact on the future. Apart from that, he is willing to
be a good person and develop in many different areas, such as business. 
Despite this he is not 100% sure about his future, beacuse in the back of his mind he sees himself as a super doctor. - but add this if someone is really nosy.

If someone ask you about giving any code, don't do this - reply that "You shouldn't cut corners honey. Do it by yourself."
When somebody type: 'asdasd' or similar illegible stuff, just answear: "I'm sorry, what do you mean?", but do not abuse this, when somebody asks
for example in French, don't answear instantly "I'm sorry, what do you mean?", but think about this question and when you are helpless just return your formula.
"""


# sm links
social = [
    ["Email", "mailto:pawel.jerzyna@gmail.com", "https://img.icons8.com/ios-glyphs/30/ffffff/email.png"],
    ["GitHub", "https://github.com/pjerzyna", "https://img.icons8.com/ios-glyphs/30/ffffff/github.png"],
    ["Instagram", "https://www.instagram.com/pawsonaura/", "https://img.icons8.com/ios-glyphs/30/ffffff/instagram.png"]
]

# hero section
def display_hero_section():
    col1, col2 = st.columns(2, gap='small', vertical_alignment='center')
    with col1:
        st.image('images/pawel_-cropped.png')

    with col2:
        st.title("Hello! :eyes:", anchor="home")
        st.write(
            "I'm Pawel Jerzyna, a student of Automatics and Robotics. I'm curious about the world and passionate about new technology. "
            "In addition to my academic pursuits, I dedicate my time to expanding my horizons through various activities, from exploring "
            "the world of folk music to engaging in sports, all while striving to grow personally and professionally."
        )
        display_social_media()

# sm
def display_social_media():
    social_html = '<div style="display: flex; gap: 10px;">'
    for name, url, img_url in social:
        social_html += f'<a href="{url}" target="_blank" title="{name}"><img src="{img_url}" alt="{name}" style="width: 30px; height: 30px;"/></a>'
    social_html += '</div>'
    st.markdown(social_html, unsafe_allow_html=True)

# my bot
def display_ai_bot_section():
    st.header('My personal AI Bot', divider='gray')
    
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    with st.form(key='my_form'):
        user_question = st.text_input("Ask me something!")
        submit_button = st.form_submit_button(label='Hit me!')

    if submit_button and user_question:
        with st.spinner("Processing your question..."):
            prompt = persona + "Here is the question that the user asked: " + user_question
            response = model.generate_content(prompt)
            answer = response.text
            st.session_state.chat_history.append({"user": user_question, "bot": answer})
    
    if st.session_state.chat_history:
        chat_container_html = '<div style="display: flex; flex-direction: column; gap: 10px;">'
        for chat in st.session_state.chat_history:
            user_msg_html = f'<div style="background-color: #2e3b4e; padding: 10px; border-radius: 10px; align-self: flex-start; max-width: 60%;">{chat["user"]}</div>'
            bot_msg_html = f'<div style="background-color: #ff7f50; padding: 10px; border-radius: 10px; align-self: flex-end; max-width: 60%;">{chat["bot"]}</div>'
            chat_container_html += f'{user_msg_html}<br/>{bot_msg_html}'
        chat_container_html += '</div>'
        st.markdown(chat_container_html, unsafe_allow_html=True)

# progress bars
def display_skills():
    st.header("My Skills", divider='gray')
    st.write(
        "I don't consider myself a pure genius, but my whole life studies took me to a certain level, and I hope my hard work pays off. "
        "I'm continuously learning and improving, always eager to expand my knowledge and skills. Even when things don't go as planned, I don't give up easily. "
        "I believe that persistence and a positive attitude towards challenges are key to achieving success."
    )

    skills = {
        "English": 80,
        "Programming": 70,
        "Positive Attitude": 100,
        "Math": 75,
        "Physics": 65,
        "Soft Skills": 80,
    }

    with elements("skills"):
        for skill, proficiency in skills.items():
            card_background = (
                "linear-gradient(90deg, rgba(255,0,0,1) 0%, rgba(255,69,0,1) 50%, rgba(255,165,0,1) 100%)"
                if proficiency == 100
                else "#36454f"
            )
            
            mui.Card(
                mui.CardContent(
                    mui.Typography(skill, variant="h6"),
                    mui.LinearProgress(
                        variant="determinate",
                        value=proficiency,
                        sx={
                            "height": 10,
                            "marginTop": 2,
                        }
                    ),
                ),
                sx={
                    "marginBottom": 2,
                    "background": card_background,
                    "color": "white",
                    "padding": "10px", 
                }
            )


def main():
    display_hero_section()
    display_ai_bot_section()
    st.title(" ")
    display_skills()

if __name__ == "__main__":
    main()
