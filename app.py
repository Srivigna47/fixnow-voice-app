import streamlit as st
import whisper
import tempfile
import os

st.set_page_config(page_title="FixNow – Voice Complaint App")

st.title("🎤 FixNow – Voice Complaint App")

uploaded_audio = st.file_uploader("Upload your complaint audio (WAV/MP3)", type=["wav", "mp3", "m4a"])

if uploaded_audio is not None:
    st.audio(uploaded_audio)

    # Save the uploaded file to a temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(uploaded_audio.read())
        tmp_path = tmp.name

    st.info("Transcribing...")

    model = whisper.load_model("base")
    result = model.transcribe(tmp_path)

    st.success("Transcription complete!")
    st.text_area("📝 Complaint Text", result["text"], height=200)

    os.remove(tmp_path)
