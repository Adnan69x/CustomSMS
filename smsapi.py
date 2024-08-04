from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/smsapi', methods=['GET'])
def smsapi():
    number = request.args.get('number')
    message = request.args.get('message')

    if not number or not message:
        return jsonify({'error': "Both 'number' and 'message' parameters are required."}), 400

    # Here you can add logic to send SMS using an SMS gateway API
    # For this example, we will just return the message
    return jsonify({'message': f"Message to {number}: {message}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Ensure the port is open in your VPS firewall settings
