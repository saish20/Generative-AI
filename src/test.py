import streamlit as st
import torch
from transformers import pipeline, set_seed

# Load the GPT-2 model
generator = pipeline('text-generation', model='gpt2')

# Define a function to generate text
def generate_text(prompt):
    set_seed(52)
    text = generator(prompt, max_length=200, num_return_sequences=1)
    return text[0]['generated_text']

# Create the Streamlit app
def app():
    # Set the app title and description
    st.set_page_config(page_title='Generative AI Demo', page_icon=':robot_face:', layout='wide')
    st.title('Generative AI Demo')
    
    # Create a two-column layout
    left_column, right_column = st.columns(2)
    
    # Add the markdown to the left column
    with left_column:
        st.write('This app demonstrates generative AI capabilities using GPT-2.')
    
    # Get user input prompt
    with right_column:
        prompt = st.text_input('Enter a prompt:', '')
    
    # Generate text based on user input prompt
    if prompt:
        generated_text = generate_text(prompt)
        st.write('Generated Text:')
        st.write(generated_text)

if __name__ == '__main__':
    app()
