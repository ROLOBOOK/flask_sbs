from app import app
from flask import render_template
import os, time
from flask import request
from flask import redirect


def work_with_page(page,files):
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    stop = 8
    last_page = len(files)/stop
    if page == 1:
        files = files[:stop]
    else:
        start = stop * (page - 1)
        end = stop * (page)
        files = files[start:end]  
     
    return (page, last_page, files)
        
@app.route('/', methods=['POST','GET'])
def index():
    return render_template('main.html')



    
@app.route('/to_pos/', methods=['GET','POST'])
def list_pos():
    page = request.args.get('page')
    files = os.listdir(r'for_print\to_pos')
    page, last_page, files = work_with_page(page,files)
    return render_template('index.html',page=page,last_page=last_page, files=files, dir_file='to_pos')    


@app.route('/to_kadri/', methods=['GET','POST'])
def list_kard():
    page = request.args.get('page') #page = 123  localhost:5000/?page=123 
    files = os.listdir(r'for_print\кадровые вопросы')
    page, last_page, files = work_with_page(page,files)
    return render_template('index.html',page=page,last_page=last_page, files=files, dir_file='кадровые вопросы')    

@app.route('/to_arm/', methods=['GET','POST'])
def list_apm():
    page = request.args.get('page')
    files = os.listdir(r'for_print\АРМ')
    page, last_page, files = work_with_page(page,files)
    return render_template('index.html',page=page,last_page=last_page, files=files, dir_file='АРМ')  
    
@app.route('/to_eirs/', methods=['GET','POST'])
def list_eirs():
    page = request.args.get('page')
    files = os.listdir(r'for_print\ЕИРС')
    page, last_page, files = work_with_page(page,files)
    return render_template('index.html',page=page,last_page=last_page, files=files, dir_file='ЕИРС')  
    
@app.route('/to_ot/', methods=['GET','POST'])
def list_ot():
    page = request.args.get('page')
    files = os.listdir(r'for_print\КТО_ОТ')
    page, last_page, files = work_with_page(page,files)
    return render_template('index.html',page=page,last_page=last_page, files=files, dir_file='КТО_ОТ')
    
@app.route('/to_suo/', methods=['GET','POST'])
def list_suo():
    page = request.args.get('page')
    files = os.listdir(r'for_print\СУО')
    page, last_page, files = work_with_page(page,files)
    return render_template('index.html',page=page,last_page=last_page, files=files, dir_file='СУО')
    




# для печати    
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
    return render_template('wait.html')


@app.errorhandler(404)
def do_not_found_page(error):
    return render_template('404.html'),404

@app.errorhandler(500)
def do_not_found_page(error):
    return render_template('500.html'),500
