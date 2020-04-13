from app import app
from flask import render_template
import os
from flask import request
from flask import redirect


    
@app.route('/to_pos/', methods=['GET','POST'])
def list_pos():
    
    files = os.listdir(r'for_print\to_pos')[:9]
    return render_template('index.html', files=files, dir_file='to_pos')

@app.route('/to_kadri/', methods=['GET','POST'])
def list_kard():
    files = os.listdir(r'for_print\кадровые вопросы')[:9]
    return render_template('index.html', files=files, dir_file='кадровые вопросы')    

@app.route('/to_arm/', methods=['GET','POST'])
def list_apm():
    files = os.listdir(r'for_print\АРМ')[:9]
    return render_template('index.html', files=files, dir_file='АРМ')  
    
@app.route('/to_eirs/', methods=['GET','POST'])
def list_eirs():
    files = os.listdir(r'for_print\ЕИРС')[:9]
    return render_template('index.html', files=files, dir_file='ЕИРС')  
    
@app.route('/to_ot/', methods=['GET','POST'])
def list_ot():
    files = os.listdir(r'for_print\КТО_ОТ')[:9]
    return render_template('index.html', files=files, dir_file='КТО_ОТ')
    
@app.route('/to_suo/', methods=['GET','POST'])
def list_suo():
    files = os.listdir(r'for_print\СУО')[:9]
    return render_template('index.html', files=files, dir_file='СУО')
    
@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')
    
@app.route('/to_print/', methods=['GET','POST'])
def printing():
    file_print = request.form['index']
    dir_file = request.form['path']
    go_print = f"for_print\{dir_file}\{file_print}"
    #os.startfile(go_print, "print") 
    
    return render_template('count_copy.html', go_print=go_print)

@app.route('/to_copy/', methods=['GET','POST'])
def to_copy():
    go_print = request.form['index']
    count = request.form['count']
    for i in range(int(count)):
        os.startfile(go_print, "print")
    
    return redirect('/')

#os.startfile("YourDocument", "print")
