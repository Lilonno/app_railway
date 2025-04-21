from flask import Flask, render_template, jsonify
import json

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

if __name__ == '__main__':
    app.run(debug=True)



