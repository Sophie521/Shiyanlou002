from flask import Flask, render_template
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('/home/shiyanlou/news/files/helloshiyanlou.json') as file:
        text1 = json.loads(f.read())
    with open('/home/shiyanlou/news/files/helloworld.json') as file:
        text2 = json.loads(f.read())   
    return render_template('index.html',text1 = text1,text2 = text2)

@app.route('/files/<filename>')
def file(filename):
    with open('/home/shiyanlou/news/files/{}.json'.format(filename)) as file:
        file_item = json.loads(f.read())
    return render_templates('file.html',file_item = file_item)
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run()
