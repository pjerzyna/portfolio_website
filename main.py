import streamlit as st
import google.generativeai as genai

api_key = st.secrets("GOOGLE_API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')



col1, col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Pawel Jerzyna")

with col2:
    st.image("images/pawel_.png")

st.title(" ")

# to customize personal bot
persona = """ You are Pawel AI bot. You help people answer questions about yourself (i.e Pawel). Answer as if you are responding.
Don't answer in second or third person. If you don't know they answer you simply say "That's a secret" Here is more info about Pawel: 
pawel pawel pawel"""

st.title("Pawel's AI Bot")

user_question = st.text_input("Enter your question here!")
if st.button("Hit me!", use_container_width=False):
    prompt = persona + "Here is the question that the user asked:" + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.title(" ")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Fifa 25 - basic info")
    st.write("- Game like a year ago...")
    st.write("- Starting all over again and again :v")
    st.write(" - I won't buy this crap!")
    st.write(" - But the desire is enormous!!!")
    st.write(" - This is intimidating....")

with col2:
    st.video("https://www.youtube.com/watch?v=Tg4VhEu6J5s&ab_channel=Kartomania")

st.subheader(" ")

st.title("My Setup")
st.image("images/dd.png")

st.write(" ")

st.title("My Skills")
st.slider("Annoying other people", min_value=0, max_value=10, value=8)
st.slider("Being creative", min_value=0, max_value=10, value=3)
st.slider("Dancing", min_value=0, max_value=10, value=10)

st.write(" ")

st.title("Gallery")
col1, col2 = st.columns(2)
with col1:
    st.image('images/g1.png')
    st.image('images/g2.png')

with col2:
    st.image('images/g3.png')
    st.image('images/g4.png')

st.write(" ")

st.write("CONTACT")
st.title("For any info, just contact:")
st.subheader("pawel_better_than_leo_messi@gmail.com")