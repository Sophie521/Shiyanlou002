from flask import Flask, render_template
import os
import json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    with open('/home/shiyanlou/news/files/helloshiyanlou.json') as file:
        text1 = json.loads(file.read())
    with open('/home/shiyanlou/news/files/helloworld.json') as file:
        text2 = json.loads(file.read())   
    return render_template('index.html',text1 = text1,text2 = text2)

@app.route('/files/<filename>')
def file(filename):
    with open('/home/shiyanlou/news/files/{}.json'.format(filename)) as file:
        text = json.loads(file.read())
    return render_templates('file.html',text = text)
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run()
