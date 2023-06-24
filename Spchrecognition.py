import streamlit as st
import sys; print(sys.path)
import os
import numpy as np
from pydub import AudioSegment
import speech_recognition as sr

def main():
    st.title("Speech Recognition App")
    st.write("Upload an audio file to start:")

    # add a file uploader to the Streamlit app
    uploaded_file = st.file_uploader("Choose an audio file:")

    # check if a file was uploaded
    if uploaded_file is not None:
        # get the file data
        audio_data = uploaded_file.read()

        # add a selectbox to choose the speech recognition API
        api_options = ["Google Speech Recognition", "Deepgram"]
        api_choice = st.selectbox("Choose Speech Recognition API:", api_options)

        # add a selectbox to choose the language
        language_options = ["en-US", "fr-FR", "es-ES", "de-DE"]
        language_choice = st.selectbox("Choose Language:", language_options)

        # add a button to trigger speech recognition
        if st.button("Start Transcription"):
            text = transcribe_speech(api_choice, language_choice, audio_data)
            st.write("Transcription: ", text)

            # ask the user if they want to save the transcription
            if st.checkbox("Save transcription to file?"):
                filename = st.text_input("Enter filename:")
                if filename:
                    save_transcription_to_file(text, filename)
                    st.success(f"Transcription saved to file: {filename}")

def transcribe_speech(api_choice, language_choice, audio_data):
    st.info("Transcribing...")

    try:
        if api_choice == "Google Speech Recognition":
            # convert audio_data to the format required by recognize_google
            audio_segment = AudioSegment.from_file(audio_data, format="wav")
            flac_data = audio_segment.export(format="flac")
            # use flac_data with recognize_google
            pass
        elif api_choice == "Deepgram":
            # using Deepgram
            # convert audio_data to the format required by Deepgram
            pass
        return text
    except sr.RequestError as e:
        # API was unreachable or unresponsive
        return f"Sorry, there was an error reaching the API: {e}"
    except sr.UnknownValueError:
        # speech was unintelligible
        return "Sorry, I could not understand what you said."
    except Exception as e:
        # other error occurred
        return f"Sorry, an error occurred: {e}"

def recognize_with_deepgram(audio_text, language_choice):
    # code to use Deepgram API for speech recognition with the specified language
    pass

def save_transcription_to_file(text, filename):
    # create the directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    # write the transcription to the file
    with open(filename, "w") as f:
        f.write(text)

if __name__ == "__main__":
    main()