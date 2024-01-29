import os
from flask import Flask, flash, request, redirect, url_for, render_template
import uuid
import logging

import video2pdfslides


# from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'static/videos'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

logging.basicConfig(level=logging.DEBUG)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            # filename = secure_filename(file.filename)
            id = str(uuid.uuid4()) + ".mp4"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], id))
            
            #splitting file into screenshots
            
            output_folder_screenshot_path = video2pdfslides.initialize_output_folder(UPLOAD_FOLDER + '/' + id) #initializing output folder
            video2pdfslides.detect_unique_screenshots(UPLOAD_FOLDER + '/' + id, output_folder_screenshot_path)
            # video2pdfslides.convert_screenshots_to_pdf(output_folder_screenshot_path)
            

            redirect(url_for('upload_file', name=id))
            return render_template('preview.html',name=id)
    return render_template('index.html')


