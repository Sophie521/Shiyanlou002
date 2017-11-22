from flask import Flask, render_template
import os
import json

app = Flask(__name__)


......pass
...


@app.route('/')
def index():
    return render_template('index.html',title_list = files.get_title_list())

@app.route('/files/<filename>')
def file(filename):
    file_item =  files.get_filename(filename)
    return render_templates('file.html',file_item = file_item)
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run()
