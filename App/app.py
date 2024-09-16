from flask import Flask, jsonify,request,Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins for all routes


@app.route('/room_305', methods=['POST'])
def button1():

    print("Robot Moving to Room 305")
    
    # print("Button was pressed!")
    return jsonify({"status": "success", "message": "Moving To 305"})


@app.route('/room_311', methods=['POST'])
def button2():
    
    print("Robot Moving to Room 311")
    # print("Button was pressed!")
    return jsonify({"status": "success", "message": "Moving To 311"})

if __name__ == '__main__':
    app.run(debug=True,port=5555)



# from flask import Flask, jsonify
# import threading
# import time

# app = Flask(__name__)

# count = 0

# def increment_counter():
#     global count
#     while True:
#         time.sleep(1)
#         count += 1



# @app.route('/get_count', methods=['GET'])
# def get_count():
#     global count
#     return jsonify({"count": count})

# if __name__ == '__main__':
#     # Start the background thread
#     thread = threading.Thread(target=increment_counter)
#     thread.daemon = True
#     thread.start()
    
#     app.run(debug=True, host='0.0.0.0', port=5555)


