from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/nosotros')
def nostros():
    return render_template('sitio/nosotros.html')

if __name__=='__main__':
    app.run(debug=True)
