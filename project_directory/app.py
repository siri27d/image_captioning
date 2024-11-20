from flask import Flask, request, render_template, send_from_directory
import os
from models.blip_model import generate_caption
from models.indictrans_model import translate_text
from models.whisper_model import text_to_speech

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/uploads/'
app.config['OUTPUT_FOLDER'] = './static/outputs/'

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file uploaded", 400

        file = request.files['file']
        if file.filename == '':
            return "No selected file", 400
        
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        caption = generate_caption(filepath)
        translations = translate_text(caption)
        audio_files = text_to_speech(translations, app.config['OUTPUT_FOLDER'])

        return render_template('index.html', caption=caption, translations=translations, audio_files=audio_files)
    
    return render_template('index.html')

@app.route('/static/outputs/<filename>')
def download_file(filename):
    return send_from_directory(app.config['OUTPUT_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
