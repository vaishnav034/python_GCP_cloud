from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Cloud Run! This is a Python CI/CD example using Cloud Build.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
