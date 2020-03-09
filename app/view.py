from app import app
from flask import render_template
import os
from flask import request
from flask import redirect


    
@app.route('/to_pos/', methods=['GET','POST'])
def list_pos():
    
    files = os.listdir(r'for_print\to_pos')
    return render_template('index.html', files=files, dir_file='to_pos')

@app.route('/to_kadri/', methods=['GET','POST'])
def list_kard():
    a = 'to_kadri'
    files = os.listdir(r'for_print\кадары')
    return render_template('index.html', files=files, dir_file='кадары')    
    
@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')
    
@app.route('/to_print/', methods=['GET','POST'])
def printing():
    file_print = request.form['index']
    dir_file = request.form['path']
    os.startfile(f"for_print\{dir_file}\{file_print}", "print")   
    return redirect('/')


#os.startfile("YourDocument", "print")
