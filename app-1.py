from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
# Import scrape_mars
import scrape_mars3

# Import pymongo library, which lets me connect my Flask app to my Mongo database.
import pymongo

# Create an instance of my Flask app.
app = Flask(__name__)

# Create connection variable
conn = "mongodb://localhost:27017/scrape_mars3"
app.config["MONGO_URI"] = "mongodb://localhost:27017/scrape_mars3"
mongo = PyMongo(app)


# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)
db = client.mars_data1
collection = db.mars_data1

# Set route
@app.route("/")
def index1():
    # mars = client.db.mars.find_one()
    mars = mongo.db.mars.find_one()
    return render_template("index1.html", mars=mars)

# Scrape 
@app.route("/scrape")
def scrape():
    mars1 = client.db.mars
    mars1 = mongo.db.mars1 
    mars_data1 = scrape_mars3.scrape()
    print(mars_data1)
    mars1.update({}, mars_data1,upsert=True )
    return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)