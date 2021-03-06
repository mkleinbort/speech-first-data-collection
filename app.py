import streamlit as st
import uuid
from helper import *
import os

os.system('ls')
os.system('sudo apt-get install libsndfile1')

st.set_page_config(layout="wide")

session_id = uuid.uuid1()
st.title('Speech First Data Collection')

st.code(f'This session id is {session_id}')

st.markdown('''
### Thank you!
Capgemini UK is developing an app to help people with speech dificulties improve their
speech though better access to speech therapists and real-time feedback

We'd really appreciate your help in recording some examples of what healthy pronunciations should sound like.
These recordings are compleately anonymous and will only be used to train an AI model to give feedback on how the
patient might improve their pronunciation.

There is no one way to pronounce these prompts - the more examples we can get, the more fair an inclusive our app will be.

Optional: If you are willing to provide some metadata we'll use that to test our model for fairness.

''')

with st.beta_expander('Optional: Metadata for Fairness scoring'):

    st.markdown('''
    ### Fairness data

    The sound recordings will be saved using filename:

        'session-{id}-gender-{gender}-age-{age}-prompt-{prompt}-timestamp-{time}.wav'

    ''')

    # 'session-2x3416e-gender-F-age-30-prompt-ah-pah-timestamp-2021-05-03:12:21:11.wav'

    col1, col2, col3 = st.beta_columns(3)
    with col1:
        gender = st.selectbox('Gender', ['', 'M','F'])
    
    with col2:
        age = st.selectbox('Age', ['', '~20','~40', '~60', '~80'])
    
    with col3:
        accent = st.selectbox('Accent',['','England','Scottland','Other'])

    st.write(f'''
        
        Your files will be saved as:

            'session-{session_id}-gender-{gender}-age-{age}-prompt-{"PROMPT"}-timestamp-{"TIME"}.wav'

        ''')
    

if st.button(f"Click to Record"):
    if filename == "":
        st.warning("Choose a filename.")
    else:
        record_state = st.text("Recording...")

        duration = 5  # seconds
        fs = 48000
        myrecording = record(duration, fs)
        record_state.text(f"Saving sample as {filename}.mp3")


        path_myrecording = f"./samples/{filename}.mp3"

        save_record(path_myrecording, myrecording, fs)
        record_state.text(f"Done! Saved sample as {filename}.mp3")

        st.audio(read_audio(path_myrecording))

        fig = create_spectrogram(path_myrecording)
        st.pyplot(fig)

