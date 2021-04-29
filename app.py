import streamlit as st
import uuid


session_id = uuid.uuid1()
st.title('Speech First Data Collection')

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

    e.g.

        'session-2x3416e-gender-F-age-30-prompt-ah-pah-timestamp-2021-05-03:12:21:11.wav'
    ''')

    gender = st.select_box('Gender', ['', 'M','F'])
    age = st.select_box('Age', ['', '~20','~40', '~60', '~80'])
    
    st.write(f'''
    
    Your files will be saved as:

        'session-{session_id}-gender-{gender}-age-{age}-prompt-{"PROMPT"}-timestamp-{"TIME"}.wav'

    ''')
    

