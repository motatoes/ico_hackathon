import os
import json
import uuid
import subprocess
from flask import Flask
from flask import request, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)


UPLOAD_FOLDER = 'files'
# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['POST'])
def upload():
    ipfs_hash = ""
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return json.dumps({'error': 'no_file_in_request'})

        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return json.dumps({'error': 'no_file_uploaded'})
        
        if file:
            filename = secure_filename(str(uuid.uuid1()))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        process = subprocess.Popen(["ipfs", "add", "files/" + filename], stdout=subprocess.PIPE)
        ipfs_out, err = process.communicate()

        ipfs_hash = ipfs_out.split()[1]
        return json.dumps({'file': 'files/' + filename, 'hash': ipfs_hash})


    return json.dumps({'error': 'no_file_uploaded'})





