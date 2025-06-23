import os
from flask import Flask

app = Flask(__name__)

# Get greeting from environment variable, default to 'Hello, World!'
GREETING = os.environ.get('GREETING', 'Hello, World!')

@app.route('/')
def hello():
    # Return the greeting message
    return f'<h1>{GREETING}</h1>'

if __name__ == '__main__':
    # Run the app on 0.0.0.0 so it works in Docker
    app.run(host='0.0.0.0', port=5000) 