# importing dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo


# Creating an instance of Flask
app = Flask(__name__)

# creating a connection variable
conn = 'mongodb://localhost:27017'

# passing the connectionn to the pymongo instance
client = pymongo.MongoClient(conn)

# connect to database
db = client.mars_db

# drop collection if available to remove duplicates
# db.mars_mission.drop()


# # Use PyMongo to establish Mongo connection
# mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")

# Routing to render index.html template using data from Mongo
@app.route("/")
def index():


    return render_template('index.html', )



# Route that will trigger the scrape function
@app.route("/scrape")
    



if __name__ == "__main__":
    app.run(debug=True)