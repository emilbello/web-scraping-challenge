# importing dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo   
import scrape_mars

# Creating an instance of Flask
app = Flask(__name__)

# talking to MongoDB
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


# Routing to render index.html template using data from Mongo
@app.route("/")
def index():
    # quering the mongo database
    mars = mongo.db.mars_dict.find_one()

    # Return template and data
    return render_template("index.html", mars=mars)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    # run the scrape function
    mars_data = scrape_mars.scrape()
    
    # Update/insert the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)
    
    return redirect("/", code=302)



if __name__ == "__main__":
    app.run(debug=True)