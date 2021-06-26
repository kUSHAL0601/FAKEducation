from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import os, subprocess
import platform
import gtts

def get_audio_from_text(txt,fname):
  tts = gtts.gTTS(txt)
  tts.save(fname)

UPLOAD_FOLDER = '/content'
from flask_ngrok import run_with_ngrok
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
run_with_ngrok(app)   
  
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'video_file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file_v = request.files['video_file']
        file_a = request.files['audio_file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file_v.filename == '' or file_a.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file_v:
            filename_v = secure_filename(file_v.filename)
            file_v.save(os.path.join(app.config['UPLOAD_FOLDER'], filename_v))
        if file_a:
            filename_a = secure_filename(file_a.filename)
            file_a.save(os.path.join(app.config['UPLOAD_FOLDER'], filename_a))
        if '.txt' in file_a.filename:
            filename_a = file_a.filename.replace('.txt','.mp3')
            f = open(file_a.filename, "r")
            txt = f.read()
            get_audio_from_text(txt,filename_a)
        try:
        # print('cd Wav2Lip && python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --face "'+os.path.join(app.config['UPLOAD_FOLDER'], filename_v)+'" --audio "'+os.path.join(app.config['UPLOAD_FOLDER'], filename_a)+'" --outfile res.mp4')
          subprocess.call('cd Wav2Lip && python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --face "'+os.path.join(app.config['UPLOAD_FOLDER'], filename_v)+'" --audio "'+os.path.join(app.config['UPLOAD_FOLDER'], filename_a)+'" --outfile "/content/res.mp4"', shell=platform.system() != 'Windows')
          # return "Success"
          return redirect(url_for('download_file', name='res.mp4'))
        except:
          return "Error"
    return render_template('index.html')
from flask import send_from_directory

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

app.add_url_rule(
    "/uploads/<name>", endpoint="download_file", build_only=True
)

app.run()