import os  # Add this import statement
from gtts import gTTS

def text_to_speech(translations, output_folder):
    audio_files = []
    for lang, text in translations.items():
        tts = gTTS(text=text, lang='hi' if lang == 'Hindi' else 'ta' if lang == 'Tamil' else 'te')
        filename = f"{lang}.mp3"
        filepath = os.path.join(output_folder, filename)
        tts.save(filepath)
        audio_files.append(filename)
    return audio_files
