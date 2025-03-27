'''
Basic Python microservice using Flask. Includes a profile check, greet request handling, 
and POST request processing. A production microservice would involve adding more complex logic, 
database interaction, error handling, and potentially using a message broker (e.g. RabbitMQ, 
Kafka, Redis, etc.) for inter-service communication.
'''

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/profile', methods=['GET'])
def profile_check():
    return jsonify({"status": "ok"}), 200

@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return jsonify({"data": f"Hola, {name}!"}), 200

@app.route('/process', methods=['POST'])
def process_data():
    data = request.get_json()
    result = {"data": "Successfully processed data", "received_data": data}
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
'''
View in web browser, curl or Postman to test the endpoints:
Profile check: GET to http://localhost:5000/profile
Greeting: GET to http://localhost:5000/greet/<YourName>
Process data: POST to http://localhost:5000/process with a JSON payload (e.g., {"key": "value"})
'''
