import streamlit as st
import torch
from transformers import pipeline, set_seed
import time

st.set_page_config(page_title='Generative AI Demo', page_icon=':robot_face:')

# Load the GPT-2 model
generator = pipeline('text-generation', model='gpt2')

# Define a function to generate text
def generate_text(prompt):
    set_seed(40)
    text = generator(prompt, max_length=200, num_return_sequences=1)
    return text[0]['generated_text']

# Create the Streamlit app
def app():
    # Set the app title and description
    
    st.title('Generative AI Demo')
    st.write('This app demonstrates generative AI capabilities using GPT-2.')
    
    # Get user input prompt
    prompt = st.text_input('Enter a prompt:', '')
    
    # Generate text based on user input prompt
    if st.button('Generate Text'):
        if prompt:
            with st.spinner('Generating text...'):
                start_time = time.time()
                generated_text = generate_text(prompt)
                end_time = time.time()
            st.write('Generated Text:')
            st.write(generated_text)
            st.write(f'Time taken: {end_time - start_time:.2f} seconds ')
            st.write("\n")
            st.write("\n")
            st.write("\n")
            st.write("\n")

            #  Add a footnote
            st.markdown(
                """<sup>*</sup> Note: This app uses the GPT-2 model to generate \
                    text based on user input prompt. After entering a prompt and  \
                    clicking the "Generate Text" button, the app will display the \
                    generated text and the time taken to retrieve it. Please note \
                    that the text generation process may take some time depending \
                    on the complexity of the prompt and the performance of the system.""",
                unsafe_allow_html=True
            )


if __name__ == '__main__':
    app()
