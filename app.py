import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import tempfile

# Page Configuration
st.set_page_config(
    page_title="Language Translator",
    page_icon="🌍"
)

# Heading
st.title("🌍 Language Translation Tool")
st.write("Translate text from one language to another.")

# Languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN"
}

# Text Input
text = st.text_area(
    "Enter Text",
    height=150
)

# Source Language
source_language = st.selectbox(
    "Select Source Language",
    list(languages.keys())
)

# Target Language
target_language = st.selectbox(
    "Select Target Language",
    list(languages.keys())
)

# Translate Button
if st.button("Translate"):

    if text.strip() != "":

        translated_text = GoogleTranslator(
            source=languages[source_language],
            target=languages[target_language]
        ).translate(text)

        st.subheader("Translated Text")

        st.success(translated_text)

        st.code(translated_text)

        st.info("You can copy the translated text above.")

        # Text To Speech
        tts = gTTS(text=translated_text, lang=languages[target_language])

        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3"
        )

        tts.save(temp_file.name)

        audio_file = open(temp_file.name, "rb")

        st.audio(audio_file.read(), format="audio/mp3")

    else:
        st.warning("Please enter some text.")