import streamlit as st
import pocketsphinx
import sys; print(sys.path)
from pocketsphinx import LiveSpeech, get_model_path
import os
import sounddevice as sd
import numpy as np

def main():
    st.title("Speech Recognition App")
    st.write("Click on the microphone to start speaking:")

    # add a selectbox to choose the speech recognition API
    api_options = ["Google Speech Recognition", "Deepgram"]
    api_choice = st.selectbox("Choose Speech Recognition API:", api_options)

    # add a selectbox to choose the language
    language_options = ["en-US", "fr-FR", "es-ES", "de-DE"]
    language_choice = st.selectbox("Choose Language:", language_options)

    # add a button to trigger speech recognition
    if st.button("Start Recording"):
        text = transcribe_speech(api_choice, language_choice)
        st.write("Transcription: ", text)

        # ask the user if they want to save the transcription
        if st.checkbox("Save transcription to file?"):
            filename = st.text_input("Enter filename:")
            if filename:
                save_transcription_to_file(text, filename)
                st.success(f"Transcription saved to file: {filename}")

def transcribe_speech(api_choice, language_choice):
    # Initialize recognizer class
    r = sr.Recognizer()
    # Reading Microphone as source
    with sr.Microphone() as source:
        st.info("Speak now...")
        recording = True
        while recording:
            # record audio
            audio = sd.rec(int(5 * 44100), samplerate=44100, channels=2)
            sd.wait()

            # add buttons to pause and resume recording
            col1, col2 = st.columns(2)
            if col1.button("Pause Recording"):
                recording = False
            if col2.button("Resume Recording"):
                recording = True

        # listen for speech and store in audio_text variable
        audio_text = r.listen(source)
        st.info("Transcribing...")

        try:
            if api_choice == "Google Speech Recognition":
                # using Google Speech Recognition
                text = r.recognize_google(audio_text, language=language_choice)
            elif api_choice == "Deepgram":
                # using Deepgram
                text = recognize_with_deepgram(audio_text, language_choice)
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
