#application.py

# System Dependecies 
from flask import Flask, render_template
# Initialize
app = Flask(__name__)
# Configure
app.config['PORT'] = 12600
app.config['HOST'] = '0.0.0.0'
app.config['SECRET_KEY'] = 'ghana tribes'


@app.route('/')
def index():
    return render_template('index.html')

