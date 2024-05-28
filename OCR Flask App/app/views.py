# importing files
from app import app
from flask import request, render_template, url_for
import os
import cv2
import numpy as np
from PIL import Image
import string
import pytesseract
from datetime import datetime

# Adding path to config
app.config['INITIAL_FILE_UPLOADS'] = 'app/static/uploads'


#route to home page
@app.route('/', methods=['GET', 'POST'])
def index():

    # get request
    if request.method == 'GET':
        full_filename = 'static/images/white_bg.jpg'
        return render_template('index.html', full_filename = full_filename)

    # for POST
    if request.method == 'POST':
        image_upload = request.files['image_upload']
        imagename = image_upload.filename
        image = Image.open(image_upload)

        # Convert image to array
        img_arr = np.array(image.convert('RGB'))
        gray_image = cv2.cvtColor(img_arr, cv2.COLOR_BGR2GRAY)
        image = Image.fromarray(gray_image)

        # Generating unique image name for dynamic naming
        d_time = datetime.now().time()
        name = imagename
        full_filename = os.path.join(app.config['INITIAL_FILE_UPLOADS'], name).replace("\\", "/")

        # extracting text form image
        custom_config = r'-l eng --oem 3 --psm 6'
        # english, ocr engine mode, page segmentation mode used for segmenting text from image
        text = pytesseract.image_to_string(image, config=custom_config)

        # remove symbol if any
        character_to_remove = "!()@—*“>+-/,'|£#%$&^_~"
        new_string = text
        for character in character_to_remove:
            new_string = new_string.replace(character, '')

        new_string = new_string.split('\n')

        img = Image.fromarray(img_arr, 'RGB')
        img.save(os.path.join(app.config['INITIAL_FILE_UPLOADS'], name).replace("\\", "/"))
        # Returning template, filename, extracted text
        return render_template('index.html', full_filename = full_filename, text = new_string)

@app.route("/About")
def about():
    image= 'images/ocr.png'
    return render_template('About.html', full_filename=image)

@app.route("/Contact")
def contact():
    return render_template('Contact.html')

if __name__ == '__main__':
    app.run(debug = True)