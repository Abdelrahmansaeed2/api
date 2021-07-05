#performing flask imports

from flask import Flask,jsonify



app = Flask(__name__) #intance of our flask application 

#Route '/' to facilitate get request from our flutter web
@app.route('/', methods = ['GET'])
def valuex():
    x ="hi";
    return jsonify({'greetings' : x}) #returning key-value pair in json format


if __name__ == "__main__":
    
        app.run() #debug will allow changes without shutting down the server 
        