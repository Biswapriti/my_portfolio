from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow CORS for local testing

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if not name or not email or not message:
        return jsonify({'status': 'error', 'message': 'All fields are required'}), 400

    # Simulating success response (replace with DB/email logic)
    return jsonify({'status': 'success', 'message': 'Form submitted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
