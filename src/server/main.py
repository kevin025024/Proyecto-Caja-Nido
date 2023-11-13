from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = "imgs"

@app.route('/ping')
def ping():
   return "pong"
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True, host="10.9.121.15")