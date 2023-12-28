import streamlit as st
import os
from monsterapi import client

def imagen(prompt):
    os.environ['MONSTER_API_KEY'] = os.getenv('MONSTERAI_API_KEY')
    monster_client = client()
    
    print(f"Generating image...")
    response = monster_client.get_response(model='sdxl-base', data={'prompt': prompt, 'negprompt': 'unreal, fake, meme, joke, disfigured, poor quality, bad, ugly', 'samples': 1, 'steps': 40, 'aspect_ratio': 'square', 'guidance_scale': 8.5})
    imageList = monster_client.wait_and_get_result(response['process_id'],timeout=200)
    print("Displaying generated images:")
    for imageURL in imageList['output']:
        return imageURL


st.set_page_config(page_title="Generate image via text prompt",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate image via text prompt 🤖")
st.caption("\u00A9 Tahmid Hossain")
col1, col2 = st.columns([.45,.55], gap ="large")
with col1: 
    st.header("Prompt")
    with st.form("prompt", clear_on_submit=False):
        prompt = st.text_area("Enter your prompt here")
        submit_button = st.form_submit_button(label="Generate")

with col2: 
    st.header("Image")
    if submit_button:
        image = imagen(prompt)
    if submit_button:
        st.image(image)
