#main.py
from appsite import app 

if __name__ == '__main__':
    app.run(app.config['HOST'], app.config['PORT'])