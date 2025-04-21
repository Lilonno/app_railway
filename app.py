from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def accueil():
    return render_template('index.html')

@app.route('/projets')
def projets():
    with open('static/projets.json', encoding='utf-8') as f:
        projets = json.load(f)
    return render_template('projets.html', projets=projets)

@app.route('/contact')
def contact():
    return render_template('contact.html')



import os

render_port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=render_port, debug=True)

