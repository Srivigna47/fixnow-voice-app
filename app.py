import streamlit as st
import openai
import os
import tempfile

# Title
st.title("FixNow – Voice Complaint Transcription")

# Upload audio
st.header("Upload your complaint audio (WAV/MP3)")
uploaded_file = st.file_uploader("Drag and drop file here", type=["wav", "mp3", "m4a"])

# Transcribe section
if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/wav")
    st.info("Transcribing...")

    # Save file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as temp_audio:
        temp_audio.write(uploaded_file.read())
        temp_audio_path = temp_audio.name

    try:
        # Load API key from Streamlit secrets
        openai.api_key = st.secrets["OPENAI_API_KEY"]

        # Use Whisper API
        with open(temp_audio_path, "rb") as audio_file:
            transcript = openai.Audio.transcribe("whisper-1", audio_file)

        # Display result
        st.success("Transcription Complete:")
        st.write(transcript["text"])

    except Exception as e:
        st.error(f"Error: {e}")

    # Delete temp file
    os.remove(temp_audio_path)

