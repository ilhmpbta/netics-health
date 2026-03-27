import time
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)
START_TIME = time.time()

@app.route('/health', methods=['GET'])
def health():
    current_time = time.time()
    uptime_seconds = current_time - START_TIME
    
    data = {
        "nama": "Bintang Ilham Pabeta",
        "nrp": "5025241152",
        "status": "UP",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "uptime": f"{int(uptime_seconds)} seconds"
    }
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6767)