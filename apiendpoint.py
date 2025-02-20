from flask import Flask, jsonify
import subprocess

# pip install flask
# set up a virtual environment for your project if you don't have one already
# endpoint to retrieve the current date
# upon running hit http://127.0.0.1:5000/date
# you should then see a data JSON response

app = Flask(__name__)

@app.route('/date', methods=['GET'])
def get_date():
    result = subprocess.check_output(['date']).decode('utf-8')
    return jsonify({'date': result.strip()})

if __name__ == '__main__':
    app.run()
