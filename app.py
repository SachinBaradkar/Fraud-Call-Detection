import streamlit as st
import speech_recognition as sr
import joblib

# Load trained model
model = joblib.load('fraud_detection_model1.pkl')

# Speech recognition function
def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        transcript = recognizer.recognize_google(audio_data)
    return transcript

# Streamlit app
def main():
    st.markdown(
        """
        <style>
        .reportview-container {
            background-color: #FFFFFF; /* White */
        }
        body {
            background-color: #FFFFFF; /* White */
            font-family: Arial, sans-serif;
            color: #333333; /* Dark gray */
        }
        .title-container {
            background-color: #2A0134; /* Green */
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 10px;
	
            box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
        }
        .upload-container {
            background-color: #000000; /* White */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
        }
        .upload-container1 {
            background-color: #000000; /* White */
            padding: 10px;
            border-radius: 20px;
            box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
        

        .red-background {
            background-color: #FF5733 !important; /* Red */
        }
        .predicted-label {
            font-size: 500px;
            font-weight: bold;
            color: #FF5733; /* Red */
        }
        h3 {
            color: black; 
        }
        h2 {
            color: red; 
        }
        .label { 
            font-size: 50px;
            font-weight: bold;
            color: #333333; /* Dark gray */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="title-container"><h1 style="color: white;">Fraud Call Detection</h1></div>', unsafe_allow_html=True)
    
    # Add marquee text with red background color
    st.markdown('<div style="background-color: #FF5733; padding: 10px;"><marquee style="color: white;">Be aware of fraud calls **** Cyber Crime HelpLine number 112 **** Register Cyber crime on portal www.cybercrime.gov.in ****</marquee></div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="upload-container1">
            <h3>Upload Audio File</h3>
            <h5>Upload the audio which you want to detect</h5>
        </div>
        """, unsafe_allow_html=True)
    
    # Upload audio file
    audio_file = st.file_uploader("", type=["mp3", "wav"])
    
    if audio_file:
        # Display loading spinner
        with st.spinner('Transcribing audio...'):
            transcript = transcribe_audio(audio_file)
        
        st.write("<br>", unsafe_allow_html=True) # Add some space
        
        # Display transcript inside the container
        st.markdown("<div class='upload-container'><h3>Transcript:</h3><p>%s</p></div>" % transcript, unsafe_allow_html=True)
        
        # Predict label
        label = model.predict([transcript])[0]
        
        # If label is scam, change background color to red
        if label == 'scam':
            st.markdown('<style>.upload-container { background-color: #FF5733 !important; }</style>', unsafe_allow_html=True)
        st.markdown( '' )
        st.markdown( '' )
        st.markdown( '' )

        # Display predicted label with styling
        st.markdown("<h3>Prediction:</h3>", unsafe_allow_html=True)
        st.markdown(f'<h2 class="predicted-label">{label}</h2>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
