from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/hello/')
def hello():
    return 'Hello World!\n'

@app.route('/hello/<username>')
def hello_user(username):
    return f'Hello {username}!\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
