from flask import Flask, render_template
#from flask import jsonify
#from flask import request
#from flask_pymongo import PyMongo

app = Flask(__name__)

#app.config['MONGO_DBNAME'] = 'nba'
#app.config['MONGO_URI'] = 'mongodb://nba_user:ready2go@ds111638.mlab.com:11638/nba'

#mongo = PyMongo(app)

#@app.route('/db', methods=['GET'])
#def parse_request():
  #data = mongo.db.nba
  #output = []
  #for s in data.find():
    #output.append({'Player_Name' : s['Player_Name'], 'Games' : s['Games']})
  #return jsonify({'result' : output})

  #MONGODB_HOST = 'localhost'
#MONGODB_PORT = 27017
#DBS_NAME = 'donorschoose'
#COLLECTION_NAME = 'projects'
#FIELDS = {'school_state': True, 'resource_type': True, 'poverty_level': True, 'date_posted': True, 'total_donations': True, '_id': False}

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/barchart")
def barchart():
  return render_template("index.html")

@app.route("/piechart")
def piechart():
  return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)