from flask import Flask, request, jsonify
import threading

app = Flask(__name__)

@app.route('/api/command', methods=['POST'])
def handle_command():
    data = request.json
    text = data.get('text')
    # This should forward to the main Jarvis parser
    # For demo: Simple print + echo
    print("WSBridge received:", text)
    resp = {"status": "parsed", "text": text}
    return jsonify(resp)

def run_ws_bridge(port=8080):
    app.run(host='0.0.0.0', port=port, debug=False)

if __name__ == "__main__":
    run_ws_bridge()
