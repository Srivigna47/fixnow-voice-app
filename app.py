import streamlit as st
import speech_recognition as sr

st.set_page_config(page_title="FixNow – Voice Complaint App", page_icon="🎤")

st.title("🎤 FixNow – Voice-Based Complaint App")
st.write("Speak up and let us fix your local problems!")

if st.button("🎙 Start Recording"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Please speak clearly.")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            st.success("You said: " + text)

            # Optional: Save to file
            with open("complaints.txt", "a") as f:
                f.write(text + "\n")

        except sr.UnknownValueError:
            st.error("Could not understand your voice.")
        except sr.RequestError:
            st.error("Speech service not available.")
        except Exception as e:
            st.error(f"Error: {e}")
