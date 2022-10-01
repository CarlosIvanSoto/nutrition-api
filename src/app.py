from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({"message": "Pong!"})
    
#add routes tasks
#app.register_blueprint(#NAME)

if __name__ == "__main__":
   app.run(debug=True)