import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory, Response, jsonify, send_file
from werkzeug.utils import secure_filename
import fileUtil as fileUtil
import speechUtil as speechUtil
import articleUtil as articleUtil
from random import randrange


UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx', 'pptx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = "liz"
app.config['SESSION_TYPE'] = 'filesystem' 
app.config['SESSION_PERMANENT']= False


@app.route('/test')
def hello():
    data = {'res':'Hello World!'}
    return jsonify(data)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        fileUtil.clean_up_files()
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return Response("Bad Request",status=400)

        file = request.files['file']

        filenameWithoutSpaces = file.filename.replace(" ", "_")

        if file and allowed_file(filenameWithoutSpaces):
            filename = secure_filename(filenameWithoutSpaces)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                        
            task = fileUtil.readFromFile(filename)
            fileNameWithoutExt = (filename.rsplit( ".", 1 )[ 0 ] )
            data = {'audio':fileNameWithoutExt+".mp3"}
            if(task):
                return jsonify(data)
            else:
                return Response("Something went wrong, please check if your file is valid.",status=400)
    except:
        return Response("Something went wrong, please check if your file is valid.",status=500)



@app.route('/text', methods=['POST'])
def upload_text():
    fileUtil.clean_up_files()
    text = request.form['text']
    print(text)

    randNum = randrange(1,900)

    filename = secure_filename("temp" + str(randNum))
    speechUtil.synthesize_and_save_to_file(text, filename)
    data = {'audio':filename+".mp3"}
    return jsonify(data)

@app.route('/audio/<string:name>', methods=['GET'])
def get_file(name):
    return send_file("output/" + name, as_attachment=True)

@app.route('/article', methods=['POST'])
def process_article():
    fileUtil.clean_up_files()
    articleLink = request.form['articleLink']
    print(articleLink)
    articleAudioFile = articleUtil.process_article(articleLink)
    data = {'audio':articleAudioFile+".mp3"}
    return jsonify(data)

app.run(port=5000)