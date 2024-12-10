import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

st.title("Story Generation")
name=st.text_input("Charater's Name", "Rajesh Andra")
persona=st.text_input("Character's Persona", "A smart young man with cold persona")
theme=st.multiselect("Genres", ['Sci-Fi','Mystery','Thriller','Romance','Horror','Crime','Fantasy','Drama','Adventure'], ['Sci-Fi','Thriller','Adventure','Mystery'])
imp=st.text_input("Brief Description","None")

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

prompt=f"""Write a long story based on the following premise: 

    character_name: {name} 

    character_persona: {persona} 

    genres: {theme}

    description:{imp}

    The story should be based on the above premise and story should atleast have 10 chapters.
    If description is not "None" or empty, make sure that the story follows the description.
    The story should have a proper introduction and conclusion.
    The story should be creative and include twist wherever required.
    If story is based on 'Sci-Fi' and 'Thriller' then story should follow a non-linear plot and the story should also be hard to understand. A clear ending may or may not exist in these type of genres.
    For other generes provide story accordingly.
    """

submit=st.button("Submit")

if submit:
    response = chat_session.send_message(prompt)
    st.write(response.text)