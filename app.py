# importing dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_costa

# Creating an instance of Flask
app = Flask(__name__)

# # Use PyMongo to establish Mongo connection
# mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")

# Routing to render index.html template using data from Mongo
@app.route("/")




# Route that will trigger the scrape function
@app.route("/scrape")



if __name__ == "__main__":
    app.run(debug=True)